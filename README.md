# Timekeeping and Automated Payroll System (Python)

## Project Description
You are required to design and develop a Python-based Timekeeping and Automated Payroll System related to your chosen business or store. The system allows employees to record their own Time In and Time Out, while automatically computing their working hours and salary (ETC – Estimated Time Compensation). This project integrates Object-Oriented Programming, GUI Development, File Handling, and Automation to simulate a real-world business system.

## Choose Your Business Theme
You must choose **ONE** business/store (or propose your own):

- Small Grocery Store  
- Coffee Shop / Milk Tea Shop  
- Hardware Store  
- Restaurant / Canteen  
- Internet Café  
- Printing Shop  
- Pharmacy  
- Tailoring Shop  
- Beauty Salon / Barbershop  
- Repair Shop  
- Family’s real business (allowed)  

The system logic remains the same; only the business context changes.

## System Objectives
Your system must:
- Allow employees to log in using Employee ID and PIN  
- Allow employees to Time In and Time Out on their own  
- Automatically compute:
  - Hours Worked  
  - Payroll (ETC = hours × rate)  
- Separate Employee Mode and Admin Mode  
- Generate attendance and payroll reports  
- Save reports to CSV files  

## Required Features (Strictly Required)

### 1. Login System
**Employee Login**
- Employee ID  
- PIN  

**Admin Login**
- Admin PIN (or admin credentials)

### 2. Employee Mode
Employees must be able to:
- Time In  
- Time Out  
- View their own:
  - Hours worked  
  - Salary (ETC)  

Employees must **NOT** see other employees’ data.

### 3. Admin Mode
Admin must be able to:
- Add employees  
- Set hourly rate  
- View employee list  
- View reports:
  - Daily Attendance  
  - Weekly Payroll Summary  
  - Monthly Payroll Summary  
- Export reports to CSV  

### 4. Timekeeping Logic
The system must correctly compute:
- Hours Worked = Time Out – Time In  
- ETC = Hours Worked × Hourly Rate  

Rules:
- Time Out must not work without Time In  
- Proper error handling is required  

### 5. File Handling (CSV)
Your system must generate:
- daily_report.csv  
- weekly_report.csv  
- monthly_report.csv  

Each file must contain:
- Employee ID  
- Employee Name  
- Date  
- Time In  
- Time Out  
- Hours Worked  
- ETC  

### 6. GUI Requirement
- Use Tkinter  
- Must be user-friendly  
- Buttons must be labeled clearly  
- Separate windows for:
  - Login  
  - Employee Panel  
  - Admin Panel  
  - Reports  

## Programming Requirements
Your system must use:
- Classes and Objects  
- At least one Custom Exception  
- File I/O (CSV)  
- Functions and Methods  
- Iteration (for reports)  
- Modular design (separate `.py` files)  

## Required Project Structure
project_folder/ <br>
├── models.py <br>
├── timelog.py <br>
├── manager.py <br>
├── gui_app.py <br>
├── app.py <br>
└── reports/ (optional)

## Sample Scenario
**Business:** Coffee Shop  
**Employee:** Juan Dela Cruz  
**Rate:** ₱60/hour  

**Time Record**
- Time In: 8:00 AM  
- Time Out: 5:00 PM  

**System Output**
- Hours Worked: 9.00  
- ETC: ₱540.00  

Data is saved automatically to CSV.
