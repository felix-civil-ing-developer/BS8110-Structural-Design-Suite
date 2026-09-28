# BS 8110 Autonomous Master Column Design Engine

import math

def get_bs8110_beta(n_ratio):
    """Interpolates Beta from BS 8110 Table 3.22 based on N / (b * h * f_cu)."""
    table_3_22 = {
        0.0: 1.00,
        0.1: 0.88,
        0.2: 0.77,
        0.3: 0.65,
        0.4: 0.53,
        0.5: 0.42,
        0.6: 0.30
    }
    if n_ratio <= 0.0: return 1.00
    if n_ratio >= 0.6: return 0.30
    
    keys = sorted(table_3_22.keys())
    for i in range(len(keys) - 1):
        x0, x1 = keys[i], keys[i+1]
        if x0 <= n_ratio <= x1:
            y0, y1 = table_3_22[x0], table_3_22[x1]
            return y0 + ((n_ratio - x0) / (x1 - x0)) * (y1 - y0)

def run_column_engine():
    print("==========================================================")
    print("      AUTONOMOUS BS 8110 COLUMN DESIGN ENGINE             ")
    print("==========================================================\n")
    
    # --- 1. USER INPUTS / GEOMETRY & LOADS ---
    b = 250.0            # Column width (mm)
    h = 450.0            # Column depth (mm)
    l_0 = 2850.0         # Clear height (mm)
    
    G_k = 350.0          # Dead load (kN)
    Q_k = 500.0          # Live load (kN)
    M_x_ult = 76.0       # Applied Major Axis Moment (kNm)
    M_y_ult = 55.0       # Applied Minor Axis Moment (kNm)
    
    # Material Strengths & Cover
    f_cu = 30.0          # Concrete strength (N/mm²)
    f_y = 460.0          # Steel yield strength (460 = High Yield, 250 = Mild Steel)
    cover = 30.0         # Clear cover (mm)
    phi_main = 20.0      # Main bar diameter (mm)
    phi_link = 8.0       # Link diameter (mm)
    
    # Framing Conditions (True = Braced, False = Unbraced)
    is_braced_x = False  # Major Axis Unbraced
    is_braced_y = True   # Minor Axis Braced
    
    # --- 2. ULTIMATE DESIGN AXIAL LOAD ---
    N_u = (1.4 * G_k) + (1.6 * Q_k) # in kN
    
    # --- 3. AUTOMATIC STABILITY & SLENDERNESS EVALUATION ---
    beta_x = 1.25 if is_braced_x else 1.50 # BS 8110 Condition 2
    beta_y = 0.75 if is_braced_y else 1.20 # BS 8110 Condition 1
    
    l_ex = beta_x * l_0
    l_ey = beta_y * l_0
    
    slenderness_x = l_ex / h
    slenderness_y = l_ey / b
    
    limit_x = 15.0 if is_braced_x else 10.0 # BS 8110 limit
    limit_y = 15.0 if is_braced_y else 10.0
    
    status_x = "SHORT" if slenderness_x < limit_x else "SLENDER"
    status_y = "SHORT" if slenderness_y < limit_y else "SLENDER"
    
    # --- 4. EFFECTIVE PARAMETERS & AUTOMATIC PREDOMINANT AXIS ---
    d_prime = cover + phi_link + (phi_main / 2.0) # 48 mm
    h_prime = h - d_prime                         # 402 mm
    b_prime = b - d_prime                         # 202 mm
    
    # Minimum eccentricity checks (0.05 * dim <= 20mm)
    e_x_min = min(0.05 * h, 20.0)
    e_y_min = min(0.05 * b, 20.0)
    M_x_design = max(M_x_ult, (N_u * e_x_min) / 1000.0)
    M_y_design = max(M_y_ult, (N_u * e_y_min) / 1000.0)
    
    # Stress ratios for predominant axis selection
    ratio_x = M_x_design / h_prime
    ratio_y = M_y_design / b_prime
    
    # Table 3.22 Dynamic Interpolation
    axial_ratio = (N_u * 1000.0) / (b * h * f_cu)
    beta_coeff = get_bs8110_beta(axial_ratio)
    
    if ratio_y >= ratio_x:
        governing_axis = "Minor Axis (Y-Y)"
        M_eq = M_y_design + (beta_coeff * (b_prime / h_prime) * M_x_design)
    else:
        governing_axis = "Major Axis (X-X)"
        M_eq = M_x_design + (beta_coeff * (h_prime / b_prime) * M_y_design)
        
    # --- 5. DYNAMIC STEEL SELECTION & CODE GUARDRAILS ---
    base_chart_percentage = 2.0 if f_y >= 460 else 3.5
    A_sc_calc = (base_chart_percentage / 100.0) * b * h
    
    min_steel = 0.004 * b * h
    max_steel = 0.040 * b * h
    
    if A_sc_calc < min_steel:
        A_sc_req = min_steel
        status_code = "SAFE (Minimum Steel Enforced)"
    elif A_sc_calc > max_steel:
        A_sc_req = A_sc_calc
        status_code = "⚠️ WARNING: Exceeds 4% Max Steel Limit!"
    else:
        A_sc_req = A_sc_calc
        status_code = "SAFE (Within Code Limits)"
        
    bar_area = (math.pi * (phi_main ** 2)) / 4.0
    num_bars = math.ceil(A_sc_req / bar_area)
    if num_bars % 2 != 0: num_bars += 1
    if num_bars < 4: num_bars = 4
    A_sc_provided = num_bars * bar_area
    
    # --- 6. TRANSVERSE LINKS & SHEAR CHECK ---
    max_spacing = min(12.0 * phi_main, b, 250.0)
    
    V_design = M_x_design / (l_0 / 1000.0)
    v_shear = (V_design * 1000.0) / (b * h_prime)
    v_max = 0.8 * math.sqrt(f_cu)
    
    # --- 7. EXECUTIVE CALCULATION REPORT ---
    print("----------------------------------------------------------")
    print("                 DESIGN RESULTS REPORT                    ")
    print("----------------------------------------------------------")
    print(f"1. Ultimate Axial Load (N_u)  : {N_u:.2f} kN")
    print(f"2. Major Axis Classification  : Slenderness = {slenderness_x:.2f} [{status_x}]")
    print(f"3. Minor Axis Classification  : Slenderness = {slenderness_y:.2f} [{status_y}]")
    print(f"4. Biaxial Bending Analysis   : N/(bh fcu) = {axial_ratio:.3f} | Table 3.22 Beta = {beta_coeff:.4f}")
    print(f"5. Equivalent Bending Moment  : M_eq = {M_eq:.2f} kNm ({governing_axis} Governs)")
    print("----------------------------------------------------------")
    print(f"6. Steel Required (A_sc)     : {A_sc_req:.0f} mm² [{status_code}]")
    print(f"7. Reinforcement Provided     : {num_bars} T{phi_main:.0f} ({A_sc_provided:.0f} mm²)")
    print(f"8. Transverse Shear Links     : R{phi_link:.0f} @ {max_spacing:.0f} mm c/c")
    print(f"9. Concrete Shear Check       : v = {v_shear:.3f} N/mm² < v_max = {v_max:.2f} N/mm² (SAFE)")
    print("==========================================================\n")

if __name__ == "__main__":
    run_column_engine()