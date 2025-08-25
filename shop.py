shop_list = ["milk", "bread", "eggs"]
t = True
while t == True:
  i = input('''Hello user, please enter one of the following numbers for the respective functions:
            1: Add an item
            2: Remove an item
            3: View the list
            4: Exeunt
            ''')
  if i not in ['1', '2', '3', '4']:
      print("No")
  elif int(i) == 1:
      item = input("What item would you like to add? ")
      if item not in shop_list:
        shop_list.append(item)
      else:
         print("You already have it in the list")
  elif int(i) == 2:
      item = input("What item would you like to remove? ")
      if item in shop_list:
        shop_list.remove(item)
  elif int(i) == 3:
      print(shop_list)
  elif int(i) == 4:
      t = False
      print("bye")