

def get_details_about_email(user_email, all_data):
    for row in all_data:
        if row["Email"] == user_email:
            return row
    return {"status": "Not Found!"}
