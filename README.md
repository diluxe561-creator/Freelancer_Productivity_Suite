# Freelancer_Productivity_Suite

A lightweight Python CLI tool for freelancers to manage business profiles, track client work, and generate professional PDF invoices.

---

## 🚀 FEATURES
- Business Profile: Store your business name, contact info, and address.
- Client Directory: Manage multiple clients with unique IDs.
- Work Logger: Track projects, task descriptions, hours, and rates.
- PDF Generation: Create professional invoices with automatic total calculations.
- Data Persistence: All data is saved locally to 'freelance_data.json'.

---

## 🛠️ INSTALLATION

1. Ensure you have Python installed.
2. Install the required PDF library:
   pip install fpdf

3. Save the script as 'freelance_suite.py' and run it:
   python freelance_suite.py

---

## 🖥️ HOW TO USE

1. [Update My Profile]: First-time setup for your business details.
2. [Add Client]: Register a client (e.g., ID: C1, Name: Acme Corp).
3. [Log Work]: Record hours worked for a specific client ID.
4. [Generate PDF Invoice]: Export a finished PDF for a client.
5. [Exit]: Save and close the application.

---

## 📁 FILE STRUCTURE

- freelance_suite.py   # The main application script
- freelance_data.json  # Auto-generated database (do not delete)
- Invoice_Name.pdf     # Generated invoices

---

## 📝 REQUIREMENTS
- Python 3.x
- fpdf library

---

Developed for streamlined freelance management.
