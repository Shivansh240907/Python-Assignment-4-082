def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

interest = simple_interest(1000, 5, 2)
print("Simple Interest:", interest)
