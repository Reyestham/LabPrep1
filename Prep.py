import math
def main():
    print("display_main_menu")
    arr = get_user_input()
    print(arr)
    avg = calc_average_temperature(arr)
    print(avg)
    maximum, minimum = calc_min_max_temperature(arr)
    print(f'The max of arr is {maximum} and the min of arr is {minimum}')

def get_user_input():
    x = input("please enter numbers with commas in between them: ")
    y = x.split(',')
    arr = []
    for i in range(len(y)):
        floatx = float(y[i])
        arr.append(floatx)
    return arr

def calc_average_temperature(temp):
    sum = 0
    for i in range(len(temp)):
        sum = sum+temp[i]
    average = sum/(len(temp))
    return average

def calc_min_max_temperature(arr):
    maxi = max(arr)
    mini = min(arr)
    return maxi,mini

if __name__ == "__main__":
    main()