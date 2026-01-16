"""
Manager Module - Handles employee management and report generation
"""
import csv
import os
from datetime import datetime, timedelta
from models import Employee, Admin, EmployeeNotFoundError, InvalidCredentialsError
from timelog import TimeLog

class SystemManager:
    """Main system manager for the payroll system"""
    
    def __init__(self):
        self.employees = {}
        self.admin = Admin()
        self.time_logs = []
        self.active_sessions = {}  # Track active employee sessions
        # No default data - empty employee list
    
    def verify_employee_login(self, emp_id, pin):
        """Verify employee credentials"""
        if emp_id not in self.employees:
            raise EmployeeNotFoundError("Employee ID not found!")
        
        if self.employees[emp_id].pin != pin:
            raise InvalidCredentialsError("Invalid PIN!")
        
        return self.employees[emp_id]
    
    def verify_admin_login(self, pin):
        """Verify admin credentials"""
        if not self.admin.verify_pin(pin):
            raise InvalidCredentialsError("Invalid Admin PIN!")
        return True
    
    def add_employee(self, emp_id, name, pin, hourly_rate):
        """Add a new employee"""
        if emp_id in self.employees:
            return False, "Employee ID already exists!"
        
        new_emp = Employee(emp_id, name, pin, hourly_rate)
        self.employees[emp_id] = new_emp
        return True, "Employee added successfully!"
    
    def time_in_employee(self, emp_id):
        """Record employee time in"""
        if emp_id in self.active_sessions:
            return False, "You are already timed in!"
        
        emp = self.employees[emp_id]
        time_log = TimeLog(emp.emp_id, emp.name, emp.hourly_rate)
        time_in_str = time_log.record_time_in()
        
        self.active_sessions[emp_id] = time_log
        
        return True, f"Time In recorded at {time_in_str}"
    
    def time_out_employee(self, emp_id):
        """Record employee time out"""
        if emp_id not in self.active_sessions:
            return False, "You must time in first!"
        
        time_log = self.active_sessions[emp_id]
        time_out_str = time_log.record_time_out()
        
        # Save to time logs
        self.time_logs.append(time_log)
        
        # Remove from active sessions
        del self.active_sessions[emp_id]
        
        # Save to daily report
        self.save_daily_report(time_log)
        
        summary = time_log.get_summary()
        return True, (f"Time Out recorded at {time_out_str}\n"
                     f"Hours Worked: {summary['hours_worked']:.2f} hours\n"
                     f"ETC: ₱{summary['etc']:.2f}")
    
    def get_employee_summary(self, emp_id):
        """Get current employee summary"""
        if emp_id in self.active_sessions:
            time_log = self.active_sessions[emp_id]
            summary = time_log.get_summary()
            return (f"Current Status: Timed In\n"
                   f"Time In: {summary['time_in']}\n"
                   f"Hourly Rate: ₱{summary['hourly_rate']:.2f}/hr")
        else:
            emp = self.employees[emp_id]
            return (f"Current Status: Not Timed In\n"
                   f"Hourly Rate: ₱{emp.hourly_rate:.2f}/hr")
    
    def get_all_employees(self):
        """Get list of all employees"""
        return list(self.employees.values())
    
    def save_daily_report(self, time_log):
        """Save individual time log to daily report"""
        filename = "daily_report.csv"
        file_exists = os.path.isfile(filename)
        
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['Employee ID', 'Employee Name', 'Date', 
                               'Time In', 'Time Out', 'Hours Worked', 'ETC'])
            writer.writerow(time_log.to_csv_row())
    
    def generate_weekly_report(self):
        """Generate weekly payroll report"""
        if not self.time_logs:
            return False, "No time logs available!"
        
        filename = "weekly_report.csv"
        
        # Get logs from last 7 days
        today = datetime.now()
        week_ago = today - timedelta(days=7)
        
        weekly_logs = [log for log in self.time_logs 
                      if datetime.strptime(log.date, "%Y-%m-%d") >= week_ago]
        
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Employee ID', 'Employee Name', 'Date', 
                           'Time In', 'Time Out', 'Hours Worked', 'ETC'])
            
            for log in weekly_logs:
                writer.writerow(log.to_csv_row())
        
        return True, f"Weekly report saved to {filename}"
    
    def generate_monthly_report(self):
        """Generate monthly payroll report"""
        if not self.time_logs:
            return False, "No time logs available!"
        
        filename = "monthly_report.csv"
        
        # Get logs from last 30 days
        today = datetime.now()
        month_ago = today - timedelta(days=30)
        
        monthly_logs = [log for log in self.time_logs 
                       if datetime.strptime(log.date, "%Y-%m-%d") >= month_ago]
        
        # Calculate totals per employee
        employee_totals = {}
        for log in monthly_logs:
            if log.emp_id not in employee_totals:
                employee_totals[log.emp_id] = {
                    'name': log.emp_name,
                    'total_hours': 0,
                    'total_etc': 0,
                    'days_worked': 0
                }
            employee_totals[log.emp_id]['total_hours'] += log.hours_worked
            employee_totals[log.emp_id]['total_etc'] += log.etc
            employee_totals[log.emp_id]['days_worked'] += 1
        
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Employee ID', 'Employee Name', 'Days Worked',
                           'Total Hours', 'Total ETC'])
            
            for emp_id, data in employee_totals.items():
                writer.writerow([
                    emp_id,
                    data['name'],
                    data['days_worked'],
                    round(data['total_hours'], 2),
                    round(data['total_etc'], 2)
                ])
        
        return True, f"Monthly report saved to {filename}"
    
    def get_daily_report_data(self):
        """Get daily report data for display"""
        if not os.path.isfile("daily_report.csv"):
            return []
        
        with open("daily_report.csv", 'r') as f:
            reader = csv.reader(f)
            return list(reader)