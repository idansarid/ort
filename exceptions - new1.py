def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print("division by zero!")
    except Exception as e:
        raise e
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(3, 0)