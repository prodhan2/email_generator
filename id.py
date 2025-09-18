import json
import csv

# ===== Load JSON files =====
with open("session.json") as f:
    session_data = json.load(f)

with open("hall.json") as f:
    hall_data = json.load(f)

with open("dept.json") as f:
    dept_data = json.load(f)

start_roll = 101
end_roll = 250

# ===== Prepare CSV file =====
csv_file = "university_emails.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Email", "Session", "Hall Code", "Hall Name", "Department Code", "Department Name"])
    
    total_count = 0
    
    # Loop through each department
    for dept in dept_data["departments"]:
        dept_code = dept["code"]
        dept_name = dept["name"]
        
        # Loop through each session
        for session in session_data["sessions"]:
            session_code = session["code"]
            session_year = session["year"]
            
            # Loop through each hall
            for hall in hall_data["halls"]:
                hall_code = hall["code"]
                hall_name = hall["name"]
                
                # Loop through roll numbers
                for roll_number in range(start_roll, end_roll + 1):
                    mail_id = f"s{int(session_code):02d}{int(hall_code):03d}{int(dept_code):02d}{roll_number:03d}"
                    email = f"{mail_id}@ru.ac.bd"
                    
                    writer.writerow([email, session_year, hall_code, hall_name, dept_code, dept_name])
                    total_count += 1

print(f"\nGenerated {total_count} emails for all sessions, halls, and departments.")
print(f"Saved in '{csv_file}'.")
