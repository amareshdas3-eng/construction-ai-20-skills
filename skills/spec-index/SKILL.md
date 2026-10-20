---
name: "Spec Index"
skill_id: "spec-index"
skill_num: "02"
category: "Before You Bid"
description: "A searchable spec database."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #02: Spec Index

**Category:** Before You Bid  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
A searchable spec database. This playbook cross-checks **CSI / Package Division** against **Referenced Standards & Submittals** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (CSI / Package Division):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Referenced Standards & Submittals):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

---

## 3. Multi-Agent Pipeline Execution
1. **CoordinatorAgent:** Initializes audit session and routes files to parser.
2. **DocumentExtractionAgent:** Ingests and normalizes raw text and schedules into structured parameters.
3. **Spec / Source Analysis Agent:** Builds baseline criteria and technical constraints.
4. **Drawing / Source Analysis Agent:** Extracts comparison values and tolerance ranges.
5. **DiscrepancyResolutionAgent:** Executes deterministic rule checks to compute cost deltas and critical path delays.
6. **QualityAssuranceAgent:** Verifies 100% citation trace back to clause and drawing sheet references.
7. **HumanApprovalGate (HITL):** Holds all CRITICAL items for Lead Engineer sign-off before report generation.
8. **ReportingAgent:** Exports Discrepancy Registers (CSV, JSON, Markdown RFIs).

---

## 4. Audited Findings & Ground Truth Register

- **ID:** `SPI-001` | **Severity:** `PASS`
  - **Element / Ref:** Div 26 05 13 — Medium-Voltage Cables (33kV & 11kV)
  - **CSI / Package Division:** XLPE Insulated, Armored Power Cables *(Spec Sec 04 (Pages 38-61))*
  - **Referenced Standards & Submittals:** Submittals: Type Test Certs (<5 yrs), Ampacity Calc, Pulling Tension Calc, Drum Schedule *(IEC 60502-2 / IS 7098-2)*
  - **Variance:** `INDEXED (6 Submittals)` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Linked to Electrical Takeoff & Spec Compliance.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `SPI-002` | **Severity:** `PASS`
  - **Element / Ref:** Div 26 12 19 — Pad-Mounted / Substation Liquid Transformers
  - **CSI / Package Division:** 15/20 MVA 33/11kV ONAN/ONAF with OLTC & RTCC *(Spec Sec 06 (Pages 85-106))*
  - **Referenced Standards & Submittals:** Submittals: GA, Losses Guarantee, Short-Circuit Calc, Oil DGA Baseline, Turret CT Curves *(IEC 60076 / IEEE C57.12)*
  - **Variance:** `INDEXED (8 Submittals)` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Linked to Cut Sheet -> Revit Family & Spec Compliance.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `SPI-003` | **Severity:** `MINOR`
  - **Element / Ref:** Div 26 13 26 — Medium-Voltage Gas-Insulated Switchgear (GIS)
  - **CSI / Package Division:** 33kV Indoor SF6 / Clean-Air GIS Panels *(Spec Sec 05 (Pages 62-84))*
  - **Referenced Standards & Submittals:** Submittals: Single Line, Interlock Logic, Internal Arc Test Report (IAC AFLR 31.5kA 1s) *(IEC 62271-200)*
  - **Variance:** `CONFLICTING ANNEX REF` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Note: Annex B references obsolete IEC 60298; log minor administrative RFI.
  - **Human Sign-Off Gate:** `APPROVED`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
