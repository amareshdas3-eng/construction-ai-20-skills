---
name: "Change Order Audit"
skill_id: "change-order-audit"
skill_num: "18"
category: "Schedule + Cost"
description: "Rates, markups + quantities."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #18: Change Order Audit

**Category:** Schedule + Cost  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Rates, markups + quantities. This playbook cross-checks **Subcontractor Claimed Variation (VO-007)** against **Forensic Contract & Star-Rate Audit** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Subcontractor Claimed Variation (VO-007)):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Forensic Contract & Star-Rate Audit):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `COA-001` | **Severity:** `CRITICAL`
  - **Element / Ref:** VO-007 Line 1: Hard Rock Excavation in 33kV Trench (Claimed: $84,500)
  - **Subcontractor Claimed Variation (VO-007):** Joint Survey Sheet #19 confirms only 410 m3 rock; Contract BOQ Item 2.04 already has fixed rock rate of $68.00/m3 *(Claimed: 650 m3 @ $130.00/m3 (Star Rate))*
  - **Forensic Contract & Star-Rate Audit:** Audited Value = $27,880.00 (Disallowed $56,620.00 due to quantity inflation & ignoring contract rate) *(Audited Entitlement: 410 m3 @ $68.00/m3)*
  - **Variance:** `-$56,620 DISALLOWED` | **Financial Impact:** $-56,620.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Enforce Contract BOQ Item 2.04 rate ($68/m3) and signed joint topological survey (410 m3).
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`

- **ID:** `COA-002` | **Severity:** `MAJOR`
  - **Element / Ref:** VO-007 Line 2: Additional 4x150mm HDPE Road Crossing Ducts (Claimed: $31,200)
  - **Subcontractor Claimed Variation (VO-007):** Drawing redline confirms 96 m net length; Contract limits OH&P markup on variations to 12% max *(Claimed: 120 m @ $185/m + 25% OH&P Markup)*
  - **Forensic Contract & Star-Rate Audit:** Audited Value = $15,267.84 (Disallowed $15,932.16 in excess waste & markup padding) *(Audited: 96 m @ $142/m x 1.12 OH&P)*
  - **Variance:** `-$15,932 DISALLOWED` | **Financial Impact:** $-15,932.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Cap OH&P at contractual 12% under FIDIC Sub-Clause 13.3 and certify $15,267.84.
  - **Human Sign-Off Gate:** `APPROVED`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
