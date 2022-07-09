import time
# Code Smell: Data Class
class Rectangle:
  def __init__(self, length, width, height):
    self.length = length
    self.width = width
    self.height = height

class Shape:
  def __init__(self,shape):
    self.shape = shape

  def getArea(self,length,width):
    return length * width

  def getVolume(self,length,width,height):
    return length * width * height

# start = time.time()
rect1 = Rectangle(10,20,30)
print("Rectangle 1's Details: ")
print("Rectangle 1's Length\t: %d cm" %(rect1.length))
print("Rectangle 1's Width\t: %d cm" %(rect1.width))
print("Rectangle 1's Height\t: %d cm" %(rect1.height))

shape = Shape(rect1)
print("Rectangle 1's Area\t: %d cm^2" %(shape.getArea(rect1.length, rect1.width)))
print("Rectangle 1's Volume\t: %d cm^3" %(shape.getVolume(rect1.length, rect1.width,rect1.height)))
# end = time.time()
# print("Computational Time \t: %f ms" %((end - start)*1000))
