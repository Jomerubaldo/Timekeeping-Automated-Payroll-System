"""
Models Module - Employee and Admin Classes
"""

class Employee:
    """Employee class to store employee information"""
    
    def __init__(self, emp_id, name, pin, hourly_rate=60.0):
        self.emp_id = emp_id
        self.name = name
        self.pin = pin
        self.hourly_rate = hourly_rate
        self.is_timed_in = False
        self.time_in = None
        self.time_out = None
    
    def __str__(self):
        return f"Employee(ID: {self.emp_id}, Name: {self.name}, Rate: ₱{self.hourly_rate}/hr)"
    
    def to_dict(self):
        """Convert employee to dictionary"""
        return {
            'emp_id': self.emp_id,
            'name': self.name,
            'pin': self.pin,
            'hourly_rate': self.hourly_rate
        }


class Admin:
    """Admin class for administrative access"""
    
    def __init__(self, admin_pin="admin123"):
        self.admin_pin = admin_pin
    
    def verify_pin(self, pin):
        """Verify admin PIN"""
        return pin == self.admin_pin


class TimeInNotFoundError(Exception):
    """Custom exception for when Time Out is attempted without Time In"""
    pass


class EmployeeNotFoundError(Exception):
    """Custom exception for when employee is not found"""
    pass


class InvalidCredentialsError(Exception):
    """Custom exception for invalid login credentials"""
    pass