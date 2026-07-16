try: 
    x = int(input("Enter value for x : "))
    ans = 10/x
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print(ans)
finally:
    print("COde block executed")