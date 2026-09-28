# BS 8110 Autonomous Structural Design Suite

A collection of professional Python modules designed to automate reinforced concrete element analysis and design checks according to **BS 8110**.

# BS 8110 Autonomous Structural Design Suite

A collection of professional Python modules designed to automate reinforced concrete element analysis and design checks according to **BS 8110**.

## 🚀 Key Features

* **Autonomous Column Design Engine (`bs8110_master_column_engine.py`):**
  * Automatic frame stability classification (Braced vs. Unbraced end conditions).
  * Dynamic β-coefficient interpolation from **BS 8110 Table 3.22**.
  * Biaxial bending evaluation and automatic governing axis determination.
  * Code limit guardrails (0.4% minimum to 4.0% maximum steel reinforcement limits).
* **Multi-Beam Floor Analyzer (`multi_beam_analyzer.py`):**
  * Automated batch calculation of bending moments (M_max = wL²/8).
  * Formatted summary tables and critical member flagging.
* **Master Suite Hub (`main.py`):**
  * Central interactive terminal menu to run all tools seamlessly.

---

## 📊 Assignment Problem & Validation Output
<img width="571" height="314" alt="Screenshot 2026-09-28 160031" src="https://github.com/user-attachments/assets/38666e10-69ba-42e9-ba67-44a7f67eb131" />

```text
==========================================================
      AUTONOMOUS BS 8110 COLUMN DESIGN ENGINE             
==========================================================

----------------------------------------------------------
                 DESIGN RESULTS REPORT                    
----------------------------------------------------------
1. Ultimate Axial Load (N_u)  : 1290.00 kN
2. Major Axis Classification  : Slenderness = 9.50 [SHORT]
3. Minor Axis Classification  : Slenderness = 8.55 [SHORT]
4. Biaxial Bending Analysis   : N/(bh fcu) = 0.382 | Table 3.22 Beta = 0.5513
5. Equivalent Bending Moment  : M_eq = 76.05 kNm (Minor Axis (Y-Y) Governs)
----------------------------------------------------------
6. Steel Required (A_sc)     : 2250 mm² [SAFE (Within Code Limits)]
7. Reinforcement Provided     : 8 T20 (2513 mm²)
8. Transverse Shear Links     : R8 @ 240 mm c/c
9. Concrete Shear Check       : v = 0.265 N/mm² < v_max = 4.38 N/mm² (SAFE)
==========================================================
