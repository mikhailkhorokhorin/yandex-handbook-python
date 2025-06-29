try:
    func()
except Exception as exception:
    print(type(exception).__name__)
else:
    print("No Exceptions")