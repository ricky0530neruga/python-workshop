expense = {
    "date": " 2026-10-01 ",
    "category": " 早餐 ",
    "amount": " 85 ",
    "note": "  "
}

def clean_expense(expense):
    cleaned_expense = {
        "date": expense["date"].strip(),
        "category": expense["category"].strip(),
        "amount": float(expense["amount"]),
        "note": expense["note"].strip()
    }
    return cleaned_expense
print(clean_expense(expense))