"""Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 

In other words, find the lowest positive integer that does not exist in the array. 

The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

placeholder_input = [3, 4, -1, 1]
placeholder_input_2 = [1, 2, 0]

def formatted_list(formatable_list):
	'''
	This function takes and arbitrary list, and creates a new list from it without negative numbers and 0
	At the end of the list the value of the counter variable appended

	'''
	formatted_list = []
	counter = 0
	for element in formatable_list:
		if element > 0 and element not in formatted_list:
			formatted_list.append(element)
		if element <= 0 or element in formatted_list:
			counter += 1

	my_val = sorted(formatted_list)
	my_val.append(counter)

	return my_val

	
def generated_lengthy_list(arbitrary_list):
	'''
	This function uses the previously formated list and list slicing to make a new list that contains positive number from 1 to max_num + 1 

	'''
	value = formatted_list(arbitrary_list)
	generated_sorted_list = []
	max_val = (len(value[:-1])+max(value[-1:]))
	for each_num in range(min(value[:-1]),max_val+1):
		generated_sorted_list.append(each_num)
	return generated_sorted_list

def problem_solver(a_list):
	'''
	This function takes a list, applies the formatted_list and generater_lenghty_list function to it 
	and then compare the indexed values of those lists

	'''
	index = 0
	list_1 = formatted_list(a_list)
	list_2 = generated_lengthy_list(a_list)
	for index in range(len(list_2)):
		if list_1[index]==list_2[index]:
			index +=1
		else:
			return list_2[index]
			break

print(generated_lengthy_list(placeholder_input))	
print(formatted_list(placeholder_input))
print(problem_solver(placeholder_input))