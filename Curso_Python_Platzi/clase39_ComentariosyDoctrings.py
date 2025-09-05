def calculate_average(numbers):
    """
    Calculate the average of a list of numbers. 
    Args:
        numbers (list): A list of int or float numbers.
    Returns:
        float: The average of the numbers in the list.
    """
    total = sum(numbers)
    average = total / len(numbers)
    return average      

#printing the result of the function
print(calculate_average([1,2,3,4,5,]))