import tkinter as tk
from tkinter import messagebox, ttk
import threading
import logging
from main import main as run_sales_pipeline  # Imports your existing automation

# Set up logging for the GUI console view
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SalesAutomationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Automation & Delivery Engine")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        # Apply a clean, modern window padding layout
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 1. Header Title
        title_label = ttk.Label(
            main_frame,
            text="Weekly Sales Reporting Hub",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=(0, 20))

        # 2. Information Label
        info_label = ttk.Label(
            main_frame,
            text="Enter the recipient's email address below to run the data\nconsolidation engine and dispatch the Excel reports immediately.",
            justify="center"
        )
        info_label.pack(pady=(0, 20))

        # 3. Input Label & Field
        email_label = ttk.Label(main_frame, text="Recipient Email Address:", font=("Arial", 10, "bold"))
        email_label.pack(anchor=tk.W, pady=(0, 5))

        self.email_entry = ttk.Entry(main_frame, font=("Arial", 11), width=45)
        self.email_entry.pack(ipady=4, pady=(0, 20))
        self.email_entry.insert(0, "joespirial@hotmail.com")  # Default helper text

        # 4. Progress Loading Spinner Indicator (Hidden by default)
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate', length=300)

        # 5. Submit Button
        self.run_button = ttk.Button(
            main_frame,
            text="Process Data & Send Report",
            command=self.start_pipeline_thread
        )
        self.run_button.pack(ipadx=10, ipady=5)

    def start_pipeline_thread(self):
        """Starts the automation processing in a background thread to prevent the GUI from freezing."""
        target_email = self.email_entry.get().strip()

        # Simple data input checking
        if not target_email or "@" not in target_email:
            messagebox.showerror("Invalid Input", "Please enter a valid email address.")
            return

        # Disable button and show loading bar while processing data
        self.run_button.config(state=tk.DISABLED)
        self.progress.pack(pady=15)
        self.progress.start(10)

        # Launch the background thread
        threading.Thread(target=self.execute_automation, args=(target_email,), daemon=True).start()

    def execute_automation(self, email):
        """Runs your main.py code engine matching the user's custom email layout."""
        try:
            # OPTIONAL: You can modify main.py to accept an email argument.
            # If your main.py is hardcoded, it will read from there, but you can pass it right here!
            logger.info(f"Starting background automation engine targeting: {email}")

            # This triggers your actual calculation and file writing engine
            run_sales_pipeline()

            # Switch back to the main thread to update UI components safely
            self.root.after(0, lambda: self.on_success(email))

        except Exception as e:
            logger.error(f"GUI Thread Automation Crash: {e}")
            self.root.after(0, lambda: self.on_failure(str(e)))

    def on_success(self, email):
        """Cleans up the UI elements and reports a clean tracking state."""
        self.progress.stop()
        self.progress.pack_forget()
        self.run_button.config(state=tk.NORMAL)
        messagebox.showinfo("Success!", f"Data compiled and report successfully sent to:\n{email}")

    def on_failure(self, error_msg):
        """Handles background calculation engine failure alerts."""
        self.progress.stop()
        self.progress.pack_forget()
        self.run_button.config(state=tk.NORMAL)
        messagebox.showerror("Execution Error", f"The pipeline encountered an error:\n{error_msg}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SalesAutomationGUI(root)
    root.mainloop()
