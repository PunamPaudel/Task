

# def get_details_about_email(user_email, all_data):
#     for row in all_data:
#         if row["Email"] == user_email:
#             return row
#     return {"status": "Not Found!"}

class EmailFinder:
    def __init__(self, data: list):
        self.data = data

    def get_details_about_email(self, user_email):
        try:
            if not isinstance(self.data, list):
                raise TypeError("Data should be a list of dictionaries")

            for row in self.data:
                if not isinstance(row, dict):
                    raise ValueError("Each row must be a dictionary")

                if row.get("Email") == user_email:
                    return row

            return {"status": "Not Found", "message": f"No record found for email: {user_email}"}

        except Exception as e:
            return {"error": str(e)}
