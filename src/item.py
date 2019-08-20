class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def on_take(self):
    print(f"You have picked up {self.name}")

  def on_drop(self):
    print(f"You have dropped {self.name}")
  
  def __str__(self):
    return f"Item in room a {self.name}"
    
# Sword is a sub class of Item and inherits from Item using super().
class Sword(Item):
  def __init__(self, name, description, category, durability):
    super().__init__(name, description)
    self.category = category
    self.durability = durability

