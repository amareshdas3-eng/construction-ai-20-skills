---
name: "Spec Reviewer"
skill_id: "spec-reviewer"
skill_num: "01"
category: "Before You Bid"
description: "Bid-killers + hidden costs."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #01: Spec Reviewer

**Category:** Before You Bid  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Bid-killers + hidden costs. This playbook cross-checks **Specification Clause** against **Standard EPC Risk Baseline** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Specification Clause):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Standard EPC Risk Baseline):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `SPR-001` | **Severity:** `CRITICAL`
  - **Element / Ref:** Liquidated Damages (LD) & Consequential Loss Waiver
  - **Specification Clause:** Delay LD @ 1.5% per week up to 15% cap; Uncapped consequential power outage liability *(Particular Conditions Cl. 8.7 (P.19))*
  - **Standard EPC Risk Baseline:** 0.5% per week up to 10% cap; Mutual exclusion of consequential loss *(Standard FIDIC Silver/Yellow Baseline)*
  - **Variance:** `BID-KILLER COMMERCIAL TRAP` | **Financial Impact:** $450,000.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Mandatory commercial qualification: Cap total LD at 10% and enforce Sub-Clause 17.6 exclusion of consequential damages.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`

- **ID:** `SPR-002` | **Severity:** `CRITICAL`
  - **Element / Ref:** Sole-Source Protection Relay & SCADA Mandate
  - **Specification Clause:** Relays must be single-OEM proprietary ring with zero 'or approved equal' allowance *(Spec Sec 07.1.2 (P.108))*
  - **Standard EPC Risk Baseline:** 3 Approved Makes (ABB / Siemens / Schneider / GE) *(Competitive Multi-Vendor Clause)*
  - **Variance:** `SOLE-SOURCE PRICING TRAP` | **Financial Impact:** $68,000.00 | **Schedule Delta:** 21 Days
  - **Recommended Action:** Submit commercial clarification requesting addition of approved equivalent IEC 61850 Tier-1 makes.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`

- **ID:** `SPR-003` | **Severity:** `MAJOR`
  - **Element / Ref:** Overseas Factory Acceptance Test (FAT) Travel Costs
  - **Specification Clause:** Contractor shall bear international airfare, 5-star hotel & per-diem for 6 Employer engineers for 10 days per FAT *(Spec Sec 01.9.4 (P.24))*
  - **Standard EPC Risk Baseline:** Employer bears own travel/living costs; Contractor covers test bay costs only *(Standard Inspection Allowance)*
  - **Variance:** `HIDDEN COST ($42k)` | **Financial Impact:** $42,000.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Add $42,000 explicit provisional allowance in Preliminaries BOQ or qualify out.
  - **Human Sign-Off Gate:** `APPROVED`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
