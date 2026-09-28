# Smart Tools: Reusable Functions & Error Handling

def get_safe_number(prompt_text):
    """Repeats input prompt until user enters a valid decimal number."""
    while True:
        user_input = input(prompt_text)
        try:
            return float(user_input)
        except ValueError:
            print("❌ Invalid input! Please enter a numerical value (e.g., 12.5).\n")

def calculate_beam_moment(length, load):
    """Calculates max bending moment for a simply supported beam under UDL."""
    return (load * (length ** 2)) / 8

# --- Main Program Flow ---
print("--- Professional Beam Calculator ---")

span = get_safe_number("Enter span length L (m): ")
udl = get_safe_number("Enter total UDL w (kN/m): ")

max_moment = calculate_beam_moment(span, udl)

print(f"\n✅ Maximum Bending Moment (M_max): {max_moment:.2f} kNm")