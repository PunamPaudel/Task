from database import get_data
from engine import get_details_about_email


def get_user_input():
    user_email = input("Enter your gmail to check ur marks: ")
    return user_email


if __name__ == "__main__":
    user_email = get_user_input()
    all_user_data = get_data()
    user_details = get_details_about_email(user_email, all_user_data)
    print(user_details)
