import math

euclidean_calculator = input("enter how many diminsions (2) or (3): ")


x = input("first x: ")
y = input("first y: ")

c = input("second x: ")
v = input("second y: ")
if euclidean_calculator == "3":
    m = input("third x: ")
    z = input("third y: ")


p1x = float(x)
p1y = float(y)

p2x = float(c)
p2y = float(v)
if euclidean_calculator == "3":
    p3x = float(m)
    p3y = float(z)

if euclidean_calculator =="2":
    dist2 = (p1x - p2x)**2 + (p1y - p2y)**2
    eclu_dist2 = math.sqrt(dist2)
    print ("distance:", eclu_dist2)
elif euclidean_calculator == "3":
    dist3 = (p1x - p2x)**2 + (p1y - p2y)**2
    dist4 = (p2x - p3x)**2 + (p2y - p3y)**2
    dist5 = (p1x - p3x)**2 + (p1y - p3y)**2
    eclu3_dist = math.sqrt(dist3)
    eclu4_dist = math.sqrt(dist4)
    eclu5_dist = math.sqrt(dist5)
    print ("distance of point 1 to point 2:", eclu3_dist)
    print ("distance of point 2 to point 3:", eclu4_dist)
    print ("distance of point 1 to point 3:", eclu5_dist)

    

