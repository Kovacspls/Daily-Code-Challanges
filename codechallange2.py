'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array 
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], 
the expected output would be 
[120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], 
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division? 
'''
# def list_multiplier(input_list):
#   for nums in input_list:
#


input_list = [1, 2, 3, 4, 5, ]
output_list = []
random_list = [2, 5, 1, 7, 9]
output_numbers = []



def fun(input_value):
    product = 1

    for each_number in input_value: 
        product = 1

        for each_num in input_value:
            
            if each_num != each_number:
                product *= each_num
                if each_num == input_value[-1]:
                    output_numbers.append(product) 
            else:
                if each_num == input_value[-1]:
                    output_numbers.append(product)


fun(input_list)
print(output_numbers)