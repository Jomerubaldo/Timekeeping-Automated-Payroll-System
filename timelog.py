"""
Time Log Module - Handles time tracking logic
"""
from datetime import datetime
from models import TimeInNotFoundError

class TimeLog:
    """Class to handle time in/out records"""
    
    def __init__(self, emp_id, emp_name, hourly_rate):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.hourly_rate = hourly_rate
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.time_in = None
        self.time_out = None
        self.hours_worked = 0.0
        self.etc = 0.0
    
    def record_time_in(self):
        """Record time in"""
        self.time_in = datetime.now()
        return self.time_in.strftime("%I:%M %p")
    
    def record_time_out(self):
        """Record time out and calculate hours worked"""
        if self.time_in is None:
            raise TimeInNotFoundError("Cannot time out without timing in first!")
        
        self.time_out = datetime.now()
        
        # Calculate hours worked
        time_diff = self.time_out - self.time_in
        self.hours_worked = time_diff.total_seconds() / 3600
        
        # Calculate ETC (Estimated Time Compensation)
        self.etc = self.hours_worked * self.hourly_rate
        
        return self.time_out.strftime("%I:%M %p")
    
    def get_summary(self):
        """Get time log summary"""
        return {
            'emp_id': self.emp_id,
            'emp_name': self.emp_name,
            'date': self.date,
            'time_in': self.time_in.strftime("%I:%M %p") if self.time_in else "N/A",
            'time_out': self.time_out.strftime("%I:%M %p") if self.time_out else "N/A",
            'hours_worked': round(self.hours_worked, 2),
            'etc': round(self.etc, 2),
            'hourly_rate': self.hourly_rate
        }
    
    def to_csv_row(self):
        """Convert to CSV row format"""
        return [
            self.emp_id,
            self.emp_name,
            self.date,
            self.time_in.strftime("%I:%M %p") if self.time_in else "N/A",
            self.time_out.strftime("%I:%M %p") if self.time_out else "N/A",
            round(self.hours_worked, 2),
            round(self.etc, 2)
        ]