# KẾ HOẠCH AUDIT VÀ SỬA LỖI OCR TÀI LIỆU "BẢN SẮC VĂN HÓA VIỆT NAM"
<!-- Audit method: Programmatic scan & Manual RCA cross-reference -->
<!-- Target Model: qwen2.5vl:7b-fp16 (Ollama) | Document: BanSacVanHoaVietNam_Phan_Ngoc.md -->
<!-- Date: 2026-06-11 | Status: DRAFT — Awaiting execution -->

## THÔNG TIN CHUNG (METADATA)

```yaml
document_type     : ocr_audit_corrective_plan
subject           : Sách "Bản Sắc Văn Hóa Việt Nam" — Tác giả Phan Ngọc
target_document   : documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md (974KB, 7714 dòng)
source_images_dir : documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/ (585 ảnh PNG)
original_ocr_model: qwen2.5vl:3b (mô hình nhỏ)
corrective_model  : qwen2.5vl:7b-fp16 (đang chạy trên Ollama nội bộ)
methodology       :
  - Phase 1: Programmatic Audit (Độ dài trang, Vòng lặp văn bản, Ký tự lạ)
  - Phase 2: Manual RCA Comparison (So sánh đối chứng ngẫu nhiên với ảnh nguồn)
  - Phase 3: Selective High-Quality OCR (Chỉ quét lại các trang hỏng bằng mô hình qwen2.5vl:7b-fp16)
  - Phase 4: Automated Content Merging & Quality Validation
status            : DRAFT — Awaiting approval
```

---

## 1. TÓM TẮT ĐÁNH GIÁ HIỆN TRẠNG (EXECUTIVE SUMMARY)

Tài liệu [BanSacVanHoaVietNam_Phan_Ngoc.md](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md) được chuyển đổi bằng mô hình `qwen2.5vl:3b` hiện gặp nhiều lỗi nghiêm trọng về cấu trúc và chính tả tiếng Việt:
1.  **Lỗi cấu trúc cực kỳ nghiêm trọng (Critical Structural Failures):** Gồm 11 trang bị cắt xén nội dung (chỉ chứa 1 dòng lửng lơ hoặc mất hoàn toàn các chương mục), 2 trang bị lặp văn bản tuần hoàn (vòng lặp vô hạn dạng thẻ HTML ảo), và 1 trang bị duplicate hoàn toàn ở cuối tài liệu.
2.  **Lỗi chính tả và dấu tiếng Việt (Severe Orthographic Errors):** Do mô hình `3b` quá nhỏ nên khả năng nhận diện dấu phụ (ă, â, ô, ơ) và dấu thanh (hỏi, ngã, nặng) rất kém, dẫn đến sai lệch ngữ nghĩa (ví dụ: "chính đảng" $\rightarrow$ "chính đáng", "phản văn hóa" $\rightarrow$ "phần văn hóa").
3.  **Chi phí tính toán tối ưu:** Thay vì chạy OCR lại toàn bộ 585 trang (tốn kém tài nguyên và thời gian), kế hoạch này đề xuất **chỉ quét lại 18 trang bị hư hại nặng** bằng mô hình thị giác lớn hơn `qwen2.5vl:7b-fp16` đang chạy cục bộ trên hệ thống và chạy tập lệnh tự động ghi đè/merge kết quả vào file `.md` hiện tại.

---

## 2. DANH SÁCH CÁC TRANG BỊ HỎNG (DAMAGED PAGES INVENTORY)

Qua đối chiếu tập lệnh kiểm tra tự động (`comprehensive_ocr_audit.py`) và tài liệu phân tích lỗi gốc (`RCA_BanSacVanHoaVietNam.md`), dưới đây là danh sách **18 trang bị lỗi nặng cần quét lại**:

### 2.1. Nhóm lỗi cấu trúc nghiêm trọng (Critical Structural Failures — 12 trang)

