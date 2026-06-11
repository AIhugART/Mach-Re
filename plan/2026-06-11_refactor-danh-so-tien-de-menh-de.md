# Plan 2026-06-11 — Refactor đánh số hệ tiên đề theo cấu trúc `raw/axiom-chart.html`

> **Trạng thái:** APPROVED (người dùng xác nhận trước trong yêu cầu: "tạo plan và lưu lại, thực hiện refactor").
> **La bàn:** A — Phan Ngọc · B — Ashby/Weick · C — Buddhist Epistemology (nhận thức luận Phật giáo).
> **Cổng quyết định:** 3-round RCA × 5-Why × scoring threshold ≥ 4/5 (RULE ZERO, CLAUDE.md).
> **Quy tắc đánh số mới (người dùng chốt 2026-06-11, override Quyết định 2 cũ 2026-06-06):**
> 1. **Chỉ Tiên Đề** (đơn vị độc lập, không suy ra được — đúng định nghĩa "Axiom" trong `raw/axiom-chart.html`) **mới được đánh số La Mã** I, II, III…
> 2. **Cấp dưới tiên đề** (Mệnh Đề / Định lý — đơn vị suy ra được từ tiên đề) **đánh số La tinh** 1, 2, 3…
> 3. **Cấp dưới nữa** (hệ quả, bổ đề, cơ chế con) **không đánh số** như đơn vị phân cấp; ký hiệu cấu trúc (structural notation: `F(S,t)`, `O-1`, `C1-min`, `DSH-1`…) không phải số phân cấp nên giữ nguyên.

---

## 0. Định nghĩa vấn đề (RCA Step 1 — Define)

**Triệu chứng (symptom):** Tầng Dẫn Xuất mang số La Mã (`Mệnh Đề V, VI, VII` + chữ `F`); nhiều trang sống còn gọi sai tầng (`Tiên Đề V/VI/VII`); đơn vị phụ `UPGRADE I–IV` dùng La Mã dù không phải tiên đề.

**Nguyên nhân gốc (root cause, 1 câu):** Quyết định 2 (2026-06-06) chốt "số La Mã đếm liên tục xuyên tầng" *trước khi* kỷ luật phân tầng của `raw/axiom-chart.html` (đơn vị suy ra được → không phải tiên đề → không mang định danh tiên đề) được nâng thành quy tắc ràng buộc — nên **ký pháp (notation) tụt hậu so với phân loại (classification)**: spec đã hạ V/VI/VII/F thành "Mệnh Đề Dẫn Xuất" nhưng số của chúng vẫn ở thanh ghi thị giác (visual register) của tiên đề.

---

## 1. Cổng quyết định — 6 quyết định, mỗi quyết định 3-round × 5-Why × scoring

### D1 — Mệnh Đề Dẫn Xuất: La Mã V/VI/VII + chữ F → La tinh **1/2/3/4** — **FIX (4.8/5)**

