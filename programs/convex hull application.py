
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def direct(point1: Point, point2: Point, point3: Point):
    d = (point2.y-point1.y)*(point3.x-point2.x)-(point2.x-point1.x)*(point3.y-point2.y)
 
    if d == 0:
        return 0
    if d > 0:
        return 1
    return 2


    
def find_convex_hull(points: list):
    size = len(points)
    
    first_point =  min(points, key=lambda point: point.y)
    temp = first_point
    
    first_index = points.index(first_point)
    second_point= points[(first_index+1)%size]
    
    convex_hull=[]
    
    
    while(second_point != temp):
        
        convex_hull.append(first_point)
        
        first_index = points.index(first_point)
        second_point = points[(first_index+1)%size]
        
        for i in range(size):
            if(direct(first_point, points[i], second_point ) == 2):
                second_point = points[i]
                
        first_point = second_point
    
    return convex_hull

def find_center(points):
    x = 0
    y = 0
    
    for p in points:
        x += p.x
        y += p.y
        
    return x/len(points), y/len(points) 

def distance2(point1, point2):
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2   

n, m = map(int, input().split())

countries = {}
for i in range(m):
    countries[i] = []
    
    
for i in range(n):
    country, x, y = map(float, input().split())
    p = Point(x,y)
    countries[int(country)].append(p)


countries_center = {}
for i in range(m):
    countries_center[i] = find_center(find_convex_hull(countries[i]))
    
        
t = int(input())

result=""
for i in range(t):
    p = list(map(float, input().split()))
    
    minn = float('inf')
    select = -1
    for c in countries_center.keys():
        dist = distance2(p,countries_center[c])
        if dist < minn:
            minn = dist
            select = c
            
    result += (str(select) + " ")
    countries[select].append(Point(p[0], p[1]))
    
print(result)
for i in range(m):
    countries[i] = sorted(find_convex_hull(countries[i]), key=lambda point: point.y)
    countries[i].sort(key=lambda point: point.x)
    print(i, end=" ")
    for p in (countries[i]):
        print("[" + format(p.x, ".2f") + ", " + format(p.y, "0.2f") + "]", end=" ")
    print()
    
    




