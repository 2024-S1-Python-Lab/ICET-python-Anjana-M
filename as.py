my_dict = {'banana': 3, 'apple': 1, 'cherry':2, 'date': 4}
print("Original list:", my_dict
asorted_dict = dict(sorted(my_dict.items()))
print("Assending order:",sorted_dict)
dsorted_dict = dict(sorted(my_dict.items(), reverse=True))
print("Desending order:", dsorted_dict)
