import shapely.geometry

import playable_area_lab1_AI as area
visited = []
def OtherPolygon(mainLine,current):
    next = 0
    minDistance = 10000
    # check if there is an intersection on another polygon except the one that is on
    for polygon in area.inner_polygons:
        if(polygon != onPolygon(current)):
            first = mainLine.intersection(polygon)
            if(not first.is_empty):
                start,end = first.boundary
                distance = area.distanceAB(current.x,current.y,start.x,start.y)
                # we search for the closest intersection
                if(minDistance>distance):# find the minimal distance to the one
                    next = start
                    minDistance = distance
    return next

def GetClosest(current):
    minimumDistance = 10000
    mainLine = shapely.geometry.LineString([(current.x, current.y), (area.end.x, area.end.y)])
    if(current!= area.start ):
        for polygon in area.inner_polygons:
            intersection = mainLine.intersection(polygon)
            if(not intersection.is_empty):
                start,end = intersection.boundary
                if(minimumDistance<area.distanceAB(current.x,current.y,start.x,start.y)):
                    minimumDistance = area.distanceAB(current.x,current.y,start.x,start.y)
                    currentPolygon = polygon
    return polygon
def seesOther(mainLine,current):
    currentPolygon = onPolygon(current)
    if(currentPolygon is None):
        currentPolygon = GetClosest(current)
    intersections = mainLine.intersection(currentPolygon)
    if(intersections.length >1):
        return False
    return True
def nextIntersection(mainLine,current):
    # get the closest intersection to the current point
    min_distance = 0.1
    if (OtherPolygon(mainLine,current) == 0):# if there is an intersection on the same polygon
        for polygon in area.inner_polygons:
            first = mainLine.intersection(polygon)

            if(not first.is_empty):
                if(first.type == "Point"):
                    start = first
                else:
                    start,end = first.boundary # this breaks after one run of the code
                return start#we basically do nothing but it will after the function walk the line
    else:
        return OtherPolygon(mainLine,current)# otherwise it willgo to the next polygon

def lineToFinish(current):
    line = shapely.geometry.LineString([(current.x,current.y),(area.end.x,area.end.y)])

    for polygon in area.inner_polygons:
        intersections = line.intersection(polygon)
        if(intersections.length>1):
            return False
    return True


def onPolygon(current):
    #checks if the point is on a polygon
    for polygon in area.inner_polygons:
        # sometimes he doesn t see the polygon for some god damn reason
        if(polygon.contains(current) or current.within(polygon)):
            return polygon
        corners = list(polygon.exterior.coords)
        for point in corners:
            if(point[0] == current.x and point[1] == current.y):
                return polygon # returns the polygon

def walkTheLine(current):
    # goes to closest corner
    polygon = onPolygon(current)
    if(polygon is None):
        polygon = getClosest(current)
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
        # we create each time the line to the end
        mainLine = shapely.geometry.LineString([(current.x, current.y), (area.end.x, area.end.y)])
        # go to the next intersection
        current = nextIntersection(mainLine,current)
        print(current)
        # go to the closest corner
        while(not seesOther(mainLine,current) and not lineToFinish(current)):
            current = walkTheLine(current)
            mainLine = shapely.geometry.LineString([(current.x, current.y), (area.end.x, area.end.y)])
            print(current)
        if(lineToFinish(current)):
            print(area.end)
            current = area.end
            print("Horray you found the finish!!!")
road()