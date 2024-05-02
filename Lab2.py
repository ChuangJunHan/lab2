def display_main_menu():
    print("Enter some numbers separated by commas e.g. 5, 67, 32)")

def get_user_input():
    numbers = input()
    listString = numbers.split(",")
    listFloat = list(map(float, listString))
    return listFloat

def calc_average(listFloat):
    average = (sum(listFloat)/len(listFloat))
    print("Average value = " + str(average))

def find_min_max(listFloat):
    minimum = min(listFloat)
    maximum = max(listFloat)
    print("Minimum value = " + str(minimum))
    print("Maximum value = " + str(maximum))
    
def sort_temperature(listFloat):
    listFloat.sort()
    print(listFloat)

def find_median(listFloat):
    listFloat.sort()
    n = len(listFloat)
    if n % 2 == 1:
        median = listFloat[n // 2]
    else:
        median = (listFloat[n // 2 - 1] + listFloat[n // 2]) / 2
    print("Median = " + str(median))

# Get user input once
display_main_menu()
user_input = get_user_input()

# Perform calculations
calc_average(user_input)
find_min_max(user_input)
sort_temperature(user_input)
find_median(user_input)