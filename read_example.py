file_handle = open('hello.txt', 'r')

while True:
  c = file_handle.read(1)

  if c == '':
    break
    
  else:
    print(c, end='')
    
file_handle.close()