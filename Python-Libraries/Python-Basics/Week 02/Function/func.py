def find_total(expence):
    """_summary_

    Args:
        expence (Integer): _description_

    Returns:
        total
    """
    total = 0
    for i in range(len(expence)):
        total += expence[i]
        # print(total)
    return total



expence_alamin = [10, 44, 233, 45]
expence_hello = [444, 223, 244, 23]
total = 0
for data in expence_alamin:
    total += data

print(total)
tot = find_total(expence_hello) 
print(tot)