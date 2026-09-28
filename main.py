# Master Structural Analysis Suite Menu

import os

def display_menu():
    print("=========================================")
    print("     CIVIL SUITE - MASTER MENU          ")
    print("=========================================")
    print("1. Beam UDL Analysis")
    print("2. Column Stress Checker")
    print("3. Concrete Strength Checker")
    print("4. Exit Suite")
    print("=========================================")

while True:
    display_menu()
    choice = input("Select a tool (1-4): ").strip()

    if choice == "1":
        print("\n--- Launching Beam Analysis ---")
        os.system("python master_beam.py")
    elif choice == "2":
        print("\n--- Launching Column Stress Checker ---")
        os.system("python column_check.py")
    elif choice == "3":
        print("\n--- Launching Concrete Strength Checker ---")
        os.system("python concrete_check.py")
    elif choice == "4":
        print("\nThank you for using Civil Suite. Goodbye!")
        break
    else:
        print("\n❌ Invalid selection! Please enter a number from 1 to 4.\n")