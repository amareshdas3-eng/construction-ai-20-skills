---
name: "IFC to Priced BOQ"
skill_id: "ifc-to-boq"
skill_num: "13"
category: "The Model"
description: "Priced BOQ with your rates."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #13: IFC to Priced BOQ

**Category:** The Model  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Priced BOQ with your rates. This playbook cross-checks **IFC Class & Qto Base Quantities** against **Composite Unit Rate & Priced Total** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (IFC Class & Qto Base Quantities):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Composite Unit Rate & Priced Total):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `IFC-001` | **Severity:** `PASS`
  - **Element / Ref:** `IfcFooting` & `IfcSlab` (Substation Transformer Bunds & GIS Basement)
  - **IFC Class & Qto Base Quantities:** Net Volume = 842.0 m3 C35/45 Sulfate-Resistant Concrete + 5% Waste = 884.1 m3 *(Model `SUB_STR_IFC4.ifc` (46 Elements))*
  - **Composite Unit Rate & Priced Total:** Material ($135) + Labor ($32) + Pump/Plant ($18) x 884.1 m3 *(Rate Library: $185.00 / m3 (Placed))*
  - **Variance:** `$163,558.50` | **Financial Impact:** $163,558.50 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Priced line item exported to Master BOQ Division 03.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `IFC-002` | **Severity:** `PASS`
  - **Element / Ref:** `IfcCableCarrierSegment` (Heavy-Duty Perforated & Ladder Cable Trays)
  - **IFC Class & Qto Base Quantities:** Net Length = 612.0 m + 7.5% Cutting/Fittings Allowance = 657.9 m *(Model `SUB_MEP_IFC4.ifc` (218 Segments))*
  - **Composite Unit Rate & Priced Total:** Material ($46) + Supports ($10) + Installation Labor ($12) x 657.9 m *(Rate Library: $68.00 / m (Installed))*
  - **Variance:** `$44,737.20` | **Financial Impact:** $44,737.20 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Priced line item exported to Master BOQ Division 26.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `IFC-003` | **Severity:** `MAJOR`
  - **Element / Ref:** `IfcElectricDistributionBoard` (110V DC Dual Battery Charger & DBs)
  - **IFC Class & Qto Base Quantities:** 4 Units Modeled, but `Qto_BaseQuantities` & `Pset_ElectricalDeviceCommon` Rating is NULL *(Model `SUB_MEP_IFC4.ifc` (4 Elements))*
  - **Composite Unit Rate & Priced Total:** Unmapped kVA/Ah rating in IFC properties; provisional rate $18,500/unit applied *(Rate Library Lookup)*
  - **Variance:** `$74,000.00 (PROV)` | **Financial Impact:** $74,000.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Verify 110V DC 300Ah Ni-Cd vs VRLA battery bank spec before locking unit rate.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
