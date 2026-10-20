# Formal Request for Information (RFI) & Discrepancy Register
**Project:** 33/11 kV Industrial Receiving Substation EPC Package
**Audit Date:** 2026-10-20 07:27:55
**Total Identified Discrepancies:** 6

| ID | Severity | Element Tag | Specification Requirement | Drawing Shown Value | Cost Exposure | Schedule Delay | Action / RFI Question | Human Gate |
|---|---|---|---|---|---|---|---|---|
| **DSC-001** | `CRITICAL` | 33kV Underground Power Feeder Cable (SYS-CBL-33KV) | 3C x 400 sq.mm Copper (Cu), XLPE, Corrugated Al Sheath (*Sec 04.2.1 (P.42)*) | 3C x 400 sq.mm Aluminium (Al), XLPE, SWA (*DWG-EL-SLD-001 Rev B (Grid B4)*) | $48,500.00 | 14 Days | RFI-001: Confirm whether 33kV feeder is Copper (per Spec) or Aluminium (per SLD). | **HOLD_FOR_LEAD_ENGINEER** |
| **DSC-002** | `CRITICAL` | 33kV Indoor GIS Switchgear Busbar & Breaker | 31.5 kA for 3 seconds short-time withstand (*Sec 05.1.4 (P.68)*) | 25 kA for 1 second (*DWG-EL-SLD-001 Rev B (Grid D2)*) | $62,000.00 | 28 Days | RFI-002: Confirm governing fault rating (31.5kA/3s vs 25kA/1s). | **HOLD_FOR_LEAD_ENGINEER** |
| **DSC-003** | `MAJOR` | 15/20 MVA 33/11kV Power Transformer Neutral Earthing | Dyn11 with 11kV Neutral Grounding Resistor (NGR 400A, 10s) (*Sec 06.3.2 (P.91)*) | Dyn11 Solidly Earthed (No NGR shown on SLD) (*DWG-EL-SLD-002 Rev A (Grid C6)*) | $19,500.00 | 10 Days | RFI-003: Clarify if 11kV NGR cubicles are required. | **APPROVED** |
| **DSC-004** | `MAJOR` | Numerical Protection Relays Communication Architecture | IEC 61850 Ed.2 Dual-Port PRP Fiber Ring (*Sec 07.4.1 (P.112)*) | RS-485 Modbus RTU Daisy-Chain Twisted Pair (*DWG-EL-PROT-004 Rev B (Note 7)*) | $14,200.00 | 7 Days | RFI-004: Confirm Ethernet Ring switches vs RS-485 serial bus. | **APPROVED** |
| **DSC-005** | `MAJOR` | Outdoor Cable Containment Ladder Material | SS316L Stainless Steel Ladder Tray (Marine Grade) (*Sec 08.1.9 (P.130)*) | Hot-Dip Galvanized Mild Steel (HDGI 85 microns) (*DWG-EL-GA-009 Rev C (Sec A-A)*) | $34,000.00 | 12 Days | RFI-005: Confirm if HDGI tray is acceptable in non-process zone. | **APPROVED** |
| **DSC-006** | `MAJOR` | Main Substation Buried Earth Grid Conductor | 75 x 10 mm Annealed Tinned Copper Tape (*Sec 09.2.1 (P.145)*) | Omitted from Layout Drawings (Missing Sheet E-104) (*[MISSING FROM DRAWING SET] (Omitted Sheet E-104)*) | $29,800.00 | 5 Days | RFI-006: Issue missing Earthing Layout E-104 and confirm Copper vs GI strip. | **APPROVED** |

---
*Generated 100% locally by ProEngineering Multi-Agent Orchestrator.*