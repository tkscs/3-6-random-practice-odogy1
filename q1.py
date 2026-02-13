import random

def spin_twister_spinner():
  """
  Returns a list with a random color, side, and appendage
  """
  colors = (["red", "green", "yellow", "blue"])
  sides = (["left" or "right"])
  appendage = (["hand", "foot"])
  
  print(random.choices(colors))
  print(random.choices(sides))
  print(random.choices(appendage))
  print("")



  #YOUR CODE HERE
  return

# Here's the function call. This should print a random assortment of twister commands
for i in range(10):
  spin_twister_spinner()

