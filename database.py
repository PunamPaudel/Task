

def get_data():
    data = [
        {
            "SN": 1,
            "Name": "Punam",
            "Email": "pnu.paudel@abc.com",
            "Phone": 9804111109,
            "Marks": "79.25"
        },

        {
            "SN": 2,
            "Name": "Ram",
            "Email": "ram@abc.com",
            "Phone": 9876411109,
            "Marks": "80.5"
        },

        {
            "SN": 3,
            "Name": "Geeta",
            "Email": "xyz@abc.com",
            "Phone": 9876411189,
            "Marks": "90.5"
        }

    ]
    return data


def write_to_txt():
    data = get_data()

    with open("students.txt", "w") as file:

        file.write(
            f"{'SN':<5}{'Name':<10}{'Email':<25}{'Phone':<15}{'Marks':<10}\n")
        file.write("-" * 70 + "\n")

        for row in data:
            file.write(
                f"{row['SN']:<5}"
                f"{row['Name']:<10}"
                f"{row['Email']:<25}"
                f"{row['Phone']:<15}"
                f"{row['Marks']:<10}\n"
            )

    print(" Data successfully written to students.txt")


# Run the program
if __name__ == "__main__":
    write_to_txt()
