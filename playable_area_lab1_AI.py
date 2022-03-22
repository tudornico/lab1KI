#!/usr/bin/env python
# coding: utf-8

# In[277]:


import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
import math

# In[278]:


plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show() 


# In[279]:


polygon0 = Polygon([(12, 3),
   (11, 2),
   (9, 12),
   (21, 22),
])

polygon1 = Polygon([(20, 25),
   (22, 60),
   (10 , 81),
   (11, 41),
])

polygon2 = Polygon([(15, 90),
   (30, 71),
   (44, 68),
   (40, 95),
])

polygon3 = Polygon([(35, 60),
   (30, 40),
   (42, 21),
   (50, 55),
])

polygon4 = Polygon([(30, 10),
   (32, 33),
   (40, 17),
   (45, 3),
])

polygon5 = Polygon([(50, 15),
   (55, 35),
   (68, 25),
   (70, 5),
])

polygon6 = Polygon([(55, 45),
   (65, 38),
   (67, 60),
   (55, 70),
])

polygon7 = Polygon([(50, 90),
   (65, 68),
   (95, 85),
   (95, 95),
])

polygon8 = Polygon([(75, 65),
   (80, 45),
   (92, 35),
   (95, 75),  
])

polygon9 = Polygon([(78, 35),
   (78, 7),
   (96, 12),
   (92, 23),
])


# In[280]:


inner_polygons = [polygon0, 
            polygon1, 
            polygon2, 
            polygon3, 
            polygon4, 
            polygon5, 
            polygon6, 
            polygon7, 
            polygon8, 
            polygon9]


# In[281]:


def draw_shapes(shapes):
    for shape in shapes:
        x, y = shape.exterior.xy
        plt.plot(x, y, c="red")


# In[282]:


draw_shapes(inner_polygons)
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()


# In[283]:


def distanceAB(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist


# In[284]:


end = Point(98,98)
draw_shapes(inner_polygons)
plt.plot(end.coords, c="red")
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()


# In[307]:


outer_polygon = Polygon(
    [
   (0, 0),
   (100, 0),
   (100, 100),
   (0, 100),
    ]
)


# In[333]:


playable_area = Polygon(outer_polygon, inner_polygons)


# In[338]:


end = Point(98,98)
end1 = Point(0,0)
end2 = Point(0,100)
end3 = Point(100,0)
#start = playable_area.representative_point()
start = Point(1,2)
draw_shapes(inner_polygons)
draw_shapes([outer_polygon])
plt.plot(*end.coords,'bo')
plt.plot(*end1.coords,'bo')
plt.plot(*end2.coords,'bo')
plt.plot(*end3.coords,'bo')
plt.plot(*start.coords,'bo')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.fill([0,100,100,0], [0,0,100,100], facecolor='lightsalmon', edgecolor='orangered', linewidth=3)
plt.show()


# In[ ]:
# all the heuristics of all points
def getHeuristics():
    list0 = list(polygon0.exterior.coords)
    list1 = list(polygon1.exterior.coords)
    list2 = list(polygon2.exterior.coords)
    list3 = list(polygon3.exterior.coords)
    list4 = list(polygon4.exterior.coords)
    list5 = list(polygon5.exterior.coords)
    list6 = list(polygon6.exterior.coords)
    list7 = list(polygon7.exterior.coords)
    list8 = list(polygon8.exterior.coords)
    list9 = list(polygon9.exterior.coords)
    heuristics =[]
    for corner in list0:
        heuristics.append((distanceAB(corner[0],corner[1],end.x,end.y),corner[0],corner[1]))

    for corner in list1:
        heuristics.append((distanceAB(corner[0], corner[1], end.x, end.y), corner[0], corner[1]))

    for corner in list2:
        heuristics.append((distanceAB(corner[0], corner[1], end.x, end.y), corner[0], corner[1]))

    for corner in list3:
        heuristics.append((distanceAB(corner[0], corner[1], end.x, end.y), corner[0], corner[1]))

    for corner in list4 :
        heuristics.append((distanceAB(corner[0], corner[1], end.x, end.y), corner[0], corner[1]))

    for corner in list5:
        heuristics.append((distanceAB(corner[0], corner[1], end.x, end.y), corner[0], corner[1]))

    for corner in list6:
        heuristics.append((distanceAB(corner[0], corner[1], end.x, end.y), corner[0], corner[1]))

    for corner in list7:
        heuristics.append((distanceAB(corner[0], corner[1], end.x, end.y), corner[0], corner[1]))

    for corner in list8:
        heuristics.append((distanceAB(corner[0], corner[1], end.x, end.y), corner[0], corner[1]))

    for corner in list9:
        heuristics.append((distanceAB(corner[0], corner[1], end.x, end.y), corner[0], corner[1]))

    heuristics.append((0,end.x,end.y))
    return heuristics #[0] :  heuristic [1] : point x [2] : point [y]

# In[ ]:





# In[ ]:


