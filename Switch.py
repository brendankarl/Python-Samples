#Use a dictionary to perform a switch
def monthswitch(value):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
        }
    print(months.get(value, "Invalid Month"))

#monthswitch(value)

#Use a dictionary that calls a function
def great():
    return "Great"

def good():
    return "Good"

def average():
    return "Average"

def bad():
    return "Bad"
 
switcher = {
        0: great,
        1: good,
        2: average,
        3: bad
    }
 
def ratingswitch(value):
    func = switcher.get(value)
    return func()

#ratingswitch(value)