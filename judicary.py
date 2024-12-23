import datetime

# CourtCase class to represent a case
class CourtCase:
    def __init__(self, cin, defendant_name, defendant_address, crime_type, crime_date, location, arresting_officer, arrest_date, hearing_date, judge_name, prosecutor_name, lawyer_name, start_date=None):
        self.cin = cin
        self.defendant_name = defendant_name
        self.defendant_address = defendant_address
        self.crime_type = crime_type
        self.crime_date = crime_date  # Date format: YYYY-MM-DD
        self.location = location
        self.arresting_officer = arresting_officer
        self.arrest_date = arrest_date
        self.hearing_date = hearing_date
        self.judge_name = judge_name
        self.prosecutor_name = prosecutor_name
        self.lawyer_name = lawyer_name
        self.status = "Pending"  # Pending, Adjourned, Completed
        self.judgment_summary = None
        self.adjournment_reason = None
        self.start_date = start_date  # Default value for start_date is None
        self.end_date = None

    def adjourn_case(self, reason, new_hearing_date):
        self.adjournment_reason = reason
        self.hearing_date = new_hearing_date
        self.status = "Adjourned"

    def complete_case(self, judgment_summary, completion_date):
        self.judgment_summary = judgment_summary
        self.status = "Completed"
        self.end_date = completion_date

    def __str__(self):
        return f"CIN: {self.cin} | Defendant: {self.defendant_name} | Crime: {self.crime_type} | Status: {self.status}"

# Judiciary Information System class to manage cases
class JudiciaryInformationSystem:
    def __init__(self):
        self.cases = []

    def add_case(self, case):
        self.cases.append(case)

    def query_case_status(self, cin):
        print(f"\nCase Status for CIN {cin}:")
        case = next((case for case in self.cases if case.cin == cin), None)
        if case:
            print(f"{case} | Hearing Date: {case.hearing_date} | Status: {case.status}")
            if case.status == "Completed":
                print(f"Judgment: {case.judgment_summary}")
            elif case.status == "Adjourned":
                print(f"Adjournment Reason: {case.adjournment_reason}")
        else:
            print("Case not found!")

# Main function to simulate the process
def main():
    jis = JudiciaryInformationSystem()

    # Registering two cases with IDs CIN001 and CIN002
    jis.add_case(CourtCase("CIN001", "John Doe", "123 Elm Street", "Theft", "2024-05-10", "Downtown", "Officer A", "2024-05-12", "2024-06-01", "Judge A", "Prosecutor X", "Lawyer 1", start_date=datetime.datetime(2024, 5, 10)))
    jis.add_case(CourtCase("CIN002", "Jane Smith", "456 Oak Street", "Arson", "2024-05-15", "Suburb", "Officer B", "2024-05-16", "2024-06-05", "Judge B", "Prosecutor Y", "Lawyer 2", start_date=datetime.datetime(2024, 5, 15)))

    # Prompting user to enter a case ID
    cin_input = input("Enter the case ID to query (e.g., CIN001 or CIN002): ").strip()

    # Query the case details by CIN
    jis.query_case_status(cin_input)

if __name__ == "__main__":
    main()
