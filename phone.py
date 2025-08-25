book = {}

while True:
  i = input('''
            1: Add contact
            2: Find contact
            3: Remove contact
            4: Exeunt
            
            ''')
  if i not in ["1", '2', '3', '4']:
      print("No")
  elif i == '1':
      n = input("Name: ")
      num = input("Phone Number: ")
      book[n] = num
  elif i =='2':
      n = input("Name: ")
      print(book[n])
  elif i == '3':
      n = input("Name: ")
      del book[n]
  elif i == '4':
      break