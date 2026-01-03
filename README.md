# Timekeeping-Automated-Payroll-System
FINAL PROJECT – PYTHON APPLICATION (FINALS) Timekeeping &amp; Automated Payroll System


PROJECT DESCRIPTION
You are required to design and develop a Python-based Timekeeping and Automated Payroll System
related to your own chosen business or store.
Your system must allow employees to record their own Time In and Time Out, while the system
automatically computes their working hours and salary (ETC – Estimated Time Compensation).
This project integrates Object-Oriented Programming, GUI Development, File Handling, and
Automation, simulating a real-world business system.

CHOOSE YOUR BUSINESS THEME
You must choose ONE business/store (or propose your own):
Examples:
• Small Grocery Store
• Coffee Shop / Milk Tea Shop
• Hardware Store
• Restaurant / Canteen
• Internet Café
• Printing Shop
• Pharmacy
• Tailoring Shop
• Beauty Salon / Barbershop
• Repair Shop
• Your family’s real business (allowed)
The logic stays the same; only the business context changes.

SYSTEM OBJECTIVES
Your system must:
✔Allow employees to log in using Employee ID + PIN
✔Allow employees to Time In and Time Out on their own
✔Automatically compute:
• Hours Worked
• Payroll (ETC = hours × rate)
✔Separate Employee Mode and Admin Mode
✔Generate Attendance and Payroll Reports
✔Save reports to CSV files

REQUIRED FEATURES (STRICTLY REQUIRED)
1. LOGIN SYSTEM
• Employee Login:
o Employee ID
o PIN
• Admin Login:
o Admin PIN (or admin credentials)

2. EMPLOYEE MODE
Employees must be able to:
✔Time In
✔Time Out
✔View their own:
• Hours worked
• Salary (ETC)
Employees must NOT see other employees’ data.

3. ADMIN MODE
Admin must be able to:
✔Add employees
✔Set hourly rate
✔View employee list
✔View reports:
• Daily Attendance
• Weekly Payroll Summary
• Monthly Payroll Summary
✔Export reports to CSV

4. TIMEKEEPING LOGIC
The system must correctly compute:
Hours Worked = Time Out – Time In
ETC = Hours Worked × Hourly Rate
✔Time Out must not work without Time In
✔Proper error handling required

5. FILE HANDLING (CSV)
Your system must generate:
• daily_report.csv
• weekly_report.csv
• monthly_report.csv
Each file must contain:
• Employee ID
• Employee Name
• Date
• Time In
• Time Out
• Hours Worked
• ETC

6. GUI REQUIREMENT
• Use Tkinter
• Must be user-friendly
• Buttons must be labeled clearly
• Separate windows for:
o Login
o Employee Panel
o Admin Panel
o Reports

PROGRAMMING REQUIREMENTS
Your system MUST USE:
✔Classes & Objects
✔At least one Custom Exception
✔File I/O (CSV)
✔Functions & Methods
✔Iteration (for reports)
✔Modular design (separate .py files)

REQUIRED PROJECT STRUCTURE
project_folder/
│
├── models.py
├── timelog.py
├── manager.py
├── gui_app.py
├── app.py
└── reports/ (optional)

SAMPLE SCENARIO (For Students)
Business: Coffee Shop
Employee: Juan Dela Cruz
Rate: ₱60/hour
• Time In: 8:00 AM
• Time Out: 5:00 PM
System Output:
• Hours Worked: 9.00
• ETC: ₱540.00
Saved automatically to CSV.
