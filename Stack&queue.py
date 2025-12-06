# queue 

# are linear structures
q = []

head = 0

def tail(q):
    return len(q)

def push(q, e):
    q.append(e)
    return q

def pop(q):
    return q.pop(head)

push(q, 4)
push(q, 3)
push(q, 5)
push(q, 6)
pop(q)

print (len(q))
print (q)


# stack


s = []

head = 0

def push(s, g):
    s.insert(head, g)
    return g

def pop(s):
    return s.pop(head)

push(s, 1)
push(s, 2)
push(s, 3)

print (s)
pop (s)
print (s)

push(s,9)
push(s,8)
push(s,7)

print (s)
pop (s)
print (s)





