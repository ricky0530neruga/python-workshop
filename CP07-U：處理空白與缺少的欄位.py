expense1 = {
    "date": "2026-10-01",
    "category": "早餐",
    "amount": "85",
    "note": "   "
}

expense2 = {
    "date": "2026-10-02",
    "category": "交通",
    "amount": "120"
}

def clean_expense(expense):
    cleaned_expense = {
        "date": expense["date"].strip(),
        "category": expense["category"].strip(),
        "amount": float(expense["amount"]),
        "note": expense.get("note", "未填寫").strip() or "未填寫"
    }
    return cleaned_expense

print(clean_expense(expense1))
print(clean_expense(expense2))