# from database import get_data
# from engine import get_details_about_email


# class UserInput:
#     def get_user_input():
#         try:
#             user_email = input("Enter your gmail to check ur marks: ")
#             return user_email

#         except Exception as e:
#             print("Input Error:", e)
#             return None

#     if __name__ == "__main__":
#         user_email = get_user_input()
#         all_user_data = get_data()
#         user_details = get_details_about_email(user_email, all_user_data)
#         print(user_details)

from database import get_data, get_database_name
from engine import EmailFinder, get_name


class UserInput:
    @staticmethod
    def get_user_input():
        try:
            user_email = input("Enter your gmail to check your marks: ")
            return user_email
        except Exception as e:
            print("Input Error:", e)
            return None


if __name__ == "__main__":
    user_email = UserInput.get_user_input()
    all_user_data = get_data()

    finder = EmailFinder(all_user_data)   # create object
    user_details = finder.get_details_about_email(user_email)  # call method

    print(user_details)
