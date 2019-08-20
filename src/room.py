# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items=None):
    self.name = name
    self.description = description
    self.items = []
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None

  def get_items(self):
    return self.items
  
  def add_item(self, item):
    return self.items.append(item)
  
  def del_item(self, item):
    return self.items.remove(item)

  def __str__(self):
    return f"Your current location is {self.name}. "