| Trang | Dòng MD | Mức độ | Loại lỗi | Mô tả chi tiết lỗi | Ảnh nguồn đối chứng |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **6 (cuối)** | 7704–7714 | 🔴 Đỏ | Trùng lặp (Duplicate) | Nội dung Trang 6 bị lặp lại hoàn toàn ở cuối tài liệu (sau trang 585). Cần xóa bỏ. | [page_006.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_006.png) |
| **9** | 93–108 | 🔴 Đỏ | Trộn & Cụt (Scrambled) | Mục lục bị đứt quãng nghiêm trọng. Mất toàn bộ từ Chương VII đến Chương XI. Trộn lẫn nội dung Chương XII-XIII từ Trang 10 nhảy sang. | [page_009.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_009.png) |
| **10** | 111–123 | 🟠 Cam | Trùng & Đảo lộn | Chứa nội dung lặp lại từ Trang 9 nhảy sang, cấu trúc các chương mục bị đảo lộn. | [page_010.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_010.png) |
| **27** | 315–321 | 🔴 Đỏ | Cắt xén (Truncated) | Chỉ chứa 1 dòng lửng (53 ký tự), kết thúc bằng chữ "lí...". Mất gần như toàn bộ trang. | [page_027.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_027.png) |
| **50** | 601–615 | 🔴 Đỏ | Vòng lặp (Text Loop) | Bị lặp văn bản dài dạng thẻ HTML đóng mở ảo do mô hình hallucinate định dạng. | [page_050.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_050.png) |
| **131** | 1557–1600 | 🔴 Đỏ | Vòng lặp & Ghép trang | Trang quá dài (5804 ký tự). Nội dung bị lặp lại tuần hoàn và đóng khung bởi thẻ HTML ảo `<thời Tấn...></thời Tấn...>` ở đầu và cuối trang. | [page_131.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_131.png) |
| **153** | 1808–1814 | 🔴 Đỏ | Cắt xén (Truncated) | Chỉ chứa chữ "Chương VI" (9 ký tự). Mất toàn bộ nội dung còn lại của chương. | [page_153.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_153.png) |
| **226** | 2783–2789 | 🔴 Đỏ | Cắt xén (Truncated) | Chỉ chứa 1 dòng cụt (54 ký tự). Mất phần lớn nội dung trang. | [page_226.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_226.png) |
| **254** | 3099–3104 | 🔴 Đỏ | Cắt xén (Truncated) | Chỉ chứa 1 dòng cụt (76 ký tự). Mất phần lớn nội dung trang. | [page_254.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_254.png) |
| **290** | 3550–3556 | 🔴 Đỏ | Cắt xén (Truncated) | Chỉ chứa 1 dòng cụt (52 ký tự). Mất phần lớn nội dung trang. | [page_290.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_290.png) |
| **297** | 3682–3687 | 🔴 Đỏ | Cắt xén (Truncated) | Trang mục lục chỉ chứa duy nhất 1 dòng mục lục cụt ngủn ("Hiểu Kinh : 1"). | [page_297.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_297.png) |
| **481** | 6450–6456 | 🔴 Đỏ | Cắt xén (Truncated) | Trang tiêu đề chương chỉ chứa chữ "Chương XIV" (10 ký tự). Mất toàn bộ nội dung của chương. | [page_481.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_481.png) |

### 2.2. Nhóm lỗi chính tả nặng (Severe Orthography Failures — 6 trang)

| Trang | Dòng MD | Mức độ | Loại lỗi | Lỗi cụ thể (Sai lệch ngữ nghĩa) | Ảnh nguồn đối chứng |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **15** | 183–205 | 🟠 Cam | Sai dấu thanh | "có mà thôi" $\rightarrow$ "có mày thôi"; "chính đảng" $\rightarrow$ "chính đáng". | [page_015.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_015.png) |
| **22** | 257–266 | 🟠 Cam | Từ vựng & Dấu | "phản văn hóa" $\rightarrow$ "phần văn hóa"; mất từ chuyển tiếp "xáo trộn". | [page_022.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_022.png) |
| **24** | 280–288 | 🟠 Cam | Sai ký tự phụ | "văn hóa" $\rightarrow$ "văn lóa"; "mở đầu" $\rightarrow$ "mớ đầu". | [page_024.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_024.png) |
| **26** | 302–310 | 🟠 Cam | Sai dấu thanh/từ | "nhường chỗ" $\rightarrow$ "nhưn chở"; "bộc lộ" $\rightarrow$ "bộ lộ". | [page_026.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_026.png) |
| **30** | 344–350 | 🟠 Cam | Sai dấu thanh/phụ | "bổn phận" $\rightarrow$ "bốn phận"; "ở" $\rightarrow$ "ơ". | [page_030.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_030.png) |
| **31** | 357–367 | 🟠 Cam | Sai dấu thanh | "chứng minh" $\rightarrow$ "chúng mình". | [page_031.png](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/page_031.png) |

---

## 3. KẾ HOẠCH THỰC THI (CORRECTIVE SCAN PLAN)

### Kịch bản xử lý tự động hóa (Automated Re-OCR & Integration Pipeline):

```
[18 Ảnh Nguồn Trang Hỏng] ──► [OCR bằng Qwen2.5:7b] ──► [Markdown Thô]
                                                               │
                                                               ▼
[BanSacVanHoaVietNam_Phan_Ngoc.md] ◄── [Merge Script] ◄── [Hậu Xử Lý]
(Xóa Trang 6 trùng lặp, cập nhật 17 trang còn lại)
```

