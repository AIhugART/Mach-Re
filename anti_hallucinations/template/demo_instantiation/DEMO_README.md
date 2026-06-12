Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- DEMO — AHP Template v1.0 (2026-06-12) — Domain-Agnostic Synthetic Example -->

# DEMO: AHP Template Instantiation — 2-System Synthetic Example

**Purpose:** Demonstrate how to instantiate the AHP template for a multi-system mapping project using a completely domain-agnostic, synthetic example. All data is fabricated — no real-world claims.

**Systems used:**
- **TFT = Traffic Flow Theory** (synthetic domain 1)
- **PNT = Packet Network Theory** (synthetic domain 2)

---

## Step 1: System Registration (`system_registry.md`)

| System ID | System Name | Short Name | SOT File Path | Namespace Prefix | Node Code Format | Edge Code Format | Status |
|-----------|------------|------------|---------------|------------------|-----------------|-----------------|--------|
| SYS-1 | Traffic Flow Theory | TFT | `systems/tft_nodes.md` | `N_TFT_` | `N_TFT_00001` | `ED_TFT_00001` | ACTIVE |
| SYS-2 | Packet Network Theory | PNT | `systems/pnt_nodes.md` | `N_PNT_` | `N_PNT_00001` | `ED_PNT_00001` | ACTIVE |

---

## Step 2: Node Definitions

### TFT Nodes

| Code | Name (EN) | Definition | SOT Reference | Pre-existing? |
|------|-----------|------------|---------------|---------------|
| `N_TFT_00001` | Flow Rate | Vehicles passing a point per unit time (veh/hr) | systems/tft_nodes.md §2 | Y |
| `N_TFT_00002` | Congestion | State where flow rate drops below free-flow threshold | systems/tft_nodes.md §3 | Y |
| `N_TFT_00003` | Traffic Light Phase | Timed signal controlling intersection right-of-way | systems/tft_nodes.md §5 | Y |

### PNT Nodes

| Code | Name (EN) | Definition | SOT Reference | Pre-existing? |
|------|-----------|------------|---------------|---------------|
| `N_PNT_00001` | Bandwidth | Data units passing a point per unit time (bps) | systems/pnt_nodes.md §1 | Y |
| `N_PNT_00002` | Queue | Buffer backlog caused by processing rate below arrival rate | systems/pnt_nodes.md §4 | Y |
| `N_PNT_00003` | Packet | Unit of data transmission with header + payload | systems/pnt_nodes.md §2 | Y |

---

## Step 3: Cross-System Mapping (`mapping_registry.md`)

### Mapping Links

| Map ID | Source Node | Target Node | mapping_type | justification | ground_system | AHP label | Status |
|--------|------------|-------------|-------------|---------------|---------------|-----------|--------|
| MAP_001 | `N_TFT_00001` | `N_PNT_00001` | **ANALOGY** | Both represent "throughput rate" — Flow Rate (veh/hr) and Bandwidth (bps) share the same mathematical structure (rate = quantity / time). But the physical substrates differ (vehicles vs. data units). | TFT | `[AH-LOW][ES-ANUMA]` | VERIFIED |
| MAP_002 | `N_TFT_00002` | `N_PNT_00002` | **STRUCTURAL** | Congestion and Queue share a formal correspondence: both are described by the same queuing-theory differential equation dQ/dt = λ − μ where λ is arrival rate and μ is service rate. The structure preserves relations: input rate → buffer state → output rate. | TFT | `[AH-LOW][ES-ANUMA]` | VERIFIED |

### NAC (No-Analogue Concept)

| NAC ID | Node | Home System | Why no analogue in PNT | Status |
|--------|------|-------------|------------------------|--------|
| NAC_001 | `N_TFT_00003` (Traffic Light Phase) | TFT | Traffic lights are a **temporal multiplexing** mechanism specific to physical intersection geometry. Packet networks use statistical multiplexing — no equivalent to a fixed-timing phase cycle. Mapping would be a category error (Vikalpa). | DOCUMENTED |

---

## Step 4: End-to-End Pipeline Walkthrough

### Claim under review: "Traffic Flow Theory and Packet Network Theory are structurally isomorphic."

### 4.1 Stakes Assessment → HIGH
- Affects framework classification → escalate to CRITICAL if published
- → Full pipeline (01→06) required

### 4.2 01 — Early Warning Scan

| Signal | Match? | Notes |
|--------|--------|-------|
| R1 (category error) | NO | Claim does not assert causal explanation |
| R4 (equivalence without justification) | **YES — ORANGE** | "Structurally isomorphic" implies STRUCTURAL or higher, but MAP_001 is ANALOGY only. Mismatch. |

**Result:** Signal R4 fires → escalate. Proceed to 02.

### 4.3 02 — Detection

