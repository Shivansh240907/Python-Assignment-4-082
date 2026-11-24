x = 10

def update_value():
    global x
    x = 25
    print("Inside function:", x)

print("Before function call:", x)
update_value()
print("After function call:", x)