### Bước 1: Chuẩn bị danh sách ảnh nguồn của các trang bị hỏng
Các trang bị hỏng sẽ tương ứng với các ảnh nguồn sau trong thư mục `BanSacVanHoaVietNam_Phan_Ngoc_pages/`:
- Trang 9 $\rightarrow$ `page_009.png`
- Trang 10 $\rightarrow$ `page_010.png`
- Trang 15 $\rightarrow$ `page_015.png`
- Trang 22 $\rightarrow$ `page_022.png`
- Trang 24 $\rightarrow$ `page_024.png`
- Trang 26 $\rightarrow$ `page_026.png`
- Trang 27 $\rightarrow$ `page_027.png`
- Trang 30 $\rightarrow$ `page_030.png`
- Trang 31 $\rightarrow$ `page_031.png`
- Trang 50 $\rightarrow$ `page_050.png`
- Trang 131 $\rightarrow$ `page_131.png`
- Trang 153 $\rightarrow$ `page_153.png`
- Trang 226 $\rightarrow$ `page_226.png`
- Trang 254 $\rightarrow$ `page_254.png`
- Trang 290 $\rightarrow$ `page_290.png`
- Trang 297 $\rightarrow$ `page_297.png`
- Trang 481 $\rightarrow$ `page_481.png`

### Bước 2: Thiết lập Prompt OCR tối ưu cho Qwen 2.5 7B
Để khắc phục triệt để các lỗi của mô hình `3b` cũ, prompt dành cho mô hình `qwen2.5:7b` (hoặc `qwen2.5vl:7b`) cần được thiết kế chặt chẽ:

```markdown
Bạn là một chuyên gia số hóa sách cổ và tài liệu học thuật tiếng Việt chất lượng cao.
Hãy thực hiện OCR ảnh trang sách đính kèm và tuân thủ các quy tắc nghiêm ngặt sau:
1. Trích xuất chính xác 100% văn bản tiếng Việt. Đặc biệt cẩn thận với các dấu phụ (ă, â, ô, ơ, ư) và dấu thanh (hỏi, ngã, nặng). Không đoán mò hoặc tự ý sửa từ nếu ảnh mờ, hãy giữ nguyên và thêm ký tự đại diện [?] nếu không thể đọc được.
2. Tuyệt đối không xuất ra bất kỳ thẻ HTML nào (như <html>, <p>, <div>, hoặc các thẻ tự đóng đóng giả lập).
3. Tuyệt đối không để xảy ra hiện tượng lặp lại văn bản tuần hoàn (vòng lặp). Chỉ xuất nội dung trang sách một lần duy nhất từ đầu đến cuối.
4. Giữ nguyên định dạng xuống dòng của các đoạn văn. Nếu có chú thích cuối trang (footnote) hoặc số trang in ở chân trang, hãy tách riêng ra bằng một dòng kẻ phụ "---".
5. Đầu ra chỉ chứa văn bản Markdown của trang sách, không chứa bất kỳ lời giải thích hoặc mã bọc ngoài nào khác.
```

### Bước 3: Chạy OCR chọn lọc (Selective Batch OCR)
Sử dụng script Python kết nối trực tiếp đến API của local Ollama (`http://localhost:11434/api/generate`) để gửi ảnh nguồn dưới dạng base64 cùng prompt xử lý qua mô hình `qwen2.5vl:7b-fp16`.

