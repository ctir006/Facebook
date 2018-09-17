''' In order to win the prize for most cookies sold, my friend Alice and I are going to merge our 
Girl Scout Cookies orders and enter as one unit. Each order is represented by an "order id" (an integer).
We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of 
orders into one sorted list.
For example:

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print merge_lists(my_list, alices_list)

'''

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

result=[]
i=0;j=0

while i<len(my_list) and j<len(alices_list):
	if my_list[i]<alices_list[j]:
		result.append(my_list[i])
		i+=1
	else:
		result.append(alices_list[j])
		j+=1
while i<len(my_list):
	result.append(my_list[i])
	i+=1
while j<len(alices_list):
	result.append(alices_list[j])
	j+=1
print(result)
