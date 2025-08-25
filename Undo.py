# Create a stack for undo operations
undo_stack = []
# Undo the last action
def undo():
  last_action = undo_stack.pop()
  print(f"Undoing action: {last_action}")
  
while True:
    i = input('''
              1: Type stuff
              2: Undo must recent action
              3: Exeunt
              ''')
    if i not in ["1", "2", "3"]:
        print("No")
    elif i == '1':
        text = input()
        words = " ".split(text)
        for item in words:
            undo_stack.append(item)
    elif i == "2":
        if undo_stack != []:
          undo()
    elif i == "3":
        break