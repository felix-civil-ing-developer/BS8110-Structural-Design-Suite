# Master Beam Calculator: Self-Weight + Applied UDL
print("--- Master Beam Analysis & Dead Load Tool ---")
print("Type '0' for beam length to exit.\n")

DENSITY_CONCRETE = 24.0  # kN/m^3

while True:
    L = float(input("Enter beam span length L (m): "))
    if L == 0:
        print("Exiting Master Beam Tool. Goodbye!")
        break

    # Section Dimensions for Self-Weight
    width = float(input("Enter beam width (m): "))
    depth = float(input("Enter beam depth (m): "))
    
    # Additional Applied UDL (Live Load / Finishes)
    w_applied = float(input("Enter additional applied UDL in kN/m (Enter 0 if none): "))

    # 1. Calculate Self-Weight UDL (w_self = Volume/m * Density)
    area = width * depth                   # m^2
    w_self = area * DENSITY_CONCRETE       # kN/m
    
    # 2. Total Combined UDL
    w_total = w_self + w_applied           # kN/m

    # 3. Statics Calculations for Simply Supported Beam under UDL
    R_A = (w_total * L) / 2
    R_B = R_A
    V_max = R_A
    M_max = (w_total * (L ** 2)) / 8

    print("\n--- DESIGN SUMMARY ---")
    print(f"Self-Weight UDL (w_self)   : {w_self:.2f} kN/m")
    print(f"Total Design UDL (w_total) : {w_total:.2f} kN/m")
    print(f"Support Reactions (R_A=R_B): {R_A:.2f} kN")
    print(f"Maximum Shear Force (V_max): {V_max:.2f} kN")
    print(f"Maximum Bending Moment     : {M_max:.2f} kNm\n")