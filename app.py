# app.py
import customtkinter as ctk
from tkinter import ttk, messagebox
from database import Database

# --- App Class ---
class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        
        # --- App Setup ---
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        
        # --- Theme and Appearance ---
        ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
        ctk.set_default_color_theme("blue") # Options: "blue", "green", "dark-blue"

        # --- Database ---
        self.db = Database('pythontut.db')

        # --- Layout ---
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')
        self.rowconfigure(0, weight=1)

        # --- Widgets ---
        self.create_widgets()
        self.populate_list()

    def create_widgets(self):
        # --- Input Frame (Left Side) ---
        input_frame = ctk.CTkFrame(self)
        input_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Title Label
        title_label = ctk.CTkLabel(input_frame, text="Contact Details", font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=(10, 20))

        # Input Fields and Labels
        self.name_entry = self.create_entry(input_frame, "Name:")
        self.phone_entry = self.create_entry(input_frame, "Phone:")
        self.email_entry = self.create_entry(input_frame, "Email:")
        self.address_entry = self.create_entry(input_frame, "Address:")
        
        # --- Button Frame ---
        button_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        button_frame.pack(pady=20, fill="x", expand=True)
        button_frame.columnconfigure((0, 1), weight=1)

        # Buttons
        ctk.CTkButton(button_frame, text="Add Contact", command=self.add_contact).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(button_frame, text="Update Contact", command=self.update_contact).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(button_frame, text="Delete Contact", command=self.delete_contact, fg_color="#D32F2F", hover_color="#B71C1C").grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(button_frame, text="Clear Fields", command=self.clear_fields, fg_color="#757575", hover_color="#616161").grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # --- Tree Frame (Right Side) ---
        tree_frame = ctk.CTkFrame(self)
        tree_frame.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="nsew")

        # Search Bar
        search_entry = ctk.CTkEntry(tree_frame, placeholder_text="Search...")
        search_entry.pack(padx=10, pady=10, fill="x")
        search_entry.bind("<KeyRelease>", lambda event: self.search_contacts(search_entry.get()))

        # --- Treeview ---
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#2a2d2e", foreground="white", fieldbackground="#2a2d2e", borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading", background="#565b5e", foreground="white", font=('Calibri', 10, 'bold'))
        
        self.tree = ttk.Treeview(tree_frame, columns=('ID', 'Name', 'Phone', 'Email', 'Address'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Phone', text='Phone')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Address', text='Address')

        # Set column widths
        self.tree.column('ID', width=30, stretch=False, anchor="center")
        self.tree.column('Name', width=120)
        self.tree.column('Phone', width=100)
        self.tree.column('Email', width=150)
        self.tree.column('Address', width=150)
        
        self.tree.pack(expand=True, fill='both', padx=10, pady=(0, 10))
        self.tree.bind('<<TreeviewSelect>>', self.select_item)

    def create_entry(self, parent, label_text):
        """Helper function to create a labeled entry widget"""
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill='x', padx=20, pady=7)
        label = ctk.CTkLabel(frame, text=label_text, width=70, anchor="w")
        label.pack(side="left")
        entry = ctk.CTkEntry(frame)
        entry.pack(side="left", expand=True, fill='x')
        return entry

    # --- UI Functions ---
    def populate_list(self, contacts=None):
        # Clear the existing list first
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Use provided contacts or fetch all
        contact_list = contacts if contacts is not None else self.db.fetch_all()
        
        # Insert contacts into the treeview
        for contact in contact_list:
            self.tree.insert('', 'end', values=contact)

    def select_item(self, event=None):
        try:
            selected_item = self.tree.selection()[0]
            contact = self.tree.item(selected_item)['values']
            
            self.clear_fields()
            
            self.name_entry.insert(0, contact[1])
            self.phone_entry.insert(0, contact[2])
            self.email_entry.insert(0, contact[3])
            self.address_entry.insert(0, contact[4])
        except IndexError:
            pass # Ignore if nothing is selected

    def clear_fields(self):
        self.name_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')

    # --- CRUD Functions ---
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name == '' or phone == '':
            messagebox.showerror("Required Fields", "Name and Phone fields are required.")
            return
        
        self.db.insert(name, phone, self.email_entry.get(), self.address_entry.get())
        self.clear_fields()
        self.populate_list()
        messagebox.showinfo("Success", "Contact added successfully.")
        
    def update_contact(self):
        try:
            selected_item = self.tree.selection()[0]
            contact_id = self.tree.item(selected_item)['values'][0]
        except IndexError:
            messagebox.showerror("Selection Error", "Please select a contact to update.")
            return

        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name == '' or phone == '':
            messagebox.showerror("Required Fields", "Name and Phone fields are required.")
            return
            
        self.db.update(contact_id, name, phone, self.email_entry.get(), self.address_entry.get())
        self.populate_list()
        messagebox.showinfo("Success", "Contact updated successfully.")

    def delete_contact(self):
        try:
            selected_item = self.tree.selection()[0]
            contact_id = self.tree.item(selected_item)['values'][0]
        except IndexError:
            messagebox.showerror("Selection Error", "Please select a contact to delete.")
            return
            
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?"):
            self.db.remove(contact_id)
            self.clear_fields()
            self.populate_list()
            messagebox.showinfo("Success", "Contact deleted successfully.")

    def search_contacts(self, query):
        results = self.db.search(query)
        self.populate_list(results)


# --- Main Execution ---
if __name__ == "__main__":
    app = App("Contact Management System", (1000, 600))
    app.mainloop()