raw_expenses = [
    {
        "date": " 2026-10-01 ",
        "category": "早餐",
        "amount": "85",
        "note": " 便利商店 ",
    },
    {
        "date": "2026-10-02",
        "category": "交通 ",
        "amount": "120",
        "note": "捷運",
    },
    {
        "date": "2026-10-03",
        "category": "日用品",
        "amount": " 350 ",
        "note": "洗衣精",
    },
    {
        "date": "2026-10-04",
        "category": "晚餐",
        "amount": "240",
        "note": "",
    },
    {
        "date": "2026-10-05",
        "category": "交通",
        "amount": "60",
    },
]

def clean_expense(expense):   #清洗單筆資料
    return {
        "date": expense["date"].strip(),
        "category": expense["category"].strip(),
        "amount": float(expense["amount"].strip()),
        "note": expense.get("note", "未填寫").strip() or "未填寫"


    }
def validate_expense(expense):  #驗證每個key是否=="" 否則 return True
    if (
        expense["date"].strip() == ""
        or expense["category"].strip() == ""
        or expense["amount"] <= 0
        or expense["note"].strip() == ""
    ):
        return False
    else:
        return True

def clean_expenses(raw_expenses):
    cleaned_list = [] #把cleaned_list 作為清單建立

    for expense in raw_expenses:  #把expense從raw_expenses 一筆一筆弄出來  
        cleaned_list.append(clean_expense(expense)) #把clean_expense(expense) 的結果放進cleaned_list這個list 裡面

    return cleaned_list #把cleaned_list 回傳出去

expenses = clean_expenses(raw_expenses) #把clean_expenses(raw_expenses)=逐筆清洗的韓式的結果放進expenses=已經清洗乾淨的list 裡面

def calculate_total(expenses): #計算全部支出

    return sum(expense["amount"] for expense in expenses) #回傳sum amount計算總花費

def calculate_average(expenses): #計算平均

    total = calculate_total(expenses)
    average = total / len(expenses)

    return average

def calculate_max(expenses): #找出最大值

    expensemost_list = [] #弄成一個list max不譨直接作用dictionary

    for expense in expenses: #for回圈 
        expensemost_list.append(expense["amount"]) #把每筆的amount加入到上面那list裡
    return max(expensemost_list) #回傳那個list裡最max的


def calculate_min(expenses): #找最小 跟上面那個依樣
    if len(expenses) == 0:
        return 0
    
    expensemin_list = []

    for expense in expenses:
        expensemin_list.append(expense["amount"])
    return min(expensemin_list)


def get_amount(expense): #sorted排序
    return expense["amount"] 

sorted_expenses = sorted(expenses, key=get_amount, reverse=True) #在expenses裡 找get_amount回傳的=amount 把它true（大到小）排序 


def print_report(expenses, budget):
    
    print("------家庭月度支出------")
    
    total = calculate_total(expenses)  #定義變數
    average = calculate_average(expenses)
    maximum = calculate_max(expenses)
    minimum = calculate_min(expenses)
    count = len(expenses)

    remaining = budget - total
    usage_rate = total / budget

    sorted_expenses = sorted(expenses, key=get_amount, reverse=True) #先sort排序
    for index, expense in enumerate(sorted_expenses, start=1): #用enumetare 排出序列
        print(f"{index:02d}.{expense['category']:>8}：{expense['amount']:>8.2f} 元 佔比:{expense['amount']/budget:.1%} {expense['note']}")
    print(f"本月預算：{budget:.2f}元")
    print(f"支出筆數：{count} 筆")
    print(f"總支出：{total:,.2f} 元")
    print(f"平均支出：{average:.2f} 元")
    print(f"最高支出：{maximum:.2f} 元")
    print(f"最低支出：{minimum:.2f} 元")
    print(f"剩餘預算：{remaining:.2f} 元")
    print(f"預算使用率：{usage_rate:.1%}")
    if usage_rate >= 100:
        print(f"預算狀態：已超支")
    else:
        print(f"預算狀態：尚未超支")
    result = any(expense["amount"] >= 500 for expense in expenses) #有一項expense["amount"] >=500 就true
    print(f"是否有花費大於500?:{result}")
    valid = all(validate_expense(expense)  for expense in expenses) #全部的expense["amount"] >0 才true
    print(f"是否所有金額有效?：:{valid}")
    



budget = float(input("本月預算？")) #確認輸入預算>0 
if budget <= 0:
    print("預算必須大於 0")
else:
    print_report(expenses, budget)





 







    





    