import json
import os
from fpdf import FPDF
from datetime import datetime

class FreelancerSuite:
    def __init__(self):
        self.db_file = "freelance_data.json"
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return {
            "me": {"name": "Enter Name", "email": "email@example.com", "address": "Your Address"},
            "clients": {},
            "logs": []
        }

    def save_data(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def update_profile(self):
        print("\n--- SET UP YOUR BUSINESS INFO ---")
        self.data['me']['name'] = input("Your Business Name: ")
        self.data['me']['email'] = input("Your Business Email: ")
        self.data['me']['address'] = input("Your Business Address: ")
        self.save_data()
        print("✔ Profile updated!")

    def add_client(self):
        print("\n--- ADD A NEW CLIENT ---")
        cid = input("Create a Client ID (e.g., C1): ")
        name = input("Client/Company Name: ")
        email = input("Client Email: ")
        self.data['clients'][cid] = {"name": name, "email": email}
        self.save_data()
        print(f"✔ Client {name} saved!")

    def log_work(self):
        if not self.data['clients']:
            print("❌ Add a client first!")
            return
        
        print("\n--- LOG WORK ---")
        for cid, info in self.data['clients'].items():
            print(f"ID: {cid} | Name: {info['name']}")
        
        cid = input("Enter Client ID for this work: ")
        if cid not in self.data['clients']:
            print("❌ Invalid Client ID.")
            return

        project = input("Project Name: ")
        task = input("Task Description: ")
        try:
            hours = float(input("Hours worked: "))
            rate = float(input("Hourly rate ($): "))
        except ValueError:
            print("❌ Please enter numbers for hours and rate.")
            return

        self.data['logs'].append({
            "client_id": cid,
            "project": project,
            "task": task,
            "hours": hours,
            "rate": rate,
            "total": hours * rate,
            "date": datetime.now().strftime("%Y-%m-%d")
        })
        self.save_data()
        print("✔ Work logged successfully!")

    def export_invoice_pdf(self):
        cid = input("\nWhich Client ID do you want to invoice? ")
        if cid not in self.data['clients']:
            print("❌ Client not found.")
            return

        client = self.data['clients'][cid]
        logs = [l for l in self.data['logs'] if l['client_id'] == cid]
        
        if not logs:
            print("❌ No work logged for this client.")
            return

        pdf = FPDF()
        pdf.add_page()
        
        # Header - Freelancer Info
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, self.data['me']['name'], ln=True)
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 5, self.data['me']['address'], ln=True)
        pdf.cell(0, 5, self.data['me']['email'], ln=True)
        pdf.ln(10)

        # Bill To
        pdf.set_font("Arial", 'B', 11)
        pdf.cell(0, 10, f"BILL TO: {client['name']} ({client['email']})", ln=True)
        pdf.ln(5)

        # Table Headers
        pdf.set_fill_color(200, 200, 200)
        pdf.cell(30, 10, "Date", 1, 0, 'C', True)
        pdf.cell(90, 10, "Task", 1, 0, 'C', True)
        pdf.cell(20, 10, "Hrs", 1, 0, 'C', True)
        pdf.cell(25, 10, "Rate", 1, 0, 'C', True)
        pdf.cell(25, 10, "Total", 1, 1, 'C', True)

        # Rows
        grand_total = 0
        pdf.set_font("Arial", size=10)
        for l in logs:
            pdf.cell(30, 10, l['date'], 1)
            pdf.cell(90, 10, f"{l['project']}: {l['task']}", 1)
            pdf.cell(20, 10, str(l['hours']), 1, 0, 'C')
            pdf.cell(25, 10, f"${l['rate']}", 1, 0, 'C')
            pdf.cell(25, 10, f"${l['total']}", 1, 1, 'C')
            grand_total += l['total']

        pdf.ln(5)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(165, 10, f"TOTAL DUE: ${grand_total:,.2f}", 0, 1, 'R')

        filename = f"Invoice_{client['name']}.pdf"
        pdf.output(filename)
        print(f"🚀 SUCCESS! Saved as {filename}")

def main():
    suite = FreelancerSuite()
    while True:
        print("\n--- FREELANCER SUITE MENU ---")
        print("1. Update My Profile")
        print("2. Add Client")
        print("3. Log Work")
        print("4. Generate PDF Invoice")
        print("5. Exit")
        
        choice = input("Select (1-5): ")
        if choice == '1': suite.update_profile()
        elif choice == '2': suite.add_client()
        elif choice == '3': suite.log_work()
        elif choice == '4': suite.export_invoice_pdf()
        elif choice == '5': break

if __name__ == "__main__":
    main()