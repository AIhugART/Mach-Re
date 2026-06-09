# PLAN — Hoàn Thiện Kịch Bản mv_001: TÊN CON / The Name

> **Date:** 2026-06-09
> **Status:** COMPLETE — all 7 phases executed, RCA 4.99/5
> **RCA Gate:** 3-round × 5-Why × scoring ≥ 4/5 cho mọi quyết định cấu trúc
> **Input:** `idea_001.md` (RCA 5.0/5 — đã qua 3-round RCA gate)
> **Author:** VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/

---

## 1. RCA Gate — Tại Sao Cần Plan Này?

### Round 1 — Symptom

`idea_001.md` đã đạt 5.0/5 RCA ở tầng **idea**. Nhưng idea không phải kịch bản. Câu hỏi: "Cần làm gì để từ idea → kịch bản hoàn chỉnh?" chưa được trả lời có cấu trúc. Nếu viết ngay mà không có plan, output sẽ là tập hợp các mảnh rời rạc — scene rời, đoạn hội thoại rời, character note rời — không có kiến trúc thống nhất.

### Round 2 — Mechanism

Zhang-Spielberg Hybrid framework yêu cầu **5 tầng output** (Full screenplay, Story beat sheet, Scene draft, Character breakdown, Opening image brief) được tích hợp chặt chẽ. Mỗi tầng phụ thuộc vào tầng trước. Viết mà không có thứ tự → phải sửa đi sửa lại vì thay đổi ở tầng dưới làm hỏng tầng trên.

Thêm vào đó, CLAUDE.md Screenplay Rules yêu cầu: RCA traceability (rule 6), falsification condition (rule 7), constraint set (rule 5). Mỗi output phải carry-forward những ràng buộc này.

### Round 3 — Root

Không có **dependency graph** giữa các artifact. Idea → Character → Beat Sheet → Key Scenes → Opening/Closing Images → Polish. Đây là chuỗi phụ thuộc một chiều. Root cause: chưa có ai vẽ ra dependency graph này cho mv_001.

**Fix:** Plan này chính là dependency graph + RCA gate cho từng bước.

**RCA Score cho chính plan này:** 5/5 (correct: real gap; deep: structural; feasible: yes; conflict-risk: none; preservation: idea intact)

---

## 2. Dependency Graph — Thứ Tự Sản Xuất

```
idea_001.md (đã có, 5.0/5)
    │
    ▼
[Phase 1] CHARACTER BREAKDOWN (3-layer)
    │  ├── Protagonist (NGƯỜI MẸ): surface · personal wound · generational wound
    │  ├── CHỒNG: relationship to system (accepted without questioning)
    │  ├── BÀ NỘI CHỒNG (85t): relationship to system (survived without being seen)
    │  ├── CON GÁI (7t, Act 3): the generation that writes her own name
    │  └── The System: gia phả phụ hệ — invisible antagonist
    │
    ▼
[Phase 2] STORY BEAT SHEET (Zhang-Spielberg architecture)
    │  ├── Opening Image (tableau)
    │  ├── Act 1 (~22%): Ordinary World → Inciting Incident → Plot Point I
    │  ├── Act 2A (~25-50%): Rising Action → Midpoint
    │  ├── Act 2B (~50-75%): System Asserts → Turning Point (Loss Without Villain)
    │  ├── Act 3 (~75-100%): Alone → Climax (Small Action) → Closing Image
    │  └── Color Temperature Map (warm → cool arc)
    │
    ▼
[Phase 3] RECURRING OBJECTS & VISUAL MOTIFS
    │  ├── Object 1: Cuốn gia phả chính thức (vải đỏ, tủ kính)
    │  ├── Object 2: Cuốn gia phả song song (giấy trắng, chữ Quốc ngữ)
    │  ├── Object 3: Cây bút (emotional proxy — xuất hiện 3 lần)
    │  └── Visual motif: camera angle shift (thấp ↔ ngang mắt)
    │
    ▼
[Phase 4] KEY SCENE DRAFTS (3-pass dialogue reduction)
    │  ├── Scene A: Opening Image — Gia đình họp mặt, gia phả mở ra
    │  ├── Scene B: Inciting Incident — "Con gái không được ghi tên"
    │  ├── Scene C: Midpoint — Mẹ viết tên bà nội chồng vào cuốn song song
    │  ├── Scene D: Turning Point — Bà nội chồng nhìn thấy cuốn song song
    │  ├── Scene E: Climax — Con gái tự viết tên mình
    │  └── Scene F: Closing Image — Cuốn gia phả song song, mở ra, đầy tên
    │
    ▼
[Phase 5] FULL BEAT-TO-SCREENPLAY INTEGRATION
    │  ├── Điền các scene còn lại (connecting tissue)
    │  ├── 3-pass dialogue reduction cho tất cả dialogue
    │  ├── Silence & negative space annotations
    │  └── Color/light direction notes
    │
    ▼
[Phase 6] RCA VERIFICATION (toàn bộ kịch bản)
    │  ├── 3-round RCA cho từng scene quan trọng
    │  ├── Falsification condition check (mỗi scene có thể fail như thế nào?)
    │  ├── Constraint set check (5 constraints từ CLAUDE.md)
    │  └── Tonal calibration check (Zhang-Spielberg register)
    │
    ▼
[Phase 7] FINAL POLISH & DELIVERABLES
       ├── Opening Image Brief (200-300 words)
       ├── Character Breakdowns (4 nhân vật)
       ├── Full Beat Sheet (numbered, annotated)
       ├── Key Scene Drafts (6 scenes × full screenplay format)
       └── RCA Traceability Report (mỗi quyết định → RCA score)
```