**Tập lệnh Python chạy OCR sửa lỗi (`run_corrective_ocr.py`):**
```python
import os
import base64
import json
import urllib.request

# Cấu hình API của local Ollama
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5vl:7b-fp16"

PROMPT = """Bạn là một chuyên gia số hóa sách cổ và tài liệu học thuật tiếng Việt chất lượng cao.
Hãy thực hiện OCR ảnh trang sách đính kèm và tuân thủ các quy tắc nghiêm ngặt sau:
1. Trích xuất chính xác 100% văn bản tiếng Việt. Đặc biệt cẩn thận với các dấu phụ (ă, â, ô, ơ, ư) và dấu thanh (hỏi, ngã, nặng). Không đoán mò hoặc tự ý sửa từ nếu ảnh mờ, hãy giữ nguyên và thêm ký tự đại diện [?] nếu không thể đọc được.
2. Tuyệt đối không xuất ra bất kỳ thẻ HTML nào (như <html>, <p>, <div>, hoặc các thẻ tự đóng đóng giả lập).
3. Tuyệt đối không để xảy ra hiện tượng lặp lại văn bản tuần hoàn (vòng lặp). Chỉ xuất nội dung trang sách một lần duy nhất từ đầu đến cuối.
4. Giữ nguyên định dạng xuống dòng của các đoạn văn. Nếu có chú thích cuối trang (footnote) hoặc số trang in ở chân trang, hãy tách riêng ra bằng một dòng kẻ phụ "---".
5. Đầu ra chỉ chứa văn bản Markdown của trang sách, không chứa bất kỳ lời giải thích hoặc mã bọc ngoài nào khác."""

# Danh sách 17 trang bị hỏng cần quét lại (Trang 6 bị duplicate cuối file sẽ được xóa bỏ, không cần quét)
PAGES_TO_FIX = [9, 10, 15, 22, 24, 26, 27, 30, 31, 50, 131, 153, 226, 254, 290, 297, 481]
IMAGES_DIR = "./documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc_pages/"
OUTPUT_DIR = "./scratch/ocr_corrected/"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for p in PAGES_TO_FIX:
    img_path = os.path.join(IMAGES_DIR, f"page_{p:03d}.png")
    out_path = os.path.join(OUTPUT_DIR, f"page_{p:03d}.txt")
    
    if not os.path.exists(img_path):
        print(f"[-] Không tìm thấy ảnh: {img_path}")
        continue
        
    print(f"[+] Đang chạy OCR Trang {p} bằng model {MODEL_NAME}...")
    
    # Encode ảnh sang Base64
    with open(img_path, "rb") as image_file:
        img_base64 = base64.b64encode(image_file.read()).decode("utf-8")
        
    # Chuẩn bị payload gửi Ollama
    payload = {
        "model": MODEL_NAME,
        "prompt": PROMPT,
        "images": [img_base64],
        "stream": False,
        "options": {
            "temperature": 0.1
        }
    }
    
    req = urllib.request.Request(
        OLLAMA_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req) as res:
            resp_data = json.loads(res.read().decode("utf-8"))
            text_out = resp_data.get("response", "").strip()
            
            # Lưu file markdown thô của trang
            with open(out_path, "w", encoding="utf-8") as out_file:
                out_file.write(text_out)
            print(f"[v] Hoàn thành Trang {p} -> {out_path}")
    except Exception as e:
        print(f"[x] Lỗi khi xử lý Trang {p}: {e}")
```

### Bước 4: Tự động hóa việc ghi đè và đồng bộ (Auto-Merging)
Sử dụng một script Python `merge_corrected_pages.py` để thực hiện:
1.  Đọc file `.md` gốc `BanSacVanHoaVietNam_Phan_Ngoc.md`.
2.  Xóa bỏ đoạn text trùng lặp của **Trang 6 ở cuối tài liệu** (từ dòng 7704 đến hết).
3.  Tìm ranh giới của các trang cần cập nhật bằng cách định vị thẻ `## TRANG N` và dấu ranh giới `---` tiếp theo hoặc thẻ `## TRANG N+1`.
4.  Thay thế nội dung bị hỏng bằng nội dung chất lượng cao tương ứng trong thư mục `scratch/ocr_corrected/page_NNN.txt`.
5.  Ghi lại file `.md` dưới dạng mã hóa UTF-8 chuẩn.

---

## 4. TIÊU CHÍ HOÀN THÀNH VÀ KIỂM ĐỊNH (DEFINITION OF DONE & VALIDATION)

Quy trình sửa lỗi chỉ được coi là hoàn tất khi đáp ứng các điều kiện sau:
- [ ] **Tính toàn vẹn cấu trúc:** Không còn bất kỳ trang nào bị lặp lại ở cuối file (Trang 6 trùng lặp đã được xóa bỏ hoàn toàn).
- [ ] **Độ dài trang tối thiểu:** Các trang 27, 153, 226, 254, 290, 481 sau khi cập nhật phải có độ dài văn bản tối thiểu $\ge 400$ ký tự và có nghĩa hoàn chỉnh (không kết thúc lửng lơ).
- [ ] **Loại bỏ thẻ HTML ảo:** Kiểm tra không còn bất kỳ thẻ đóng/mở dạng `<thống tổ chức...>` hay `<thời Tấn...>` nào xuất hiện trong toàn bộ file `.md`.
- [ ] **Kiểm định di học thuật (Spellcheck Gate):** Chạy kiểm tra chính tả ngẫu nhiên trên các trang đã sửa (Trang 15, 22, 24, 26, 30, 31) để đảm bảo các lỗi diacritic nghiêm trọng đã được khắc phục hoàn toàn.
