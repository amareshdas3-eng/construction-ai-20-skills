---
name: "Drawing Index"
skill_id: "drawing-index"
skill_num: "06"
category: "Drawings"
description: "Searchable drawing database."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #06: Drawing Index

**Category:** Drawings  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Searchable drawing database. This playbook cross-checks **Title Block Metadata** against **Drawing Register Audit** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Title Block Metadata):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Drawing Register Audit):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `DRI-001` | **Severity:** `PASS`
  - **Element / Ref:** DWG-EL-SLD-001 — 33kV & 11kV Master Single Line Diagram
  - **Title Block Metadata:** Rev B | Date: 2026-09-15 | Status: Issued for Tender *(Electrical / Scale: NTS)*
  - **Drawing Register Audit:** Matches Transmittal Line 01 *(Cover Index Match)*
  - **Variance:** `VERIFIED` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Indexed in searchable CSV database.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `DRI-002` | **Severity:** `MAJOR`
  - **Element / Ref:** DWG-EL-GA-009 — Substation Equipment General Arrangement & Sections
  - **Title Block Metadata:** Title Block shows Rev C (2026-09-28) *(Electrical / Scale: 1:50)*
  - **Drawing Register Audit:** Transmittal lists Rev B (2026-08-19) *(Cover Transmittal Index)*
  - **Variance:** `REVISION MISMATCH` | **Financial Impact:** $0.00 | **Schedule Delta:** 2 Days
  - **Recommended Action:** Confirm Rev C supersedes Rev B for contractual pricing baseline.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`

- **ID:** `DRI-003` | **Severity:** `CRITICAL`
  - **Element / Ref:** DWG-EL-EAR-104 — Main Substation Earthing & Lightning Protection Layout
  - **Title Block Metadata:** Referenced on SLD Note 11 & Transmittal Line 14 *(Electrical / Scale: 1:100)*
  - **Drawing Register Audit:** Sheet Missing from Tender Zip Package *(PDF Drawing Folder)*
  - **Variance:** `MISSING SHEET` | **Financial Impact:** $29,800.00 | **Schedule Delta:** 5 Days
  - **Recommended Action:** Request immediate issuance of DWG-EL-EAR-104.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
