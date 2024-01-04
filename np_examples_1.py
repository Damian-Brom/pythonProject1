import numpy as np

my_list = [0,1,2,3,4] 
arr = np.array(my_list) # turning a list to an array 
first = arr[0]
last = arr[-1]
without_last = arr[:-1]
odd_values = arr[1::2]
last_three = arr[-3:] 
min = np.min(arr)
min_idx = np.argmin(arr) 

# So how does it all look like?
print(f"my_list =", my_list)
print(f"arr =", arr)
print(f"first arr element =", first)
print(f"last arr element =", last)
print(f"arr without last element =", without_last)
print(f"arr's odd_values only =", odd_values)
print(f"arr's last three elements =", last_three)
print(f"arr's min value =", min)
print(f"arr's min value's index =", min_idx)
