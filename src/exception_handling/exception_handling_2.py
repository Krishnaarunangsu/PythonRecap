import sys

try:
    a=1
    b=0
    c=1/0
except ArithmeticError as err:
    # print("OS error:", err)
    raise ZeroDivisionError("Cannot divide by zero") from err
except ValueError:
    print("Could not convert data to an integer.")
#except Exception as err:
    #print(f"Unexpected {err=}, {type(err)=}")
    #raise
finally:
    print("Jagannath")