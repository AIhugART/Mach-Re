import os
import re
import base64
import requests
import time

MD_PATH = r"C:\Stable_Diffusion\MACH_RE\documents\public_documents\ban_sac.md"
EXTRACTED_DIR = r"C:\Stable_Diffusion\MACH_RE\documents\public_documents\extracted_pages"
MODEL_NAME = "qwen2.5vl:3b"

def run_ollama_ocr(image_path, system_prompt):
    try:
        with open(image_path, "rb") as f:
            img_base64 = base64.b64encode(f.read()).decode("utf-8")
        
        payload = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": "Please transcribe the text in this page exactly. Output only the transcription in Markdown format.", "images": [img_base64]}
            ],
            "options": {
                "temperature": 0.1,
                "top_p": 0.9,
                "num_predict": 4096
            },
            "stream": False
        }
        
        response = requests.post("http://127.0.0.1:11434/api/chat", json=payload, timeout=900)
        response.raise_for_status()
        content = response.json().get("message", {}).get("content", "")
        return content.strip()
    except Exception as e:
        print(f"\n[ERROR] Failed to process {os.path.basename(image_path)}: {str(e)}")
        return f"\n* [Lỗi nhận diện trang {os.path.basename(image_path)}: {str(e)}]* \n"

def parse_md_into_sections(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Split content by the "## TRANG " sections, keeping the separators
    # We want to segment the file by matching '## TRANG \d+'
    parts = re.split(r"(## TRANG \d+\n)", content)
    
    header = parts[0]
    sections = []
    
    # re.split keeps the captured group, so parts will be:
    # [header, "## TRANG 1\n", "content 1", "## TRANG 2\n", "content 2", ...]
    for i in range(1, len(parts), 2):
        title = parts[i]
        body = parts[i+1] if i+1 < len(parts) else ""
        
        # Extract page number
        m = re.match(r"## TRANG (\d+)", title)
        page_num = int(m.group(1)) if m else i // 2
        
        sections.append({
            "title": title,
            "body": body,
            "page_num": page_num
        })
        
    return header, sections

def save_md(md_path, header, sections):
    # Temp file write then rename to avoid file corruption
    temp_path = md_path + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(header)
        for sec in sections:
            f.write(sec["title"])
            f.write(sec["body"])
    
    if os.path.exists(md_path):
        os.remove(md_path)
    os.rename(temp_path, md_path)

def process_batch():
    system_prompt = (
        "You are an expert OCR engine. Transcribe the Vietnamese text in this image precisely. "
        "Preserve line breaks, paragraphs, and markdown headings where appropriate. "
        "Output ONLY the transcribed text without any conversational preamble or notes."
    )
    
    print("Reading and parsing ban_sac.md...")
    header, sections = parse_md_into_sections(MD_PATH)
    
    # Identify empty pages
    empty_indices = []
    for idx, sec in enumerate(sections):
        # Clean up separators like ---
        cleaned_body = sec["body"].replace("---", "").strip()
        if not cleaned_body:
            empty_indices.append(idx)
            
    total_empty = len(empty_indices)
    print(f"Found {total_empty} empty pages out of {len(sections)} total pages.")
    
    if total_empty == 0:
        print("No empty pages to process. Finalized!")
        return

    print(f"Beginning OCR processing using {MODEL_NAME}...")
    success_count = 0
    
    for i, idx in enumerate(empty_indices):
        sec = sections[idx]
        page = sec["page_num"]
        
        # Find image path
        img_path = os.path.join(EXTRACTED_DIR, f"page_{page:03d}.png")
        if not os.path.exists(img_path):
            img_path = os.path.join(EXTRACTED_DIR, f"page_{page}.png")
            
        if not os.path.exists(img_path):
            print(f"[{i+1}/{total_empty}] Page {page}: Image not found ({img_path}). Skipping.")
            continue
            
        print(f"[{i+1}/{total_empty}] Processing Page {page} ({os.path.basename(img_path)})...", end="", flush=True)
        start_time = time.time()
        
        # Run OCR
        transcription = run_ollama_ocr(img_path, system_prompt)
        
        # Clean up any markdown code fence blocks if returned by model
        transcription = re.sub(r"^```markdown\n", "", transcription)
        transcription = re.sub(r"^```\n", "", transcription)
        transcription = re.sub(r"\n```$", "", transcription)
        transcription = transcription.strip()
        
        # Format the body
        sec["body"] = f"\n\n{transcription}\n\n---\n\n"
        
        # Save incrementally
        save_md(MD_PATH, header, sections)
        
        elapsed = time.time() - start_time
        print(f" Success ({elapsed:.1f}s)")
        success_count += 1
        
    print(f"\nCompleted batch run! Successfully filled {success_count} blank pages.")

if __name__ == "__main__":
    process_batch()
