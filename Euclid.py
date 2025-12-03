
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
    dist2 = ((abs)(p1x - p2x)**2 + (abs)(p1y - p2y)**2)**(1/2)
    
    print ("distance:", dist2)
elif euclidean_calculator == "3":
    dist3 = ((abs)(p1x - p2x)**2 + (abs)(p1y - p2y)**2)**(1/2)
    dist4 = ((abs)(p2x - p3x)**2 + (abs)(p2y - p3y)**2)**(1/2)
    dist5 = ((abs)(p1x - p3x)**2 + (abs)(p1y - p3y)**2)**(1/2)
    
    print ("distance of point 1 to point 2:", dist3)
    print ("distance of point 2 to point 3:", dist4)
    print ("distance of point 1 to point 3:", dist5)

    

