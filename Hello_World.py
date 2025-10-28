H = "Hello"
W = "World"
print (H,W)


import array as Arr
A = Arr.array('l',[1,2,3,4])


P = list([246,345])
L = list ('246345')
print (P)
print (L)
T = tuple(A)
print(T)
R = list(range(1,10,5))
print(R)
print (list(A))
P.reverse()
print(P)

def f(x):
     return (x - 2)
print(f(2), f(4), f(6))

def main(x,y):
     print(x,y)
main("Hello","World")

     
def g(n):
     return (n*n+n+2)/2
print (g(3))
print (g(1), g(0))
print (g(100), g(67))