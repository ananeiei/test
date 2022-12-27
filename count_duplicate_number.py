def count_duplicate_number (list_number):
  
  #Count the number of occurrences of each number
  list_number.sort()
  my_dict = {i:list_number.count(i) for i in list_number}
  
  # Print the count for each number
  for number, count in my_dict.items():
    print(f"{number}: {count}")



input_number = [2,3,4,6,2,4,4,1]
count_duplicate_number(input_number)
