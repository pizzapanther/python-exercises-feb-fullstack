name = "paul"

if name == "paul":
  print('hello')
  

nums = [1, 2]

class MyError(Exception):
  pass

try:
  print(nums[6])
  
except IndexError:
  print(nums)
  print('!!!!number not found!!!!')
  
except ArithmeticError:
  print('oops')
  
except MyError:
  pass
  
# if len(nums) >= 7:
#   print(nums[6])
# else:
#   print('ERRRRRROR!!!!')
#   raise NameError('number not found')
  
print('The End')
  
# print(me)
