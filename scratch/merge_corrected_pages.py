import re
import os
import sys
import io

# Cấu hình UTF-8 cho stdout/stderr trên Windows
if sys.platform.startswith('win'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

ORIGINAL_FILE = "./documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md"
BACKUP_FILE = "./documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md.bak"
CORRECTED_DIR = "./scratch/ocr_corrected/"
PAGES_TO_FIX = [9, 10, 15, 22, 24, 26, 27, 30, 31, 50, 131, 153, 226, 254, 290, 297, 369, 384, 419, 442, 450, 458, 481, 488, 497, 500, 520, 529, 538, 580]

def clean_ocr_text(text):
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text

def merge_pages():
    # Read from BACKUP_FILE if it exists, otherwise ORIGINAL_FILE
    source_file = BACKUP_FILE if os.path.exists(BACKUP_FILE) else ORIGINAL_FILE
    print(f"[*] Đang đọc file nguồn: {source_file}")
    if not os.path.exists(source_file):
        print("[!] Không tìm thấy file nguồn.")
        return

    with open(source_file, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Tạo bản sao lưu nếu chưa tồn tại
    if not os.path.exists(BACKUP_FILE):
        print(f"[*] Tạo bản sao lưu tại: {BACKUP_FILE}")
        with open(BACKUP_FILE, "w", encoding="utf-8") as f:
            f.write(content)

    # Tìm các mốc trang: ## TRANG <số trang>
    page_regex = re.compile(r'^##\s+TRANG\s+(\d+)', re.MULTILINE | re.IGNORECASE)
    
    # Tìm tất cả các khớp và vị trí của chúng
    matches = list(page_regex.finditer(content))
    print(f"[*] Tìm thấy {len(matches)} nhãn trang trong file.")
    
    # Trích xuất phần header (trước nhãn trang đầu tiên)
    first_match = matches[0]
    header = content[:first_match.start()]
    
    # Tách các trang
    pages_dict = {} # page_num -> list of text
    ordered_page_nums = []
    
    for i in range(len(matches)):
        p_num = int(matches[i].group(1))
        start_idx = matches[i].end()
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(content)
        
        page_text = content[start_idx:end_idx]
        
        if p_num not in pages_dict:
            pages_dict[p_num] = []
            ordered_page_nums.append(p_num)
        pages_dict[p_num].append({
            'index': i,
            'text': page_text,
            'start_line': content.count('\n', 0, matches[i].start()) + 1
        })
        
    print(f"[*] Tổng số trang duy nhất (unique): {len(pages_dict)}")
    
    # Reassembly logic
    reconstructed_content = header
    
    # Chúng ta sẽ đi qua các trang từ 1 đến 585
    # Và chỉ ghi lại mỗi trang đúng 1 lần (loại bỏ duplicate)
    duplicate_removed = 0
    pages_updated = 0
    
    for p_num in range(1, 586):
        if p_num not in pages_dict:
            print(f"[!] Cảnh báo: Thiếu Trang {p_num} trong file gốc!")
            continue
            
        occurrences = pages_dict[p_num]
        
        # Chọn occurrence đầu tiên, bỏ qua các duplicate phía sau
        primary_occurrence = occurrences[0]
        if len(occurrences) > 1:
            print(f"[-] Phát hiện Trang {p_num} bị lặp {len(occurrences)} lần. Chỉ giữ lần xuất hiện đầu tiên (dòng {primary_occurrence['start_line']}).")
            duplicate_removed += len(occurrences) - 1
            
        page_text = primary_occurrence['text']
        
        # Kiểm tra xem trang này có nằm trong danh sách cần sửa lỗi không
        if p_num in PAGES_TO_FIX:
            corr_file = os.path.join(CORRECTED_DIR, f"page_{p_num:03d}.txt")
            if os.path.exists(corr_file):
                with open(corr_file, "r", encoding="utf-8") as cf:
                    new_text = cf.read().strip()
                
                # Làm sạch markdown backticks nếu mô hình xuất thừa ra
                new_text = clean_ocr_text(new_text)
                
                # Format lại ranh giới trang: thêm khoảng trống và dấu phân tách trang "---"
                # Đảm bảo giữ nguyên cấu trúc chuẩn
                old_len = len(page_text.strip())
                new_len = len(new_text)
                
                # Thay thế
                page_text = "\n\n" + new_text + "\n\n---\n"
                pages_updated += 1
                print(f"[v] Đã cập nhật Trang {p_num}: {old_len} ký tự -> {new_len} ký tự (từ {corr_file})")
            else:
                print(f"[!] Cảnh báo: Cần sửa Trang {p_num} nhưng không tìm thấy file {corr_file}")
                
        # Thêm nhãn trang và nội dung vào file reconstructed
        reconstructed_content += f"## TRANG {p_num}{page_text}"
        
    # Ghi đè lại file gốc
    print(f"[*] Đang ghi kết quả đã merge vào: {ORIGINAL_FILE}")
    with open(ORIGINAL_FILE, "w", encoding="utf-8") as f:
        f.write(reconstructed_content)
        
    print("-" * 50)
    print(f"[*] THÀNH CÔNG:")
    print(f"    - Số trang được cập nhật từ OCR mới: {pages_updated}")
    print(f"    - Số trang trùng lặp bị loại bỏ: {duplicate_removed}")
    print(f"    - File kết quả: {ORIGINAL_FILE}")

if __name__ == '__main__':
    merge_pages()
