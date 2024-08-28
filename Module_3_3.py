def print_params(a = 1,b = 'Настасья',c = True):
    print(a,b,c)
    global values_list, values_list_2, values_dict
    values_list = [1000, "Napoli", 3.14]
    values_dict = {'a':'Зенит', 'b':"Спартак", 'c':"ЦСКА"}
    values_list_2 = ["Bavaria", False]


print_params()
print_params(b = 25, c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 666)