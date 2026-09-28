# Multi-Beam Floor System Analyzer

def get_safe_number(prompt_text):
    """Safely gets a float input from the user."""
    while True:
        user_input = input(prompt_text)
        try:
            return float(user_input)
        except ValueError:
            print("❌ Invalid input! Please enter a numerical value.\n")

print("=========================================")
print("   MULTI-BEAM FLOOR SYSTEM ANALYZER      ")
print("=========================================\n")

# 1. Collect beam counts
num_beams = int(get_safe_number("How many beams are on this floor level? "))

# Lists to store beam data
beam_ids = []
spans = []
udls = []
moments = []

# 2. Populate lists using a loop
print(f"\n--- Entering Data for {num_beams} Beams ---")
for i in range(num_beams):
    print(f"\nBeam #{i+1}:")
    b_id = input(f"Enter Beam ID (e.g., B10{i+1}): ").strip()
    L = get_safe_number("Enter span length L (m): ")
    w = get_safe_number("Enter total UDL w (kN/m): ")
    
    # Calculate max moment: M_max = (w * L^2) / 8
    M_max = (w * (L ** 2)) / 8
    
    # Append (add) values to our lists
    beam_ids.append(b_id)
    spans.append(L)
    udls.append(w)
    moments.append(M_max)

# 3. Print Summary Table
print("\n==========================================================")
print("                   FLOOR BEAM SUMMARY                     ")
print("==========================================================")
print(f"{'Beam ID':<10} | {'Span (m)':<10} | {'UDL (kN/m)':<12} | {'M_max (kNm)':<12}")
print("-" * 58)

for i in range(len(beam_ids)):
    print(f"{beam_ids[i]:<10} | {spans[i]:<10.2f} | {udls[i]:<12.2f} | {moments[i]:<12.2f}")

print("==========================================================")

# 4. Find the Critical Beam (Highest Moment)
max_moment_val = max(moments)
critical_index = moments.index(max_moment_val)
critical_beam = beam_ids[critical_index]

print(f"\n⚡ CRITICAL MEMBER: {critical_beam} with Maximum Bending Moment = {max_moment_val:.2f} kNm\n")