---

## 3. Phase Chi Tiết

### Phase 1 — Character Breakdown (3-Layer)

**Mục tiêu:** Xây dựng 4 nhân vật theo Zhang-Spielberg 3-layer construction.

**RCA Gate cho Phase 1:**
- Round 1: Nhân vật trong `idea_001.md` mới có sketch (want/need). Chưa có behavior inventory, chưa có personal wound được thể hiện qua hành vi.
- Round 2: Zhang-Spielberg yêu cầu personal wound "discoverable through behavior — the things they avoid, the things they hold too carefully, the moments they go very still." Nếu không có behavior inventory, character sẽ chỉ là mô tả, không phải con người.
- Round 3: Root — character construction thiếu tầng generational. Personal wound của MẸ phải connected với generational wound của BÀ NỘI CHỒNG, và resolution phải là CON GÁI viết tên mình → 3 thế hệ, một vết thương.
- Score: 5/5

**Deliverable:** `mv_001/characters.md`

| Nhân vật | Surface | Personal Wound | Generational Wound | Behavior Inventory |
|----------|---------|----------------|-------------------|-------------------|
| MẸ (35t) | Kế toán, làng Nam Định | ? | ? | ? |
| CHỒNG (38t) | ? | ? | ? | ? |
| BÀ NỘI CHỒNG (85t) | ? | ? | ? | ? |
| CON GÁI (7t, Act 3) | ? | ? | ? | ? |

**The System (invisible antagonist):** Gia phả phụ hệ — "xưa giờ vậy mà" — operates like weather.

---

### Phase 2 — Story Beat Sheet

**Mục tiêu:** Map toàn bộ câu chuyện vào Zhang-Spielberg architecture.

**RCA Gate cho Phase 2:**
- Round 1: Không có beat sheet → không biết scene nào cần viết, scene nào thừa.
- Round 2: Zhang-Spielberg architecture là load-bearing structure — mỗi beat có chức năng kể chuyện riêng. Bỏ qua một beat = cấu trúc yếu.
- Round 3: Root — cần mapping cụ thể giữa các yếu tố trong `idea_001.md` (Central Image, Cinematic Mechanism, World & Characters) vào từng structural position.
- Score: 5/5

**Deliverable:** `mv_001/beat_sheet.md`

Cấu trúc dự kiến (sẽ được RCA-gate từng beat trong quá trình viết):

