def value_contains(list,value):
	if value in list:
		result = True
	else: 
		result = False
	return result

print(value_contains(list((1,2,3)),3))