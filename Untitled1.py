#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
class Segment:
    def __init__(self,point1,point2):
        self.point1=point1
        self.point2=point2
        
    def length(self):
        x1,y1=self.point1.x,self.point1.y
        x2,y2=self.point2.x,self.point2.y
        return((x2-x1)**2+(y2-y1)**2)**0.5
    def slope(self):
        x1,y1=self.point1.x,self.point1.y
        x2,y2=self.point2.x,self.point2.y
        if x2-x1==0:
            return None
        else:
            return((y2-y1)/(x2-x1))
        
p1=Point(3,4)
p2=Point()
s=Segment(p1,p2)
print(s.length())
print(s.slope())

