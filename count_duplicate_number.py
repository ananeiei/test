def count_duplicate_number (list_number):
  list_number.sort()
  my_dict = {i:list_number.count(i) for i in list_number}
  return my_dict


input_number = [2,3,4,6,2,4,4,1]
print(count_duplicate_number(input_number))