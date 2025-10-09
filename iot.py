import math
class circle:
   def__init__(self,r):
      self.r=r

   def calarea(self):
      return math.pi*self.r**2
   def cirper(self):
      return 2 *math.pi*self.r

 #drive code
r=float(input("Input the radius of the circle:"))

a=circle(r)

area=a.calarea()
ap=a.cirper()

print("Area of the circle:",ap)