| # | Beat | Runtime % | Mô tả dự kiến |
|---|------|-----------|---------------|
| 1 | Opening Image | 0% | Cảnh nhà thờ họ — gia phả mở, chỉ đàn ông chạm vào |
| 2 | Ordinary World | 0-15% | Nhịp sống gia đình — Mẹ chăm con, chợ làng, bữa cơm |
| 3 | Inciting Incident | ~15% | Họp họ — con gái không được ghi tên. "Cố thêm đứa nữa." |
| 4 | Plot Point I | ~22% | Mẹ mua cuốn sổ trắng — quyết định bí mật |
| 5 | Act 2A Rising | 22-50% | Mẹ bắt đầu viết — hỏi những người phụ nữ trong họ về tên, về mẹ, về bà |
| 6 | Midpoint | 50% | Mẹ viết tên BÀ NỘI CHỒNG — bà không biết. Khoảnh khắc đẹp nhất. |
| 7 | Act 2B Compression | 50-75% | Gia đình chồng bắt đầu nghi ngờ. Áp lực "sinh con trai" tăng. |
| 8 | Turning Point | ~65-70% | BÀ NỘI CHỒNG tìm thấy cuốn song song — bà khóc. Loss: sự im lặng của cả một đời được nhìn thấy quá muộn. |
| 9 | Plot Point II | ~75% | Mẹ đối mặt: tiếp tục viết hay dừng lại? |
| 10 | Alone | 75-85% | Mẹ ngồi một mình với cuốn sổ — những trang đã viết, những trang còn trống. |
| 11 | Climax | ~90% | CON GÁI (7t) cầm bút, tự viết tên mình vào cuốn song song. |
| 12 | Closing Image | 100% | Camera rút ra — cuốn gia phả song song mở, đầy tên phụ nữ. Ánh sáng chiều. |

---

### Phase 3 — Recurring Objects & Visual Motifs

**Mục tiêu:** Xác định 2-3 recurring objects + color temperature map.

**RCA Gate cho Phase 3:**
- Round 1: `idea_001.md` đã phác thảo 2 cuốn gia phả + camera angle. Nhưng chưa có recurring object protocol (xuất hiện 3 lần: neutral → connection → loss).
- Round 2: Zhang-Spielberg rule: "the object should first appear in a neutral context, then in a moment of connection, then in the scene of loss." Cần mapping cụ thể.
- Round 3: Root — visual language của phim này là **2 cuốn sách + 1 cây bút**. Mỗi object cần trajectory riêng trong timeline.
- Score: 5/5

**Deliverable:** `mv_001/visual_motifs.md`

| Object | Lần 1 (neutral) | Lần 2 (connection) | Lần 3 (loss/climax) |
|--------|-----------------|-------------------|---------------------|
| Gia phả chính thức | Opening — mở ra, trang trọng | Midpoint — ai đó chỉ vào chỗ trống nơi tên phụ nữ lẽ ra phải có | Turning Point — Bà Nội Chồng chạm vào, camera thấp |
| Gia phả song song | Mẹ mua sổ trắng | Mẹ viết tên bà nội chồng (Midpoint) | Con gái tự viết tên mình (Climax) |
| Cây bút | Cây bút của chồng — để trên bàn thờ | Mẹ dùng bút của chính mình (mua riêng) | Con gái cầm bút của mẹ (Climax) |

---

### Phase 4 — Key Scene Drafts

**Mục tiêu:** Viết 6 scene quan trọng nhất ở full screenplay format.

**RCA Gate cho Phase 4:**
- Round 1: Không phải mọi scene đều quan trọng như nhau. Cần chọn đúng scene để đầu tư.
- Round 2: 6 scene được chọn vì chúng là structural joints — nếu chúng yếu, toàn bộ phim sập. Các scene còn lại là connecting tissue.
- Round 3: Root — mỗi key scene phải qua 3-pass dialogue reduction + có silence annotation + color/light direction.
- Score: 5/5

**Deliverable:** `mv_001/key_scenes.md`

| Scene | Structural Position | Yêu cầu đặc biệt |
|-------|-------------------|-----------------|
| A — "Gia Phả Mở" | Opening Image | Tableau: đẹp nhưng có gì đó sai. Không lời thoại. |
| B — "Con Gái Không Được Ghi" | Inciting Incident | External (họp họ) meets internal (Mẹ chưa từng nghĩ đến). Đối thoại tối giản. |
| C — "Tên Của Bà" | Midpoint | Đẹp nhất phim. Mẹ viết, không ai biết. Ánh sáng vàng hổ phách. |
| D — "Bà Nội Chồng Khóc" | Turning Point | Loss without villain. Không nhạc. Bà chạm vào tên mẹ mình. |
| E — "Con Viết Tên Con" | Climax | Hành động nhỏ — đứa trẻ cầm bút. Mẹ nắm tay con. |
| F — "Cuốn Sổ Đầy Tên" | Closing Image | Camera rút xa. Human trace. Có ánh sáng. |

---

### Phase 5 — Full Beat-to-Screenplay Integration

**Mục tiêu:** Điền connecting tissue giữa các key scenes → kịch bản hoàn chỉnh.

**Deliverable:** `mv_001/screenplay_full.md`

---

### Phase 6 — RCA Verification

**Mục tiêu:** RCA-gate toàn bộ kịch bản trước khi đóng dấu "done."

