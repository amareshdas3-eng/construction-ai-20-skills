---
name: "Electrical Takeoff"
skill_id: "electrical-takeoff"
skill_num: "07"
category: "Drawings"
description: "Two-way counts + drawing proof."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #07: Electrical Takeoff

**Category:** Drawings  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Two-way counts + drawing proof. This playbook cross-checks **Path A: SLD & Cable Schedule** against **Path B: Plan Layout & Routing** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Path A: SLD & Cable Schedule):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Path B: Plan Layout & Routing):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `ETO-001` | **Severity:** `PASS`
  - **Element / Ref:** 33kV GIS Indoor Switchgear Panels (2 Incomer + 1 Bus Coupler + 6 Feeder)
  - **Path A: SLD & Cable Schedule:** 9 Panels Total (1250A Bus, Motorised Earth Switches) *(DWG-EL-SLD-001 Rev B)*
  - **Path B: Plan Layout & Routing:** 9 Bays Counted on Floor Plan (7,200mm x 1,450mm footprint) *(DWG-EL-GA-009 Rev C (Room 101))*
  - **Variance:** `EXACT MATCH (9 Nos.)` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Adopt 9 Panels in BOQ.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `ETO-002` | **Severity:** `CRITICAL`
  - **Element / Ref:** 11kV Outgoing XLPE Feeder Cables (3C x 300 sq.mm Al)
  - **Path A: SLD & Cable Schedule:** 14 Outgoing Circuits Scheduled (Total Scheduled Length: 2,850 m) *(DWG-EL-CBL-003 Cable Schedule)*
  - **Path B: Plan Layout & Routing:** 16 Outgoing Circuits Drawn on Trench Plan + 420m vertical risers & 10% slack = 3,597 m *(DWG-EL-RTG-005 Trench Layout)*
  - **Variance:** `+747 m VARIANCE (+26.2%)` | **Financial Impact:** $38,900.00 | **Schedule Delta:** 6 Days
  - **Recommended Action:** Schedule omits 2 spare motor feeders (FDR-15/16) and vertical termination drops; adopt 3,600m.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`

- **ID:** `ETO-003` | **Severity:** `MAJOR`
  - **Element / Ref:** Substation Building LED Industrial High-Bay & Emergency Luminaires
  - **Path A: SLD & Cable Schedule:** 48 Nos. 120W High-Bay + 18 Nos. Emergency Bulkheads *(Luminaire Schedule DWG-EL-LTG-01)*
  - **Path B: Plan Layout & Routing:** 54 Nos. 120W High-Bay + 22 Nos. Emergency Bulkheads counted across grids A1-F6 *(Lighting Plan DWG-EL-LTG-02)*
  - **Variance:** `+10 LUMINAIRES ON PLAN` | **Financial Impact:** $4,600.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Price 54 High-Bay + 22 Bulkheads per layout count and flag BOQ quantity adjustment.
  - **Human Sign-Off Gate:** `APPROVED`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
