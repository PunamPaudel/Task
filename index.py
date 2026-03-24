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
for row in data:
    if row["Email"] == "xyz@abc.com":
        print(row["Name"])
