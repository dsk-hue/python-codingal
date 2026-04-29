nums = (2, 5, 8, 5, 2, 9, 8, 1, 5)
number_w_count = {
    "mode" : 0,
    "number times": 0,
    "current times": 0,
}

for x in (1, 10):
    for j in nums:
        if x == j:
            number_w_count["current times"] += 1
    if number_w_count["current times"] > number_w_count["number times"]:
        number_w_count["mode"] = x
        number_w_count["number times"] = number_w_count["current times"]
    
print(f"The most common number is {number_w_count["mode"]}, which appears {number_w_count["number times"]} times.")   
    