- **Round 1 (Symptom):** "Mệnh Đề V" và "Tiên Đề IV" cùng dùng La Mã → người đọc suy ra mệnh đề có địa vị tiên đề.
- **Round 2 (Mechanism):** Mạch Rễ tự tuyên bố kỷ luật axiom-chart ("tiên đề suy ra được phải bị hạ cấp thành Định lý" — nguyên tắc cốt lõi của `raw/axiom-chart.html`). Một framework mời gọi soi xét nghiêm ngặt bị tổn thương nặng hơn bởi chính lỗi nó cảnh báo: ký pháp đồng phục La Mã chính là hình ảnh của "tiên đề dư thừa" chưa hạ cấp xong.
- **Round 3 (Root):** Vi phạm chuẩn nội tại — Tiên Đề VIII (Tự Nhìn Thấy Mình) đòi framework áp thước đo của mình lên chính nó; phân loại đã sửa (P2: "Mệnh Đề Dẫn Xuất") nhưng ký pháp chưa theo → traceability nội bộ gãy.
- **5-Why:** Vì sao V/VI/VII mang La Mã? → Quyết định 2 chốt La Mã liên tục. → Vì sao chốt vậy? → Lúc đó tầng do *nhãn* chỉ, không do dải số. → Vì sao chưa đủ? → Nhãn bị rơi rụng khi trích dẫn ngắn ("Tiên Đề V" xuất hiện ở 5 trang sống). → Vì sao rơi rụng? → Số La Mã tự nó phát tín hiệu "tiên đề". → **Root: ký pháp không tự mang phân loại** (1 câu — đạt).
- **La bàn:** A — bản sắc là *kiểu quan hệ* bền, không phải nhãn; đổi số giữ nguyên tên thuần Việt + nội dung = pattern bất biến được bảo toàn. B — Ashby: ký pháp phân tầng làm giảm variety của cách đọc sai; Weick: sensemaking của người đọc mới đi đúng tầng ngay từ ký hiệu. C — Apoha: số "1/2/3" loại trừ đúng cái cần loại trừ (không-phải-tiên-đề); Nhị đế: định danh là quy ước (saṃvṛti), được phép đổi khi phương tiện (upāya) tốt hơn.
- **Scoring:** Correct 5 · Deep 5 · Feasible 5 · Conflict-risk 4 (archive giữ định danh cũ → cần alias tại định nghĩa) · Preservation 5 → **4.8 ≥ 4 → FIX**.
- **Mapping chốt:** `Mệnh Đề V → Mệnh Đề 1 (Phân Tán)` · `VI → 2 (Chuyển Hóa Nhiễu Loạn)` · `VII → 3 (Nổi Lên Có Hướng)` · `F → 4 (Điều Kiện Đứt Gãy — ký hiệu cấu trúc F giữ nguyên trong F(S,t), F-A/B/C)`. EN: `Derived Proposition 1–4`.

### D2 — Tiên Đề VIII, IX: **giữ số, không dồn thành V/VI** — phương án dồn số bị **BÁC (1.8/5)**; phương án giữ + chú thích quy ước **FIX (4.8/5)**

- **Round 1:** Sau khi hạ tầng, dãy La Mã của tiên đề có khoảng trống: I, II, III, IV, VIII, IX.
- **Round 2:** Dồn VIII→V sẽ tái sử dụng số "V" — số mà toàn bộ corpus đã xuất bản (papers, screenplay framework Tier-1, CHANGELOG, review) gắn với "Phân Tán/Giữ Mà Không Gom" → mơ hồ thảm họa giữa tài liệu cũ–mới; "Tiên Đề VIII" là định danh đã xuất bản, được CLAUDE.md và mọi node phụ thuộc.
- **Round 3:** Quy tắc người dùng ràng buộc *tầng nào dùng kiểu số nào*, không ràng buộc *tính liên tục của dãy*. Khoảng trống V–VII là **dấu vết trung thực của sự tự-sửa** (VIII áp lên chính hệ) — đồng dạng với lịch sử "tiên đề thứ 5 của Euclid" giữ tên dù hệ được tái cấu trúc.
- **5-Why (phương án dồn):** đổi để được gì? → dãy đẹp. → đẹp phục vụ chuẩn nội tại nào? → không chuẩn nào — thuần thẩm mỹ. → chi phí? → đứt mọi tham chiếu đã xuất bản. → **Root: không có defect thật để sửa.**
- **La bàn:** A — Phan Ngọc: bản sắc nhận diện được *qua thời gian* đòi hỏi định danh ổn định với hệ phụ thuộc bên ngoài. B — Weick (retrospect): khoảng trống kể đúng câu chuyện tổ chức của hệ; Ashby: dồn số làm bùng nổ variety của cách đọc nhầm. C — saṃvṛti: cộng đồng đã dùng quy ước "VIII"; đổi quy ước đang sống là phản-upāya.
- **Scoring (dồn số):** Correct 2 · Deep 2 · Feasible 2 · Conflict-risk 1 · Preservation 2 → **1.8 < 4 → KHÔNG dồn**.
- **Scoring (giữ + thêm chú thích "số tiên đề là định danh lịch sử, không tái sử dụng số đã hạ tầng"):** 5·4·5·5·5 → **4.8 → FIX** (thêm chú thích vào `axiom_spec.md` header + `dictionary_rule.md §9`).

