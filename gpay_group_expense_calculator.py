# Google Pay Group Expense Calculator

import json

# Replace with your Google Pay Expenses json file
googlePayJsonDataFileName = "group_expenses.json"


# Load Google Pay JSON data from file
with open(googlePayJsonDataFileName, "r") as file:

    data = json.load(file)


# Extract group names and members
split_group_expense_data = data["Group_expenses"]


# Dictionary to store total expenses of each member
total_expenses = {}


for split_Group in split_group_expense_data:

    split_Group_name = split_Group["group_name"]

    state_of_main_split = split_Group["state"]

    # Only consider groups with "COMPLETED" or "ONGOING" state. 
    if state_of_main_split in ["COMPLETED", "ONGOING"]:

        for item in split_Group["items"]:

            payer = item["payer"]

            amount = float(item["amount"].replace("\u20b9", "").replace(",", ""))  # Convert amount to float and remove commas

            if payer in total_expenses:

                if split_Group_name in total_expenses[payer]:

                    total_expenses[payer][split_Group_name] += amount

                else:

                    total_expenses[payer][split_Group_name] = amount

            else:

                total_expenses[payer] = {split_Group_name: amount}

# Print total expenses of each member with respective group name
print("Payer\t\t\t\tGroup Name\t\t\tTotal Expenses")

print("-" * 70)

for payer, expenses in total_expenses.items():

    for split_Group_name, total in expenses.items():

        print("{:<30} {:<30} {:<25}".format(payer, split_Group_name, total))

    print()
