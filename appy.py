"""
Main Application Entry Point
Coffee Shop Timekeeping and Payroll System

To run: python app.py
"""

from gui_app import TimekeepingGUI

def main():
    """Main function to start the application"""
    print("=" * 50)
    print("Coffee Shop Timekeeping & Payroll System")
    print("=" * 50)
    print("\nStarting application...")
    print("\nDefault Credentials:")
    print("Admin PIN: admin123")
    print("\nNote: Add employees through Admin Panel first")
    print("=" * 50)
    
    app = TimekeepingGUI()
    app.run()

if __name__ == "__main__":
    main()