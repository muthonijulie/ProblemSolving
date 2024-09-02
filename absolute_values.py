def dist_abs_value(x):
    distinct_abs_value=set()
    for value in x:
        abs_value=abs(value)
        distinct_abs_value.add(abs_value)
    return len(distinct_abs_value),distinct_abs_value

x=[-5, -3, -1, 0, 1, 3, 6]
count,distinct_abs_value=dist_abs_value(x)

print("Count of distinct absolute values:", count)
print("Distinct absolute values:", distinct_abs_value)

