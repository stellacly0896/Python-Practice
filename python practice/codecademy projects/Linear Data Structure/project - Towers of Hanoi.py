"""

Towers of Hanoi
Towers of Hanoi is an ancient mathematical puzzle that starts off with three stacks and many disks.


The objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack.

The game follows three rules:

Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
No disk may be placed on top of a smaller disk.
In this project, we are going to use our knowledge of stacks to implement this game! Let’s get started!

"""

from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))
for i in range(num_disks,0,-1):
  left_stack.push(i)

num_optimal_moves = 2 **num_disks - 1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))

#Get User Input, use the first letter to represent positions of the staks
def get_input():
  choices = [stack.get_name()[0].upper() for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print ("Enter {0} for {1}".format(letter,name))


    user_input = input("")
    #check if user_input is in choices
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]

#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()

    #check if the from_stack is empty
    if from_stack.get_size() == 0:
      print("\n\nInvalid Move. Try Again")
    #only in these two scenarios are the moves valid
    elif (to_stack.is_empty()) or (from_stack.peek() < to_stack.peek()):
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves +=1
      break
    #if the user tries to move a larger disk onto a smaller one
    else:
      print("\n\nInvalid Move. Try Again")

#end of the game
print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves,num_optimal_moves))
