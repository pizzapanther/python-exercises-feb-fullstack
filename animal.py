class Animal:
  def __init__ (self, name):
    self.name = name
    
class Dog (Animal):
  def woof (self):
    print("Woof")
    
class ShihTzu (Dog):
  def woof (self):
    print("Yip Yip")
    
class Dog2 (Animal):
  def __init__ (self, name, sound):
    self.sound = sound
    super().__init__(name)
    
  def woof (self):
    print(self.sound)
    
class Cat (Animal):
  def woof (self):
    print("Meow")
    
class CatDog (Cat, Dog):
  pass

class Robot:
  def auto_destruct (self):
    print("Boom!")
    
class RoboCat (Robot, Cat):
  pass

class RoboDog (Robot, Dog):
  pass

def fight ():
  pass

NAMES = []

def run ():
  total = 2 + 2
  print("Hello")
  
if __name__ == "__main__":
  run()
