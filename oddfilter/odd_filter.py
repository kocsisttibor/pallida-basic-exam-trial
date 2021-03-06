# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

# print(odd_filter([1, 2, 3, 4, 5]))  # should print [1, 3, 5]

def odd_filter(given_list):
    try:
        odd_list = []
        for i in given_list:
            if i % 2 != 0:
                odd_list.append(i)
        return odd_list
    except TypeError:
        print("The given parameter is not a list of numbers.")
        return -1

alma = ["majd", 2, 3]
odd_filter(alma)
