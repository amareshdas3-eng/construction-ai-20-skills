---
name: "Spec vs Drawings Check"
skill_id: "spec-vs-drawings"
skill_num: "03"
category: "Before You Bid"
description: "Spec–drawing conflicts."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #03: Spec vs Drawings Check

**Category:** Before You Bid  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Spec–drawing conflicts. This playbook cross-checks **Specification Requirement** against **Drawing Shown Value** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Specification Requirement):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Drawing Shown Value):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `DSC-001` | **Severity:** `CRITICAL`
  - **Element / Ref:** 33kV Underground Power Feeder Cable (SYS-CBL-33KV)
  - **Specification Requirement:** 3C x 400 sq.mm Copper (Cu), XLPE, Corrugated Al Sheath *(Sec 04.2.1 (P.42))*
  - **Drawing Shown Value:** 3C x 400 sq.mm Aluminium (Al), XLPE, SWA *(DWG-EL-SLD-001 Rev B (Grid B4))*
  - **Variance:** `GOLD_PLATING_SPEC` | **Financial Impact:** $48,500.00 | **Schedule Delta:** 14 Days
  - **Recommended Action:** RFI-001: Confirm whether 33kV feeder is Copper (per Spec) or Aluminium (per SLD).
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`

- **ID:** `DSC-002` | **Severity:** `CRITICAL`
  - **Element / Ref:** 33kV Indoor GIS Switchgear Busbar & Breaker
  - **Specification Requirement:** 31.5 kA for 3 seconds short-time withstand *(Sec 05.1.4 (P.68))*
  - **Drawing Shown Value:** 25 kA for 1 second *(DWG-EL-SLD-001 Rev B (Grid D2))*
  - **Variance:** `DIRECT_CONFLICT` | **Financial Impact:** $62,000.00 | **Schedule Delta:** 28 Days
  - **Recommended Action:** RFI-002: Confirm governing fault rating (31.5kA/3s vs 25kA/1s).
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`

- **ID:** `DSC-003` | **Severity:** `MAJOR`
  - **Element / Ref:** 15/20 MVA 33/11kV Power Transformer Neutral Earthing
  - **Specification Requirement:** Dyn11 with 11kV Neutral Grounding Resistor (NGR 400A, 10s) *(Sec 06.3.2 (P.91))*
  - **Drawing Shown Value:** Dyn11 Solidly Earthed (No NGR shown on SLD) *(DWG-EL-SLD-002 Rev A (Grid C6))*
  - **Variance:** `DIRECT_CONFLICT` | **Financial Impact:** $19,500.00 | **Schedule Delta:** 10 Days
  - **Recommended Action:** RFI-003: Clarify if 11kV NGR cubicles are required.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `DSC-004` | **Severity:** `MAJOR`
  - **Element / Ref:** Numerical Protection Relays Communication Architecture
  - **Specification Requirement:** IEC 61850 Ed.2 Dual-Port PRP Fiber Ring *(Sec 07.4.1 (P.112))*
  - **Drawing Shown Value:** RS-485 Modbus RTU Daisy-Chain Twisted Pair *(DWG-EL-PROT-004 Rev B (Note 7))*
  - **Variance:** `DIRECT_CONFLICT` | **Financial Impact:** $14,200.00 | **Schedule Delta:** 7 Days
  - **Recommended Action:** RFI-004: Confirm Ethernet Ring switches vs RS-485 serial bus.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `DSC-005` | **Severity:** `MAJOR`
  - **Element / Ref:** Outdoor Cable Containment Ladder Material
  - **Specification Requirement:** SS316L Stainless Steel Ladder Tray (Marine Grade) *(Sec 08.1.9 (P.130))*
  - **Drawing Shown Value:** Hot-Dip Galvanized Mild Steel (HDGI 85 microns) *(DWG-EL-GA-009 Rev C (Sec A-A))*
  - **Variance:** `GOLD_PLATING_SPEC` | **Financial Impact:** $34,000.00 | **Schedule Delta:** 12 Days
  - **Recommended Action:** RFI-005: Confirm if HDGI tray is acceptable in non-process zone.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `DSC-006` | **Severity:** `MAJOR`
  - **Element / Ref:** Main Substation Buried Earth Grid Conductor
  - **Specification Requirement:** 75 x 10 mm Annealed Tinned Copper Tape *(Sec 09.2.1 (P.145))*
  - **Drawing Shown Value:** Omitted from Layout Drawings (Missing Sheet E-104) *([MISSING FROM DRAWING SET])*
  - **Variance:** `OMISSION_ON_DRAWING` | **Financial Impact:** $29,800.00 | **Schedule Delta:** 5 Days
  - **Recommended Action:** RFI-006: Issue missing Earthing Layout E-104 and confirm Copper vs GI strip.
  - **Human Sign-Off Gate:** `APPROVED`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
