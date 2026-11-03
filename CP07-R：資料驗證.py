expense = {
    "date": " ",
    "category": "早餐",
    "amount": 85.0,
    "note": "便利商店"
}

def validate_expense(expense):
    if expense["date"].strip() == "" or expense["category"].strip() == "" or expense["amount"] <= 0 or expense["note"].strip() == "":
        return False
    else:
        return True    

print(validate_expense(expense))