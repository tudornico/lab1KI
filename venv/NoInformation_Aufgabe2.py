import shapely.geometry

import playable_area_lab1_AI as area
visited = []
def OtherPolygon(mainLine,current):
    next = 0
    minDistance = 10000
    for polygon in area.inner_polygons:
        if(polygon != onPolygon(current)):
            first = mainLine.intersection(polygon)
            if(not first.is_empty):
                start,end = first.boundary
                distance = area.distanceAB(current.x,current.y,start.x,start.y)
                # we search for the closest intersection
                if(minDistance>distance):
                    next = start
                    minDistance = distance
    return next
def nextIntersection(mainLine,current):
    # get the closest intersection to the current point
    min_distance = 0.1
    if (OtherPolygon(mainLine,current) == 0):
        for polygon in area.inner_polygons:
            first = mainLine.intersection(polygon)

            if(not first.is_empty):
                if(first.type == "Point"):
                    start = first
                else:
                    start,end = first.boundary # this breaks after one run of the code
                return start
    else:
        return OtherPolygon(mainLine,current)




def onPolygon(current):
    for polygon in area.inner_polygons:
        # sometimes he doesn t see the polygon for some god damn reason
        if(polygon.contains(current) or current.within(polygon)):
            return polygon
        corners = list(polygon.exterior.coords)
        for point in corners:
            if(point[0] == current.x and point[1] == current.y):
                return polygon

def walkTheLine(current):
    # go to closest
    polygon = onPolygon(current)
    listOfCorners = list(polygon.exterior.coords)
    dist = 10000
    for point in listOfCorners:
        corner = area.Point(point[0],point[1])
        if(dist > area.distanceAB(point[0],point[1],current.x,current.y) and corner!=current and visited.count(corner) == 0):
            dist = area.distanceAB(point[0],point[1],current.x,current.y)
            next = corner
    visited.append(next)
    return next
def road():

    current = area.start
    while(current != area.end):
        mainLine = shapely.geometry.LineString([(current.x, current.y), (area.end.x, area.end.y)])
        current = nextIntersection(mainLine,current)
        print(current)
        current = walkTheLine(current)

        print(current)
road()