### D3 — Sai tầng "Tiên Đề V/VI/VII" trong file sống → "Mệnh Đề 1/2/3" — **FIX (5.0/5)**

- **Round 1:** `luu_tru.html`, `ubuntu.html`, `yoruba.html`, `relational_and_distributed_philosophy.html`, thang tiên đề trong `axiom_9.html`, `upgrade.html` còn gọi "Tiên Đề V/VI/VII".
- **Round 2:** Đây không chỉ là lỗi kiểu số — là **lỗi phạm trù** (category error): gán địa vị tiên đề cho đơn vị suy ra được, đúng lỗi mà nguyên tắc cốt lõi của axiom-chart cấm ("redundant axiom").
- **Round 3:** Các trang viết trước P2 (hạ tầng 2026-06-06) và chưa được đối soát lại với SSOT — root: **thiếu bước reconciliation sau khi SSOT đổi**, vi phạm quy tắc "Mọi file HTML/MD render từ axiom_spec.md".
- **Scoring:** 5·5·5·5·5 → **5.0 → FIX**.

### D4 — `UPGRADE I/II/III/IV` (La Mã cho đơn vị không phải tiên đề) → `Upgrade 1/2/3/4` — **FIX (4.6/5)**

- **Round 1:** `upgrade.html` đánh số La Mã cho 4 bản mở rộng; `axiom_conflict.html` tham chiếu "Upgrade II".
- **Round 2:** Vi phạm trực tiếp quy tắc 1 ("chỉ tiên đề mới được La Mã") — và "UPGRADE III — Tiên Đề V" tạo chuỗi nhầm phạm trù kép.
- **Round 3:** Root: cùng nguyên nhân gốc §0 — ký pháp La Mã được dùng như trang trí thứ bậc, không như định danh tầng.
- **Scoring:** Correct 5 · Deep 4 · Feasible 5 · Conflict-risk 4 · Preservation 5 → **4.6 → FIX**. Upgrade là đơn vị *dưới tiên đề* → La tinh 1–4 (đúng quy tắc 2).

### D5 — Dải "I–VIII" (nghĩa: hệ đơn đầy đủ) → "I–IV + VIII" trong file sống — **FIX (4.4/5)**

- **Round 1:** "hai hệ I–VIII gặp nhau", "mỗi hệ đã vận hành Tiên Đề I–VIII" (axiom_9, upgrade, index, spec §IX).
- **Round 2:** Sau refactor, V–VII không còn là số tiên đề → dải "I–VIII" chứa 3 số không trỏ vào tiên đề nào → dải không nhất quán với chính hệ.
- **Round 3:** Root: dải số được dùng thay cho khái niệm "hệ đơn vận hành đầy đủ". Vì Mệnh Đề 1–3 **được kéo theo logic** từ I–IV (đúng định nghĩa derived), "I–IV + VIII" tương đương ngữ nghĩa và tự nhất quán.
- **Scoring:** Correct 4 · Deep 4 · Feasible 5 · Conflict-risk 4 · Preservation 5 → **4.4 → FIX** (chỉ file sống; công thức formal trong spec §IX sửa kèm chú thích "các Mệnh Đề 1–4 kéo theo từ I–IV").

### D6 — Ký hiệu cấu trúc cấp dưới (`F(S,t)`, `F-A/B/C`, `O-1..O-4`, `G1–G3`, `C1-full/min/zero`, `DSH-1..3`, `[DEF-1]`, "hệ quả 1–5 của VIII", "Module 5") — **GIỮ NGUYÊN (đề xuất xóa bị bác 1.8/5)**

