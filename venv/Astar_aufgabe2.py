import shapely.geometry

import playable_area_lab1_AI as area
heuristics = area.getHeuristics()
#gets all the seeable points from the current point
def intersects(current,next):
    line = shapely.geometry.LineString([(current[1], current[2]), (next[1], next[2])])
    for polygon in area.inner_polygons:
        intersections = line.intersection(polygon)
        if(intersections.length>1):
            return True
    return False
def Seeable(current):
    seeable = []
    for next in heuristics:
        if(not intersects(current,next) and current !=next):
            seeable.append(next)
    return seeable

# gets the next point by calculating the distance + heuristic
def NextPoint(current):
    seeable = Seeable(current)
    max = 1000
    dist = 0
    for next in seeable:
        if(max>area.distanceAB(current[1],current[2],next[1],next[2]) + next[0] and next[0]<current[0] ):
            dist = area.distanceAB(current[1],current[2],next[1],next[2])
            max = area.distanceAB(current[1],current[2],next[1],next[2]) + next[0]
            possibleNext = next
    return possibleNext
def Astar_algorithm():

    start = area.start
    end = area.end
    previousCorners=[]
    firstDistance = area.distanceAB(start.x,start.y,end.x,end.y)
    current = [firstDistance,start.x,start.y]
    distance = 0
    lines = []
    while(current[1]!= end.x and current[2] != end.y):
        previous = current
        current = NextPoint(current)
        distance+=area.distanceAB(current[1],current[2],previous[1],previous[2])

    return 1000-distance

def main():
    points = 0
    #we can change the start each time if we want from here
    for tries in range(1,10):
        currentPoints = Astar_algorithm()

        print("You've scored " + str(currentPoints) + " points this round!")
        points += round(currentPoints)
    print("you've scored "+ str(points) + " points Horray!")

main()