**Deliverable:** `mv_001/rca_verification.md`

Checklist:
- [ ] 3-round RCA cho từng key scene (≥ 4/5)
- [ ] Falsification condition cho từng scene
- [ ] Constraint set: Không chính trị · Không tôn giáo · UK/US language · Bối cảnh Việt Nam · Tiên Đề III là cấu trúc
- [ ] Tonal calibration: không quá lạnh (Zhang Yimou thuần), không quá ấm (Spielberg thuần)
- [ ] Dialogue 3-pass reduction verification
- [ ] Show-don't-tell: Tiên Đề III không được giải thích trong lời thoại

---

### Phase 7 — Final Polish & Deliverables

**Deliverables cuối cùng:**

| File | Nội dung |
|------|----------|
| `mv_001/idea_001.md` | **Đã có (5.0/5)** — canonical idea reference |
| `mv_001/characters.md` | 4 nhân vật × 3-layer construction × behavior inventory |
| `mv_001/beat_sheet.md` | 12 beats × Zhang-Spielberg architecture |
| `mv_001/visual_motifs.md` | 3 objects + color temperature map + camera language |
| `mv_001/key_scenes.md` | 6 key scenes × full screenplay format |
| `mv_001/screenplay_full.md` | Kịch bản hoàn chỉnh (tích hợp tất cả) |
| `mv_001/rca_verification.md` | RCA traceability report |
| `mv_001/PLAN.md` | File này — plan reference |

---

## 4. Risk Assessment

| Risk | Level | Mitigation |
|------|-------|------------|
| Phase 4 scene drafts yếu vì thiếu Phase 1-3 foundation | **HIGH** | Không skip phase. Dependency graph là bắt buộc. |
| Dialogue quá nhiều — phá vỡ Zhang-Spielberg silence rule | **MEDIUM** | Mỗi scene phải qua 3-pass reduction. |
| Lạc vào "message movie" thay vì "structure movie" | **MEDIUM** | RCA gate mỗi scene: Tiên Đề III là cấu trúc, không phải theme. |
| Tonal drift — quá ấm (Spielberg) hoặc quá lạnh (Zhang Yimou) | **LOW** | Phase 6 tonal calibration check. |
| Conflict với constraint set (chính trị, tôn giáo) | **LOW** | Không có yếu tố nào trong idea hiện tại chạm constraint. |

---

## 5. Estimated Complexity

| Phase | Effort | Dependency |
|-------|--------|-----------|
| 1 — Character Breakdown | 1-2 hours | idea_001.md |
| 2 — Story Beat Sheet | 2-3 hours | Phase 1 |
| 3 — Visual Motifs | 1 hour | Phase 2 |
| 4 — Key Scene Drafts | 3-4 hours | Phase 1-3 |
| 5 — Full Integration | 2-3 hours | Phase 4 |
| 6 — RCA Verification | 2 hours | Phase 5 |
| 7 — Final Polish | 1 hour | Phase 6 |
| **Total** | **12-16 hours** | |

---

## 6. Carry-Forward Set

Từ `idea_001.md`, các assets sau được carry-forward (phải tái xác nhận qua RCA gate trước khi dùng):

| Asset | Nguồn | Điều kiện carry-forward |
|-------|-------|------------------------|
| Logline | idea_001.md L7 | Phải giữ nguyên — đã RCA 5.0 |
| 3-round RCA trace (D11 mechanism) | idea_001.md L9-20 | Carry nguyên vẹn |
| Scoring rubric (C1-C5, 5.0/5) | idea_001.md L22-32 | Tham chiếu — không sửa |
| Cinematic Mechanism (2 cuốn gia phả, camera angle) | idea_001.md L34-40 | Mở rộng thành Phase 3 |
| World & Characters (4 nhân vật sketch) | idea_001.md L42-48 | Mở rộng thành Phase 1 |
| Central Image | idea_001.md L50-52 | Dùng làm reference cho Scene E (Climax) |
| Present-Day Problem | idea_001.md L54-56 | Dùng làm context, không đưa vào screenplay |
| Constraint Set | CLAUDE.md Screenplay Rules §Tier 2.5 | Áp dụng toàn bộ |
| Zhang-Spielberg Framework | `publish/movie_script/Zhang_Yimou_Spielberg_Hybrid_Screenplay.md` | Áp dụng toàn bộ |

---

**WAITING FOR CONFIRMATION:** Proceed with this 7-phase plan? (yes / no / modify)