| # | ID | Name | Origin | Pre-existing? | SOT link | H score |
|---|-----|------|--------|--------------|----------|---------|
| 1 | N_TFT_00001 | Flow Rate | TFT | Y | systems/tft_nodes.md §2 | 0 |
| 2 | N_TFT_00002 | Congestion | TFT | Y | systems/tft_nodes.md §3 | 0 |
| 3 | N_TFT_00003 | Traffic Light Phase | TFT | Y | systems/tft_nodes.md §5 | 0 |
| 4 | N_PNT_00001 | Bandwidth | PNT | Y | systems/pnt_nodes.md §1 | 0 |
| 5 | N_PNT_00002 | Queue | PNT | Y | systems/pnt_nodes.md §4 | 0 |
| 6 | MAP_001 | Flow Rate ↔ Bandwidth | Mapping | N (new in scope) | Both SOTs | 3 |
| 7 | MAP_002 | Congestion ↔ Queue | Mapping | N (new in scope) | Both SOTs + queuing theory | 3 |
| 8 | NAC_001 | Traffic Light Phase → no PNT analogue | NAC | N (new in scope) | TFT SOT only | 1 |

**Group classification:**
- Group A (standard): Nodes 1-5 → ES-PRATY
- Group B (pre-existing): none
- Group C (new, anchored): MAP_001, MAP_002, NAC_001 → ES-ANUMA

### 4.4 03 — SOT Traceability

| Component | SOT-1 (TFT) | SOT-2 (PNT) | SOT-3 (Core) | SOT-4 (Gov) | Trace Score | Anchor |
|-----------|------------|------------|-------------|------------|-------------|--------|
| MAP_001 | + | + | - | + | 3/4 | STRONG |
| MAP_002 | + | + | + | + | 4/4 | STRONG |
| NAC_001 | + | - | - | + | 2/4 | MODERATE |

### 4.5 04 — 5-Whys RCA (for R4 signal on "isomorphic" claim)

```
W1: Why does "structurally isomorphic" trigger R4?
  → "Isomorphic" implies STRUCTURAL or EQUIVALENCE, but MAP_001 is ANALOGY only.
W2: Why is MAP_001 ANALOGY only?
  → Flow Rate (veh/hr) and Bandwidth (bps) share rate = quantity/time but physical substrates differ.
W3: Why does the claim overstate the mapping type?
  → The word "isomorphic" is used colloquially, not formally.
W4: Why was "isomorphic" chosen over "analogous"?
  → Linguistic habit — "isomorphic" sounds more rigorous.
W5: Is the claim a fabrication?
  → NO. The mappings exist and are documented. The WORDING is the problem, not the substance.

Root Cause (Type 1 — Category Error in wording): The claim uses "isomorphic" (formal term)
  for a relationship that is partially ANALOGY and partially STRUCTURAL.
```

### 4.6 05 — Scoring

| Component | Score | Band | Label |
|-----------|-------|------|-------|
| N_TFT_00001–00003, N_PNT_00001–00002 | 0-1 | Green | `[AH-OK][ES-PRATY]` |
| MAP_001 | 3 | Blue | `[AH-LOW][ES-ANUMA]` |
| MAP_002 | 3 | Blue | `[AH-LOW][ES-ANUMA]` |
| NAC_001 | 2 | Green | `[AH-OK][ES-ANUMA]` |
| Claim wording ("isomorphic") | 5 | Yellow | `[AH-WARN][ES-ANUMA]` — wording fix needed |

**System average: 1.6/10 (Green)**

### 4.7 06 — Solution

| # | Issue | Component | Score | Priority | Solution Type | Status |
|---|-------|-----------|-------|----------|---------------|--------|
| 1 | "Isomorphic" overstates mapping type | Claim wording | 5 | P2 MEDIUM | DOCUMENT — change to "share structural analogies with one formal correspondence" | OPEN |

---

## Step 5: Top Risk Record

| Rank | Component ID | Name | System | H | W | A | Risk Score | TTL_CLASS | Label |
|------|-------------|------|--------|---|---|---|-----------|-----------|-------|
| 1 | MAP_001 | Flow Rate ↔ Bandwidth | Mapping | 3 | 2 | 0.5 | 9.0 | Historical | `[AH-LOW][RS-LOW][ES-ANUMA]` |
| 2 | MAP_002 | Congestion ↔ Queue | Mapping | 3 | 2 | 0.5 | 9.0 | Historical | `[AH-LOW][RS-LOW][ES-ANUMA]` |
| 3 | NAC_001 | Traffic Light Phase (no analogue) | NAC | 2 | 1 | 0 | 2.0 | Atemporal | `[AH-OK][RS-LOW][ES-ANUMA]` |

---

## Key Takeaways

1. **ANALOGY is the default** — MAP_001 is ANALOGY because the physical substrates differ, even though the mathematical structure matches.
2. **STRUCTURAL requires formal proof** — MAP_002 earned STRUCTURAL via the shared queuing-theory equation (formal correspondence demonstrated).
3. **NAC is a valid result** — Traffic Light Phase has NO analogue in PNT because packet networks use statistical multiplexing, not temporal. This is NOT a gap — it's an important distinction.
4. **Wording triggers signals** — The word "isomorphic" in the claim triggered R4, even though the underlying mappings are valid. Documentation fix (Type 3) resolves it.

---

*DEMO v1.0 — Fully synthetic, domain-agnostic 2-system example. All nodes and claims are fabricated for demonstration. Exported from AHP Template v1.0 (2026-06-12).*
