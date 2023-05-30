some_string = '123asmvb45mb0fs234djf'

count_numbers = sum(c.isdigit() for c in some_string)

print(count_numbers)


# num_list = []
# for i in some_string:
#     if i.isdigit():
#         num_list.append(int(i))
#
#
# result = len(num_list)
# print(result)