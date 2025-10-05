import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
import json
import os
from email_sender import send_email
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
EMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

TEMPLATES_FILE = "templates.json"

def load_templates():
    try:
        with open(TEMPLATES_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load templates: {e}")
        return {}

class SmartMailAutomatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SmartMail Automator")
        self.geometry("600x500")
        self.configure(bg="#f9f9f9")
        self.resizable(False, False)

        self.templates = load_templates()

        # Fonts
        self.title_font = Font(family="Segoe UI", size=18, weight="bold")
        self.tagline_font = Font(family="Segoe UI", size=11, slant="italic")
        self.label_font = Font(family="Segoe UI", size=11)
        self.entry_font = Font(family="Segoe UI", size=11)
        self.button_font = Font(family="Segoe UI", size=11, weight="bold")

        self.create_widgets()
        self.bind_shortcuts()

    def create_widgets(self):
        pad = {'padx': 15, 'pady': 10}
        # Header
        header_frame = tk.Frame(self, bg="#f9f9f9")
        header_frame.pack(fill=tk.X, **pad)
        tk.Label(header_frame, text="SmartMail Automator", bg="#f9f9f9", fg="#222", font=self.title_font).pack()
        tk.Label(header_frame, text="Automate your daily emails in one click", bg="#f9f9f9", fg="#666", font=self.tagline_font).pack()

        # Input Fields
        input_frame = tk.Frame(self, bg="#f9f9f9")
        input_frame.pack(fill=tk.X, **pad)

        tk.Label(input_frame, text="Recipient Email:", font=self.label_font, bg="#f9f9f9").grid(row=0, column=0, sticky="e")
        self.recipient_entry = tk.Entry(input_frame, font=self.entry_font, width=35)
        self.recipient_entry.grid(row=0, column=1, sticky="w")

        tk.Label(input_frame, text="Subject:", font=self.label_font, bg="#f9f9f9").grid(row=1, column=0, sticky="e")
        self.subject_entry = tk.Entry(input_frame, font=self.entry_font, width=35)
        self.subject_entry.grid(row=1, column=1, sticky="w")

        tk.Label(input_frame, text="Template:", font=self.label_font, bg="#f9f9f9").grid(row=2, column=0, sticky="e")
        self.template_var = tk.StringVar()
        self.template_dropdown = ttk.Combobox(input_frame, textvariable=self.template_var, width=33, state="readonly")
        self.template_dropdown["values"] = list(self.templates.keys())
        self.template_dropdown.grid(row=2, column=1, sticky="w")
        self.template_dropdown.bind("<<ComboboxSelected>>", self.on_template_select)

        # Body Editor
        body_frame = tk.Frame(self, bg="#f9f9f9")
        body_frame.pack(fill=tk.BOTH, expand=True, **pad)
        tk.Label(body_frame, text="Email Body:", font=self.label_font, bg="#f9f9f9").pack(anchor="w")
        self.body_text = tk.Text(body_frame, font=self.entry_font, height=12, width=60, wrap=tk.WORD, bd=1, relief=tk.SOLID)
        self.body_text.pack(fill=tk.BOTH, expand=True, pady=5)

        # Action Buttons
        button_frame = tk.Frame(self, bg="#f9f9f9")
        button_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=20)
        self.send_btn = tk.Button(button_frame, text="Send Email", font=self.button_font, bg="#28a745", fg="white", command=self.on_send)
        self.send_btn.pack(side=tk.LEFT, padx=(80,10), ipadx=10, ipady=5)
        self.clear_btn = tk.Button(button_frame, text="Clear All", font=self.button_font, bg="#28a745", fg="white", command=self.on_clear)
        self.clear_btn.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)
        self.exit_btn = tk.Button(button_frame, text="Exit", font=self.button_font, bg="#28a745", fg="white", command=self.quit)
        self.exit_btn.pack(side=tk.RIGHT, padx=(10,80), ipadx=10, ipady=5)

    def bind_shortcuts(self):
        self.bind('<Control-Return>', lambda e: self.on_send())
        self.bind('<Control-l>', lambda e: self.on_clear())

    def on_template_select(self, event=None):
        selected = self.template_var.get()
        template_body = self.templates.get(selected, "")
        self.body_text.delete("1.0", tk.END)
        self.body_text.insert(tk.END, template_body)

    def on_send(self):
        recipient = self.recipient_entry.get().strip()
        subject = self.subject_entry.get().strip()
        body = self.body_text.get("1.0", tk.END).strip()

        if not recipient or not subject or not body:
            messagebox.showwarning("Missing Fields", "Please fill in all fields before sending.")
            return
        if not EMAIL_ADDRESS or not APP_PASSWORD:
            messagebox.showerror("Config Error", "Gmail credentials not found in .env file.")
            return

        self.send_btn.config(state="disabled")
        self.send_btn.update()
        try:
            send_email(
                sender_email=EMAIL_ADDRESS,
                app_password=APP_PASSWORD,
                to_email=recipient,
                subject=subject,
                body=body
            )
            messagebox.showinfo("Success", "Email sent successfully!")
        except Exception as e:
            messagebox.showerror("Failure", f"Failed to send email:\n{e}")
        finally:
            self.send_btn.config(state="normal")

    def on_clear(self):
        self.recipient_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.template_dropdown.set("")
        self.body_text.delete("1.0", tk.END)

if __name__ == "__main__":
    app = SmartMailAutomatorApp()
    app.mainloop()