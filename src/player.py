# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.items = []
    self.inventory = []

  def get_items(self, item_name):
    for item in self.inventory:
      if item.name == item.name:
        return item
    return None
  
  def add_item(self, item):
    self.items.append(item)
    return self.items

  def del_item(self, item):
    self.items.remove(item)
    return self.items
  
  def __str__(self):
    return f"Welcome! {self.name} {self.current_room} {self.inventory}"