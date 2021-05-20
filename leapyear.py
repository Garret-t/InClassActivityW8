### HOW TO RUN ###
#In the file directory, run:
#python leap_year_no_error_handling.py
#or
#python3 leap_year_no_error_handling.py
#depending how you have python setup.
#Then enter in a year > 0 when prompted "Year: ".


def leap_year(user_in):
    if user_in % 4 == 0:
        if user_in % 100 == 0:
            if user_in % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    user_in = int(input("Year: "))
    print(leap_year(user_in))