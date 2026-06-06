# Mạch Rễ — Kế Hoạch TÁI DỰNG Hệ Tiên Đề Từ Đầu (Rebuild · clean-slate re-derivation)

> **Loại:** REBUILD (không phải revision). **Thay thế** `mach-re-axiom-revision-plan.md` (v1) và `mach-re-axiom-revision-plan-v2.md`. Hai file đó giữ làm tham chiếu lịch sử.
> **Quyết định người dùng (2026-06-06):**
> 1. **Re-derive hệ tiên đề từ nguyên lý đầu** — KHÔNG cam kết với tập/số lượng hiện tại (7, 8, hay 4+3). Tài liệu cũ = *reference only*. Kết quả có thể là hệ tiên đề khác hẳn.
> 2. **Thay** quy tắc "extend, not overwrite" bằng quy tắc **"rebuild + carry-forward set khai báo tường minh"**.
> **Cổng quyết định:** 3-round RCA × 5-Why × ≥4/5 (CLAUDE.md RULE ZERO).
> **Định dạng:** LLM-friendly Markdown — mỗi section độc lập.

---

## 0. TÓM TẮT (TL;DR)

| Phase | Tên | Sản phẩm | RCA |
|---|---|---|---|
| **P0** ✅ | Đổi governance | CLAUDE.md: thay "extend not overwrite" → "rebuild + carry-forward" — **ĐÃ XONG 2026-06-06** ([CLAUDE.md:126](../CLAUDE.md#L126)) | 4.4 |
| **P1** ✅ | Khai báo Carry-Forward Set | `dictionary §7` → "Carry-Forward Set" + backbone 3 hệ (A/B/C); `§9` hạ trạng thái — **ĐÃ XONG 2026-06-06** | 4.6 |
| **P2** ✅ | Re-derive tiên đề | [`axiom_spec.md`](../axiom_spec.md) — 4 Core + 3 Derived + 1 Meta; **ĐÃ XONG + 3 quyết định §5 đã giải bằng RCA 2026-06-06** (MA-1 IN · ID CA/DP/MA · CA-2 Nhị đế) | 4.6 |
| **P3** | Falsifiability + prior-art per axiom | Mỗi tiên đề có điều kiện phản chứng + nguồn kế thừa, ngay từ đầu | 4.6 |
| **P4** ◐ | Regenerate documents | **MẪU XONG:** [`axioms.html`](../axioms.html) render từ spec (đánh số La Mã đếm lại theo tầng — người dùng override CA/DP/MA). Còn lại ~9 HTML + archive chờ duyệt mẫu | 4.0 |
| **P5** | Cross-check + CHANGELOG | Quét nhất quán đa trang, ghi đợt rebuild | 4.6 |

**Nguyên tắc xương sống:** **Spec trước, tài liệu sau.** Mọi mâu thuẫn cũ (bảng nói ✅ độc lập / text nói derived; 7 vs 8) sinh ra vì *không có single source* — tài liệu tự định nghĩa lẫn nhau. Rebuild lần này: một `axiom_spec.md` là nguồn chân lý duy nhất, HTML chỉ *render* spec.

---

## 1. RCA — VÌ SAO REBUILD, KHÔNG PHẢI REVISION (xác nhận gốc)

**Round 1 — Triệu chứng:** 4 đời plan đều là vá-chồng-vá; v2 phải uốn éo giữ số La Mã + nhãn cũ trong khi đại phẫu.

**Round 2 — Cơ chế:** "extend, not overwrite" là quy tắc *bảo tồn* — đúng cho corpus đã ổn định, người ngoài phụ thuộc. Hệ tiên đề Mạch Rễ vẫn **chưa xuất bản, một tác giả, đang dò** (tự ghi "giả thuyết"). Áp quy tắc bảo tồn lên lý thuyết *đang được suy ra* → mỗi sửa khái niệm cõng chi phí tương thích ngược → **chính quy tắc chống mâu thuẫn lại đẻ mâu thuẫn** vì cấm thay sạch.

**Round 3 — Gốc (một câu):** Governance nhập quy tắc bảo tồn (hợp cho bản xuất bản) áp lên lõi còn bất ổn, nên bản sửa tích tụ thành nhãn-chồng-nhãn thay vì suy lại sạch.

**Fix gốc:** Cho phép suy lại sạch (rebuild), nhưng chặn rủi ro *mất giá trị do tai nạn* bằng một **Carry-Forward Set khai báo tường minh** (P1). Đây là điểm Bảo-tồn-2/5 được nâng lên 4 trong phiên bản có trách nhiệm.

---

## 2. P0 — ĐỔI GOVERNANCE (làm đầu tiên, trước mọi thứ)

### 2.1 Đoạn bị thay trong CLAUDE.md §"Document contract rules"
❌ **Gỡ bỏ:**
> "Apply the mandatory principle 'extend, not overwrite'… preserve existing valid structure… unless the user explicitly requests replacement; add, refine, or qualify content by extending… rather than overwriting it."

### 2.2 Đoạn thay vào (đề xuất nguyên văn)
✅ **Quy tắc "Rebuild + Carry-Forward":**
> **Rebuild-with-carry-forward (thay cho 'extend, not overwrite'):** Với phần nội dung **chưa xuất bản / đang dò** (hệ tiên đề, mapping nội bộ), cho phép **viết đè sạch / suy lại từ đầu** — KHÔNG bắt buộc bảo tồn cấu trúc cũ. Điều kiện bắt buộc: **trước khi xóa/đè, khai báo một "Carry-Forward Set"** — danh sách tường minh các tài sản (claim, định nghĩa, điều kiện phản chứng, la bàn phương pháp) được phép mang sang. Mọi mục trong set là *ứng viên phải tái-kiểm bằng cổng RCA*, không tự động giữ. Mục KHÔNG nằm trong set → mặc định bị bỏ (thành reference-only). Với phần **đã xuất bản / có người ngoài phụ thuộc**, vẫn ưu tiên extend; chỉ overwrite khi người dùng yêu cầu rõ.

**Lý do giữ vế "đã xuất bản vẫn extend":** không vứt luôn lưới an toàn cho nội dung mạnh (điều kiện phản chứng, la bàn Phật giáo) — đúng cảnh báo Bảo-tồn của RCA.

### 2.3 Cập nhật mục liên quan
- `dictionary_rule.md §7` ("Điều KHÔNG đụng") → đổi tên thành "Carry-Forward Set mặc định" (cùng vai trò mới).
- `dictionary_rule.md §9` (bảng tên canonical) → hạ trạng thái từ "nguồn chân lý duy nhất" → "ứng viên carry-forward, chờ re-derive xác nhận".

---

## 3. P1 — KHAI BÁO CARRY-FORWARD SET

> Đây là tài sản *ứng viên* mang sang P2. Mỗi mục phải **sống sót re-derivation** (tái-kiểm ≥4/5) mới được giữ. Ngoại lệ: nhóm **PHƯƠNG PHÁP** (quy tắc chất lượng, không phải nội dung tiên đề) — giữ nguyên không cần re-derive.

### 3.1 PHƯƠNG PHÁP — giữ nguyên (không phải nội dung tiên đề)
| Tài sản | Nguồn | Vì sao giữ vô điều kiện |
|---|---|---|
| Cổng RCA (3-round × 5-Why × ≥4/5) | CLAUDE.md | Là *công cụ* re-derive, không phải đầu ra |
| `dictionary §1–§6` (chống tuyệt đối, ẩn dụ≠sự thật, minh họa≠chứng minh, công thức giả→sơ đồ, bỏ tự-chấm-điểm, quy trình P1–P5) | dictionary_rule.md | Quy tắc viết chung, độc lập với tiên đề nào tồn tại |
| La bàn nhận thức luận Phật giáo (Upāya, Śūnyatā, Nhị đế, Tứ cú, Pramāṇa) | axiom_conflict.html, CHANGELOG | La bàn *phương pháp*, dùng để suy, không phải kết luận |

### 3.2 NỘI DUNG — ứng viên, phải re-test trong P2
| Tài sản | Trạng thái | Điều kiện sống sót |
|---|---|---|
| **Câu hỏi gốc** ("vì sao một số hệ thống bản sắc tập thể sống sót đồng hóa, số khác không?") | hạt giống sinh ra cả hệ | Giữ — đây là *điểm xuất phát*, không cần chứng minh |
| Điều kiện phản chứng (falsification) | ứng viên mạnh | Re-derive phải đẻ ra điều kiện phản chứng *của riêng nó* |
| Hai tầng IV: essence (Orthogonal) vs manifestation (Vertical) | ứng viên (RCA cũ 5/5) | Chỉ giữ NẾU "thời gian" tái xuất hiện như tiên đề độc lập |
| Cơ chế tự phê bình / reflexive (VIII cũ) | ứng viên | Chỉ giữ nếu re-derive cần một tầng meta |
| "Hấp thụ có định hướng" (directed absorption) | ứng viên — từng được coi là đóng góp novel | Re-test: có phải tiên đề, hệ quả, hay chỉ minh họa? |
| Prior-art catalog (Whitehead, Heidegger, Gadamer, Ashby, Phan Ngọc, Lévi-Strauss, Anattā) | tài sản nghiên cứu | Gắn vào tiên đề mới tương ứng ở P3 |
| Nghề đặt tên thuần Việt (phương pháp) | giữ *kỹ thuật*, không giữ *tên cụ thể* | Tên mới phát sinh từ tiên đề mới |

### 3.3 KHÔNG carry-forward (bỏ → reference-only)
- Tập 7/8 tiên đề và **số La Mã I–VIII** như định danh ràng buộc.
- Nhãn "4 Core + 3 Derived" (artifact của migration).
- `dictionary §9` như bảng *ràng buộc* (chỉ còn là ứng viên).
- Toàn bộ migration v2.

---

## 4. P2 — RE-DERIVE HỆ TIÊN ĐỀ (lõi · sản phẩm = `axiom_spec.md`)

### 4.1 Tiêu chí một tiên đề (gate, dùng nguyên bộ cũ vì là phương pháp)
Một phát biểu là **tiên đề** chỉ khi đạt cả 5: **Độc lập** (không suy được từ tiên đề khác) · **Nhất quán** · **Phủ đầy** (góp phần trả lời câu hỏi gốc) · **Tối giản** · **Ontological** (nói về *cái gì tồn tại*, không phải mẹo thực hành). Không đạt "Độc lập" → là **Mệnh Đề Dẫn Xuất**, không phải tiên đề.

### 4.2 Quy trình suy (mỗi ứng viên qua cổng RCA)
```
1. Xuất phát: CÂU HỎI GỐC (carry-forward 3.2)
2. Liệt kê các "điều kiện cần" để một hệ bản sắc sống sót
     → mỗi điều kiện = 1 candidate axiom
3. Với mỗi candidate, chạy INDEPENDENCE TEST:
     "Suy được từ các candidate khác không?"
       CÓ  → hạ xuống Derived Proposition (ghi đường dẫn xuất)
       KHÔNG → giữ làm Core Axiom
4. Chấm 5 tiêu chí (≥4/5) cho từng Core Axiom
5. Kiểm TỐI GIẢN toàn cục: bỏ thử từng axiom — hệ còn trả lời được câu hỏi gốc?
       còn → axiom đó dư → hạ/gộp
6. KẾT QUẢ: tập tối giản N Core Axioms + M Derived (N, M KHÔNG định trước)
```

### 4.3 Cảnh báo trung thực (RCA — tiêu chí Khả thi 3/5)
- **Không pre-commit kết quả.** Plan này KHÔNG được giả định đầu ra là 4+3. Nếu re-derivation tái tạo đúng 4+3 → đó là *xác nhận độc lập* (giá trị cao). Nếu ra khác (3, 5, 6…) → theo nó.
- **Rủi ro thiên kiến xác nhận (confirmation bias):** vì ta đã biết 4+3, dễ vô thức lái về đó. Giảm thiểu: chạy independence test *bằng văn bản*, ghi rõ từng bước suy, để người khác soi.
- **Định dạng `axiom_spec.md`:** mỗi axiom một block — `ID · Tên · Phát biểu · Loại (Core/Derived/Meta) · (nếu Derived) đường dẫn xuất · 5-tiêu-chí-score · điều kiện phản chứng · prior-art · notation (nếu có, kèm disclaimer §4)`.

---

## 5. P3 — FALSIFIABILITY + PRIOR-ART NGAY TỪ ĐẦU

Khác các đời trước (bolt-on sau), lần này **mỗi Core Axiom sinh ra đã kèm**:
- **Điều kiện phản chứng** cụ thể: "tiên đề này SAI nếu tồn tại [trường hợp X]".
- **Prior-art** (từ carry-forward 3.2) + một câu *phân biệt* (Mạch Rễ khác ở đâu — cụ thể, theo `dictionary §1`: nêu phạm vi đối chiếu, tránh "không ai/duy nhất").
- **Phân loại đóng góp**: Synthesis / Extension / Novel (gắn nhãn ngay, không claim "nguyên bản" trống).

---

## 6. P4 — REGENERATE DOCUMENTS (viết lại, không migrate)

- HTML được **viết lại từ `axiom_spec.md`** — không sửa tại chỗ bản cũ.
- File cũ chuyển `archives/` hoặc gắn banner "reference — superseded by spec YYYY-MM-DD".
- Thứ tự: `what.html` (định nghĩa hệ) trước → các file phụ thuộc (`upgrade`, `who`, `axiom_4`, `axiom_conflict`, `mach_re_homologous`, `index`) sau, mỗi cái render lại từ spec.
- **P2 đối xứng song ngữ** áp dụng khi viết.

---

## 7. P5 — CROSS-CHECK & CHỐT

- [ ] Quét đa trang: mọi file nói về tiên đề khớp `axiom_spec.md` (single source).
- [ ] Không còn bảng "✅ Độc lập" cho mục thực ra là Derived.
- [ ] `dictionary §9` viết lại từ tập tên mới (nếu tên đổi).
- [ ] Ghi `CHANGELOG.md`: đợt REBUILD + bảng điểm RCA + tập tiên đề trước/sau (P5).

---

## 8. RISK REGISTER

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Mất nội dung mạnh do "làm lại từ đầu" | 🔴 CAO | **Carry-Forward Set (P1)** — lưới an toàn khai báo trước |
| Confirmation bias → ép về 4+3 | 🟡 TB | Independence test bằng văn bản, ghi từng bước (P2.3) |
| Spec & HTML lại phân kỳ | 🟡 TB | Spec-first; HTML chỉ render; quét P5 |
| Re-derive ra hệ khác → vỡ liên kết chéo nhiều file | 🟡 TB | P4 viết lại từ spec, không chắp vá; archive bản cũ |
| Bỏ luôn quy tắc bảo tồn cho bản đã xuất bản | 🟢 THẤP | P0 giữ vế "đã xuất bản vẫn extend" |
| Re-derivation tốn công lớn, dở dang | 🟡 TB | Phase hóa; P2 ra spec hoàn chỉnh trước khi đụng HTML |

---

## 9. THỨ TỰ THỰC THI (bất biến)

```
P0 (governance) → P1 (carry-forward set) → P2 (re-derive → axiom_spec.md)
   → P3 (falsifiability + prior-art) → P4 (regenerate HTML) → P5 (cross-check + CHANGELOG)
```

**Quy tắc quy trình giữ nguyên (`dictionary §6`):** P1 quét đa trang · P2 song ngữ · P3 dedupe · P4 không đụng `raw/` · P5 ghi CHANGELOG.

---

## 10. ĐIỂM DỪNG ĐỂ XÁC NHẬN

Tiến độ: **P0 + P1 đã thực thi** (2026-06-06). Điểm dừng còn lại:
1. ~~**P0** — sửa CLAUDE.md~~ ✅ XONG — [CLAUDE.md:126](../CLAUDE.md#L126).
2. ~~**P1** — Carry-Forward Set~~ ✅ XONG — `dictionary §7` (backbone 3 hệ A/B/C) + `§9` hạ trạng thái + CHANGELOG.
3. ~~**P2** — re-derive `axiom_spec.md`~~ ✅ XONG — 3 quyết định §5 đã giải bằng RCA.
4. **P4 ◐ đang làm** — **mẫu `axioms.html` đã render** (đánh số La Mã đếm lại theo tầng I–IV/V–VII/VIII; tên thuần Việt giữ). **DỪNG chờ bạn duyệt mẫu.** Sau khi duyệt:
   - Nhân rộng: cập nhật `what.html` (axiom section), `index.html` (nav), `who.html`, `upgrade.html`, `mach_re_homologous.html` theo số mới + link `axioms.html`.
   - **Archive (chính sách người dùng):** `axiom_4.html`, `axiom_8.html` (nếu publish), và axiom section cũ → `archives/` + banner "superseded by axioms.html / axiom_spec.md". `axiom_conflict.html` giữ (Module VIII còn dùng), chỉ cập nhật số.
   - Chưa archive gì ở bước mẫu (mẫu thuần additive, đảo ngược được).
5. **P4 nhân rộng — RCA chặn find/replace hàng loạt (2.0/5).** ~150 ref La Mã bị remap nghĩa → phải **regenerate từng trang từ spec + archive**, KHÔNG mass-replace. Đã wire `axioms.html` vào `index.html` nav + banner canonical ở `what.html` (additive). Còn lại 7 file regenerate page-by-page (queue: `what` full → `upgrade` → `mach_re_homologous` → `axiom_4` → `who`/`how`/`when`/`why`; `axiom_conflict` giữ, chỉ đổi số).
6. **`what.html` ◐ — đã gỡ mâu thuẫn (bounded):** bảng kiểm tra III/VI/VII → ⚠️ dẫn xuất; kết luận §3.6 "giả thuyết" → "đã giải" + trỏ `axioms.html`. 7 card vẫn số cũ dưới banner legacy (full renumber/reorder hoãn — single-source ưu tiên `axioms.html`, tránh trùng lặp). Trang nội bộ nhất quán, không mâu thuẫn ngầm.
7. **Banner canonical ✅ (additive, gate 4.2–4.8):** đã thêm vào `upgrade`, `mach_re_homologous` (IV→III), `axiom_conflict` (VIII giữ số), `axiom_4` (IV→III), `how` (generic — trang dùng sơ đồ 3-Core cục bộ). `who` (1 ref thoáng) + `when`/`why` (không nhắc số) bỏ qua. **Toàn site giờ trỏ về canonical, không mâu thuẫn ngầm.**
8. **Deep-renumber từng trang = GATE REJECT (3.0/5).** Ngay cả trang đơn-chủ-đề `axiom_4` cũng cascade ngược ra cross-file (tên file `axiom_4` vs nội dung "III", text link vào "Tiên Đề IV", cross-ref line 396 "III"=Phân Tán=V). Chỉ nên làm như một **batch phối hợp toàn site** (đổi tên file + mọi text link + mọi nội dung) hoặc KHÔNG làm (banner đã đủ coherence). **→ Rollout dừng ở trạng thái coherent. P4 coi như hoàn tất ở mức single-source + canonical pointer.**

---

*Plan REBUILD này thay thế tinh thần `mach-re-axiom-revision-plan.md` (v1) và `…-v2.md`. Re-derivation chốt hướng 2026-06-06.*

> **Metadata cho LLM:**
> - Loại: REBUILD (clean-slate re-derivation), KHÔNG pre-commit tập tiên đề
> - Thay thế: hai plan axiom-revision
> - Governance mới: "rebuild + carry-forward set" (thay "extend, not overwrite")
> - Single source tương lai: `axiom_spec.md` (sản phẩm P2)
> - Cổng: 3-round RCA × 5-Why × ≥4/5
> - Trình tự bất biến: P0 → P1 → P2 → P3 → P4 → P5
