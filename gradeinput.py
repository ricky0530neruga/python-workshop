scores = [85, 92, 76, 60, 95]

def calculate_average(scores):
    if not scores:
        return 0
    else:
        return sum(scores) / len(scores)
print(calculate_average([85, 92, 76, 60, 95]))
print(calculate_average([100, 80, 90]))
print(calculate_average([]))