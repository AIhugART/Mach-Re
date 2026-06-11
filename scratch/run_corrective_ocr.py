import os
import base64
import json
import urllib.request
import time
import sys
import io

# Cấu hình UTF-8 cho stdout/stderr trên Windows
if sys.platform.startswith('win'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Cấu hình API của local Ollama
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5vl:7b-fp16"

PROMPT = """Bạn là một chuyên gia số hóa sách cổ và tài liệu học thuật tiếng Việt chất lượng cao.
Hãy thực hiện OCR ảnh trang sách đính kèm và tuân thủ các quy tắc nghiêm ngặt sau:
1. Trích xuất chính xác 100% văn bản tiếng Việt. Đặc biệt cẩn thận với các dấu phụ (ă, â, ô, ơ, ư) và dấu thanh (hỏi, ngã, nặng). Không đoán mò hoặc tự ý sửa từ nếu ảnh mờ, hãy giữ nguyên và thêm ký tự đại diện [?] nếu không thể đọc được.
2. Tuyệt đối không xuất ra bất kỳ thẻ HTML nào (như <html>, <p>, <div>, hoặc các thẻ tự đóng đóng giả lập).
3. Tuyệt đối không để xảy ra hiện tượng lặp lại văn bản tuần hoàn (vòng lặp). Chỉ xuất nội dung trang sách một lần duy nhất từ đầu đến cuối.
4. Giữ nguyên định dạng xuống dòng của các đoạn văn. Nếu có chú thích cuối trang (footnote) hoặc số trang in ở chân trang, hãy tách riêng ra bằng một dòng kẻ phụ "---".
5. Đầu ra chỉ chứa văn bản Markdown của trang sách, không chứa bất kỳ lời giải thích hoặc mã bọc ngoài nào khác.
"""

# Danh sách các trang bị hỏng/lỗi cần quét lại
PAGES_TO_FIX = [9, 10, 15, 22, 24, 26, 27, 30, 31, 50, 131, 153, 226, 254, 290, 297, 369, 384, 419, 442, 450, 458, 481, 488, 497, 500, 520, 529, 538, 580]
IMAGES_DIR = "./documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/"
OUTPUT_DIR = "./scratch/ocr_corrected/"

def run_batch_ocr():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"[*] Bắt đầu tiến trình chạy OCR với {MODEL_NAME}")
    print(f"[*] Thư mục ảnh nguồn: {IMAGES_DIR}")
    print(f"[*] Thư mục kết quả: {OUTPUT_DIR}")
    print(f"[*] Tổng số trang cần sửa: {len(PAGES_TO_FIX)}")
    print("-" * 50)
    
    start_time = time.time()
    
    for idx, p in enumerate(PAGES_TO_FIX):
        img_path = os.path.join(IMAGES_DIR, f"page_{p:03d}.png")
        out_path = os.path.join(OUTPUT_DIR, f"page_{p:03d}.txt")
        
        # Nếu đã có file và dung lượng > 10 bytes, bỏ qua để hỗ trợ resume
        if os.path.exists(out_path) and os.path.getsize(out_path) > 10:
            print(f"[{idx+1}/{len(PAGES_TO_FIX)}] Trang {p} đã tồn tại kết quả. Bỏ qua.")
            continue
            
        if not os.path.exists(img_path):
            print(f"[{idx+1}/{len(PAGES_TO_FIX)}] [!] Không tìm thấy ảnh: {img_path}")
            continue
            
        print(f"[{idx+1}/{len(PAGES_TO_FIX)}] Đang quét Trang {p}...")
        
        # Encode ảnh sang Base64
        try:
            with open(img_path, "rb") as image_file:
                img_base64 = base64.b64encode(image_file.read()).decode("utf-8")
        except Exception as e:
            print(f"[-] Lỗi đọc file ảnh Trang {p}: {e}")
            continue
            
        # Chuẩn bị payload gửi Ollama
        payload = {
            "model": MODEL_NAME,
            "prompt": PROMPT,
            "images": [img_base64],
            "stream": False,
            "options": {
                "temperature": 0.1,
                "num_ctx": 4096
            }
        }
        
        req = urllib.request.Request(
            OLLAMA_API_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        
        try:
            p_start = time.time()
            with urllib.request.urlopen(req) as res:
                resp_data = json.loads(res.read().decode("utf-8"))
                text_out = resp_data.get("response", "").strip()
                
                # Lưu file markdown thô của trang
                with open(out_path, "w", encoding="utf-8") as out_file:
                    out_file.write(text_out)
                
                p_elapsed = time.time() - p_start
                print(f"[v] Thành công Trang {p} ({p_elapsed:.1f}s) -> {out_path}")
        except Exception as e:
            print(f"[x] Lỗi gọi API cho Trang {p}: {e}")
            
    total_elapsed = time.time() - start_time
    print("-" * 50)
    print(f"[*] Hoàn tất toàn bộ lô quét trong {total_elapsed:.1f} giây.")

if __name__ == '__main__':
    run_batch_ocr()
