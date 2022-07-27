import pandas as pd

# type annotation
def days_difference(day1: int, day2: int) -> int:
    return day1 - day2

if __name__ == "__main__":
    day1 = 3
    day2 = 'abc'

    print(days_difference(day1, day2))
