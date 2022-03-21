import shapely.geometry

import playable_area_lab1_AI as area

def nextIntersection(mainLine):
    intersections = []
    for polygon in area.inner_polygons:


    return intersections[0]


def road():
    mainLine = shapely.geometry.LineString([(area.start.x,area.start.y),(area.end.x,area.end.y)])
    nextIntersection(mainLine)
