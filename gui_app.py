"""
GUI Application Module - Tkinter Interface
"""
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from manager import SystemManager
from models import InvalidCredentialsError, EmployeeNotFoundError

class TimekeepingGUI:
    """Main GUI Application"""
    
    def __init__(self):
        self.manager = SystemManager()
        self.current_user = None
        self.root = tk.Tk()
        self.root.title("Coffee Shop - Timekeeping & Payroll System")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.show_login_screen()
    
    def clear_window(self):
        """Clear all widgets from window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_login_screen(self):
        """Display login screen"""
        self.clear_window()
        self.root.title("Login - Coffee Shop Timekeeping System")
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(expand=True, fill='both')
        
        # Title
        title_label = ttk.Label(main_frame, text="☕ Coffee Shop Timekeeping System", 
                               font=('Arial', 16, 'bold'))
        title_label.pack(pady=20)
        
        # Login type selection
        login_frame = ttk.LabelFrame(main_frame, text="Select Login Type", padding="20")
        login_frame.pack(pady=20, padx=20, fill='x')
        
        ttk.Button(login_frame, text="Employee Login", 
                  command=self.show_employee_login, width=20).pack(pady=5)
        ttk.Button(login_frame, text="Admin Login", 
                  command=self.show_admin_login, width=20).pack(pady=5)
        
        # Info
        info_label = ttk.Label(main_frame, 
                              text="Default Admin PIN: admin123\nAdd employees through Admin Panel first",
                              font=('Arial', 9), foreground='gray')
        info_label.pack(pady=20)
    
    def show_employee_login(self):
        """Display employee login form"""
        self.clear_window()
        self.root.title("Employee Login")
        
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(expand=True, fill='both')
        
        ttk.Label(main_frame, text="Employee Login", 
                 font=('Arial', 16, 'bold')).pack(pady=20)
        
        # Form frame
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(pady=20)
        
        ttk.Label(form_frame, text="Employee ID:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        emp_id_entry = ttk.Entry(form_frame, width=25)
        emp_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="PIN:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        pin_entry = ttk.Entry(form_frame, width=25, show='*')
        pin_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=20)
        
        def login():
            emp_id = emp_id_entry.get().strip()
            pin = pin_entry.get().strip()
            
            if not emp_id or not pin:
                messagebox.showerror("Error", "Please fill all fields!")
                return
            
            try:
                employee = self.manager.verify_employee_login(emp_id, pin)
                self.current_user = employee
                self.show_employee_panel()
            except (EmployeeNotFoundError, InvalidCredentialsError) as e:
                messagebox.showerror("Login Failed", str(e))
        
        ttk.Button(btn_frame, text="Login", command=login, width=15).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Back", command=self.show_login_screen, width=15).pack(side='left', padx=5)
    
    def show_admin_login(self):
        """Display admin login form"""
        self.clear_window()
        self.root.title("Admin Login")
        
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(expand=True, fill='both')
        
        ttk.Label(main_frame, text="Admin Login", 
                 font=('Arial', 16, 'bold')).pack(pady=20)
        
        # Form frame
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(pady=20)
        
        ttk.Label(form_frame, text="Admin PIN:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        pin_entry = ttk.Entry(form_frame, width=25, show='*')
        pin_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=20)
        
        def login():
            pin = pin_entry.get().strip()
            
            if not pin:
                messagebox.showerror("Error", "Please enter PIN!")
                return
            
            try:
                self.manager.verify_admin_login(pin)
                self.show_admin_panel()
            except InvalidCredentialsError as e:
                messagebox.showerror("Login Failed", str(e))
        
        ttk.Button(btn_frame, text="Login", command=login, width=15).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Back", command=self.show_login_screen, width=15).pack(side='left', padx=5)
    
    def show_employee_panel(self):
        """Display employee control panel"""
        self.clear_window()
        self.root.title(f"Employee Panel - {self.current_user.name}")
        
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(expand=True, fill='both')
        
        ttk.Label(main_frame, text=f"Welcome, {self.current_user.name}!", 
                 font=('Arial', 16, 'bold')).pack(pady=10)
        
        ttk.Label(main_frame, text=f"Employee ID: {self.current_user.emp_id}",
                 font=('Arial', 10)).pack()
        
        # Summary frame
        summary_frame = ttk.LabelFrame(main_frame, text="Your Status", padding="15")
        summary_frame.pack(pady=20, padx=20, fill='x')
        
        summary_text = tk.Text(summary_frame, height=4, width=40, wrap='word')
        summary_text.pack()
        summary_text.insert('1.0', self.manager.get_employee_summary(self.current_user.emp_id))
        summary_text.config(state='disabled')
        
        # Action buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=20)
        
        def time_in():
            success, message = self.manager.time_in_employee(self.current_user.emp_id)
            if success:
                messagebox.showinfo("Success", message)
                self.show_employee_panel()  # Refresh
            else:
                messagebox.showerror("Error", message)
        
        def time_out():
            success, message = self.manager.time_out_employee(self.current_user.emp_id)
            if success:
                result = messagebox.showinfo("Success", message + "\n\nThank you for your work today!")
                # After time out, ask if they want to logout or stay
                logout_choice = messagebox.askyesno("Logout?", "Do you want to logout and return to main login screen?")
                if logout_choice:
                    self.show_login_screen()
                else:
                    self.show_employee_panel()  # Refresh and stay
            else:
                messagebox.showerror("Error", message)
        
        ttk.Button(btn_frame, text="Time In", command=time_in, width=15).pack(pady=5)
        ttk.Button(btn_frame, text="Time Out", command=time_out, width=15).pack(pady=5)
        ttk.Button(btn_frame, text="Logout", command=self.show_login_screen, width=15).pack(pady=5)
    
    def show_admin_panel(self):
        """Display admin control panel"""
        self.clear_window()
        self.root.title("Admin Panel")
        
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(expand=True, fill='both')
        
        ttk.Label(main_frame, text="Admin Panel", 
                 font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Button frame
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=20)
        
        ttk.Button(btn_frame, text="Add Employee", 
                  command=self.show_add_employee, width=25).pack(pady=5)
        ttk.Button(btn_frame, text="View Employees", 
                  command=self.show_employee_list, width=25).pack(pady=5)
        ttk.Button(btn_frame, text="View Daily Report", 
                  command=self.show_daily_report, width=25).pack(pady=5)
        ttk.Button(btn_frame, text="Generate Weekly Report", 
                  command=self.generate_weekly_report, width=25).pack(pady=5)
        ttk.Button(btn_frame, text="Generate Monthly Report", 
                  command=self.generate_monthly_report, width=25).pack(pady=5)
        ttk.Button(btn_frame, text="Logout", 
                  command=self.show_login_screen, width=25).pack(pady=15)
    
    def show_add_employee(self):
        """Display add employee form"""
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Employee")
        add_window.geometry("400x300")
        add_window.resizable(False, False)
        
        main_frame = ttk.Frame(add_window, padding="20")
        main_frame.pack(expand=True, fill='both')
        
        ttk.Label(main_frame, text="Add New Employee", 
                 font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Form
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(pady=10)
        
        ttk.Label(form_frame, text="Employee ID:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        emp_id_entry = ttk.Entry(form_frame, width=20)
        emp_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        name_entry = ttk.Entry(form_frame, width=20)
        name_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="PIN:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        pin_entry = ttk.Entry(form_frame, width=20, show='*')
        pin_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="Hourly Rate (₱):").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        rate_entry = ttk.Entry(form_frame, width=20)
        rate_entry.grid(row=3, column=1, padx=5, pady=5)
        
        def add():
            emp_id = emp_id_entry.get().strip()
            name = name_entry.get().strip()
            pin = pin_entry.get().strip()
            rate = rate_entry.get().strip()
            
            if not all([emp_id, name, pin, rate]):
                messagebox.showerror("Error", "Please fill all fields!")
                return
            
            try:
                rate_float = float(rate)
                success, message = self.manager.add_employee(emp_id, name, pin, rate_float)
                if success:
                    messagebox.showinfo("Success", message)
                    add_window.destroy()
                else:
                    messagebox.showerror("Error", message)
            except ValueError:
                messagebox.showerror("Error", "Invalid hourly rate!")
        
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=20)
        
        ttk.Button(btn_frame, text="Add Employee", command=add, width=15).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Cancel", command=add_window.destroy, width=15).pack(side='left', padx=5)
    
    def show_employee_list(self):
        """Display list of all employees"""
        list_window = tk.Toplevel(self.root)
        list_window.title("Employee List")
        list_window.geometry("600x400")
        
        main_frame = ttk.Frame(list_window, padding="20")
        main_frame.pack(expand=True, fill='both')
        
        ttk.Label(main_frame, text="Employee List", 
                 font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Create treeview
        tree_frame = ttk.Frame(main_frame)
        tree_frame.pack(expand=True, fill='both')
        
        tree = ttk.Treeview(tree_frame, columns=('ID', 'Name', 'Rate'), show='headings')
        tree.heading('ID', text='Employee ID')
        tree.heading('Name', text='Name')
        tree.heading('Rate', text='Hourly Rate')
        
        tree.column('ID', width=100)
        tree.column('Name', width=200)
        tree.column('Rate', width=100)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', expand=True, fill='both')
        scrollbar.pack(side='right', fill='y')
        
        # Populate data
        for emp in self.manager.get_all_employees():
            tree.insert('', 'end', values=(emp.emp_id, emp.name, f"₱{emp.hourly_rate:.2f}"))
        
        ttk.Button(main_frame, text="Close", command=list_window.destroy, width=15).pack(pady=10)
    
    def show_daily_report(self):
        """Display daily report"""
        report_window = tk.Toplevel(self.root)
        report_window.title("Daily Report")
        report_window.geometry("800x500")
        
        main_frame = ttk.Frame(report_window, padding="20")
        main_frame.pack(expand=True, fill='both')
        
        ttk.Label(main_frame, text="Daily Attendance Report", 
                 font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Text area with scrollbar
        text_frame = ttk.Frame(main_frame)
        text_frame.pack(expand=True, fill='both')
        
        text_area = scrolledtext.ScrolledText(text_frame, wrap='word', width=90, height=20)
        text_area.pack(expand=True, fill='both')
        
        # Load data
        data = self.manager.get_daily_report_data()
        if data:
            for row in data:
                text_area.insert('end', ' | '.join(str(cell) for cell in row) + '\n')
        else:
            text_area.insert('end', 'No data available.')
        
        text_area.config(state='disabled')
        
        ttk.Button(main_frame, text="Close", command=report_window.destroy, width=15).pack(pady=10)
    
    def generate_weekly_report(self):
        """Generate weekly report"""
        success, message = self.manager.generate_weekly_report()
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
    
    def generate_monthly_report(self):
        """Generate monthly report"""
        success, message = self.manager.generate_monthly_report()
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
    
    def run(self):
        """Run the application"""
        self.root.mainloop()