---
name: "Bid Hunter (SAM.gov)"
skill_id: "bid-hunter"
skill_num: "05"
category: "Before You Bid"
description: "Contract matches + bid drafts."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #05: Bid Hunter (SAM.gov)

**Category:** Before You Bid  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Contract matches + bid drafts. This playbook cross-checks **Solicitation / Tender Criteria** against **Capability & Go/No-Go Score** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Solicitation / Tender Criteria):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Capability & Go/No-Go Score):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `BID-001` | **Severity:** `PASS`
  - **Element / Ref:** SOL-2026-IND-33KV: Industrial Park 33/11kV GIS Substation Turnkey
  - **Solicitation / Tender Criteria:** Est. Value: $4.8M | Deadline: 28 Days | Past Perf: 2x 33kV Substations in 7 yrs *(NAICS 237130 / CPV 45232220)*
  - **Capability & Go/No-Go Score:** 3x 33kV/132kV Substations Completed; PMP + Senior HV Commissioning Team ready *(Company Profile Match)*
  - **Variance:** `GO SCORE: 92/100` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** HIGH PRIORITY GO: Generate Technical Volume I draft and submit 6 pre-bid RFIs.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `BID-002` | **Severity:** `PASS`
  - **Element / Ref:** SOL-2026-PORT-MES: Port Electrification & Shore Power MV Upgrade
  - **Solicitation / Tender Criteria:** Est. Value: $3.2M | Deadline: 35 Days | Requires IEC 60092 / HV Shore Connection *(NAICS 238210 / Marine HV)*
  - **Capability & Go/No-Go Score:** Strong MV Switchgear & Protection Relay Testing fit; partner for marine civil *(Company Profile Match)*
  - **Variance:** `GO SCORE: 84/100` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** QUALIFIED GO: Pursue Electrical/Protection & Project Controls package.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `BID-003` | **Severity:** `MAJOR`
  - **Element / Ref:** SOL-2026-400KV-TL: 400kV Overhead Transmission Line (180 km)
  - **Solicitation / Tender Criteria:** Est. Value: $42M | Requires $10M Bid Bond + Tower Manufacturing Plant *(NAICS 237130 / EHV Towers)*
  - **Capability & Go/No-Go Score:** Outside target asset class (EHV lattice tower fabrication required) *(Company Profile Match)*
  - **Variance:** `NO-GO SCORE: 31/100` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** DECLINE BID: Preserve estimating bandwidth for industrial MV/HV substation tenders.
  - **Human Sign-Off Gate:** `APPROVED`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
