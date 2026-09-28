# Concrete Column Load Checker

print("--- Felix Column Design Load Checker ---")
print("Type 'exit' as Column ID to stop.\n")

while True:
    column_id = input("Enter Column ID (or 'exit'): ")
    
    # Check if user wants to quit
    if column_id.lower() == "exit":
        print("Closing check system. Goodbye!")
        break
        
    N_u = float(input("Enter Ultimate Axial Load N_u (in kN): "))
    A_c = float(input("Enter Column cross-sectional area A_c (in mm²): "))
    
    # Compute the average compressive stress (N/mm²)
    sigma = (N_u * 1000) / A_c
    
    # Evaluate stress state
    if sigma <= 15:
        status = "SAFE - Standard Column Section"
    elif sigma <= 25:
        status = "WARNING - High Stress Section"
    else:
        status = "UNSAFE - Section Redesign Required"

    print(f"\nCalculated Stress (sigma): {sigma:.2f} N/mm²")
    print(f"Status: {status}\n")

    # Generate Automated Report
    filename = f"{column_id}_report.txt"
    with open(filename, "w") as file:
        file.write("===================================\n")
        file.write("   COLUMN DESIGN STRESS REPORT     \n")
        file.write("===================================\n")
        file.write(f"Column ID    : {column_id}\n")
        file.write(f"Axial Load   : {N_u:.2f} kN\n")
        file.write(f"Section Area : {A_c:.2f} mm²\n")
        file.write(f"Stress       : {sigma:.2f} N/mm²\n")
        file.write(f"Status       : {status}\n")
        file.write("===================================\n")
        
    print(f"Report saved as '{filename}' in Python_Civil_Tools folder!\n")