import csv
from database import get_data


class EmailFinder:
    def __init__(self, data: list):
        self.data = data

    def get_details_about_email(self, user_email):
        try:
            # First, check in self.data
            for row in self.data:
                if not isinstance(row, dict):
                    raise ValueError("Each row must be a dictionary")
                if row.get("Email") == user_email:
                    return row

            # If not found, check in CSV
            try:
                with open("students_pipe.csv", "r") as file:
                    reader = csv.DictReader(file, delimiter="|")
                    for row in reader:
                        if row.get("Email") == user_email:
                            return row
            except FileNotFoundError:
                pass

            # If not found anywhere
            return {"status": "Not Found", "message": f"No record found for email: {user_email}"}

        except Exception as e:
            return {"error": str(e)}


data = get_data()  # list of dicts from database
finder = EmailFinder(data)

email = input("Enter email to search: ")
result = finder.get_details_about_email(email)

print(result)