- **Round 1:** Quy tắc 3 nói "cấp dưới nữa không đánh số" — các nhãn trên trông như đánh số.
- **Round 2:** Chúng là **ký hiệu cấu trúc / định danh vận hành** (structural notation), không phải số thứ bậc phân cấp của sơ đồ axiom-chart; các điều kiện phản chứng (falsification conditions) trỏ thẳng vào chúng (vd: O-1a, DSH-F1, F-A) — xóa là phá traceability, vi phạm Rule #7.
- **Round 3:** Phạm vi đúng của quy tắc 3 là **đơn vị phân cấp của hệ** (Bổ đề/Hệ quả/cơ chế con không mang định danh thứ bậc kiểu "Hệ quả III"); riêng "hệ quả 1–5 của Tiên Đề VIII" và "Module 5" nằm ở **cấp ngay dưới tiên đề** (= cấp Mệnh Đề/Định lý) → La tinh là đúng quy tắc 2, không phải vi phạm quy tắc 3.
- **Scoring (xóa):** Correct 2 · Deep 2 · Feasible 2 · Conflict-risk 1 · Preservation 2 → **1.8 < 4 → GIỮ**.

---

## 2. Phạm vi (Scope table)

**Tầng SỐNG — refactor:**

| File | Việc |
|---|---|
| `axiom_spec.md` (SSOT) | Header sơ đồ đánh số; §0.1.1 dải "III–VII"; §1 cột kết luận; §2 heading tầng Dẫn Xuất + 4 heading Mệnh Đề + cross-refs nội bộ; §3 sơ đồ; §5 thêm **Quyết định 4** (override Quyết định 2, không viết lại lịch sử); §5.1 bảng map thêm cột mới; §8 YAML keys; §9 các ref "Mệnh đề F" |
| `plan/dictionary_rule.md` §9 | Tách bảng: Tiên Đề (I–IV, VIII, IX — La Mã) / Mệnh Đề Dẫn Xuất (1–4 — La tinh); chú thích không-tái-sử-dụng-số |
| `CLAUDE.md` | Bảng "Tên thuần Việt các Tiên Đề" cập nhật theo cấu trúc mới |
| `axioms.html`, `axiom_derived.html`, `what.html`, `how.html`, `index.html`, `who.html`, `when.html`, `axiom_1.html`, `axiom_9.html`, `axiom_ix_spec.md` | V/VI/VII/F → 1/2/3/4; dải I–VIII → I–IV + VIII |
| `luu_tru.html`, `ubuntu.html`, `yoruba.html`, `relational_and_distributed_philosophy.html` | Sửa lỗi phạm trù "Tiên Đề V/VI/VII" → "Mệnh Đề 1/2/3" |
| `upgrade.html`, `axiom_conflict.html` | UPGRADE I–IV → Upgrade 1–4; "Tiên Đề V" → "Mệnh Đề 1"; dải I–VIII |
| `CHANGELOG.md` | Entry refactor (root tier) |

**Tầng LƯU TRỮ — KHÔNG sửa (lịch sử không viết lại):** `CHANGELOG*` entries cũ, `plan/*` có ngày, `review/*`, `raw/*`, `scratch/*`, `LICENSE`, `papers/*` (đã xuất bản — Rule #12 non-retroactive; định danh cũ trong papers được bảo vệ bởi bảng map §5.1), `publish/movie_script/*` (chỉ tham chiếu VIII — không đổi).

**Anchor/ID HTML (`#F`, `id="..."`) giữ nguyên** — đổi text hiển thị, không đổi id để không gãy link.

## 3. Verify (RCA Step 5)

1. Grep file sống: không còn `Mệnh Đề V|VI|VII|F`, `Tiên Đề V|VI|VII`, `UPGRADE [IVX]` (trừ alias "(trước: …)" tại định nghĩa và bảng map lịch sử).
2. Tiên Đề chỉ còn La Mã: I, II, III, IV, VIII, IX; Mệnh Đề chỉ còn 1–4.
3. Đối chiếu ngược về `raw/axiom-chart.html`: tầng Tiên đề / Định lý-Mệnh đề / dưới-không-số khớp.
4. Ghi `CHANGELOG.md` (root tier — đúng routing "phải và chỉ được").

**Nguồn Trích Dẫn:** Tài liệu này không có trích dẫn nghiên cứu từ bên ngoài (la bàn A/B/C tham chiếu qua `axiom_spec.md` §Nguồn Trích Dẫn [1]–[5]).
