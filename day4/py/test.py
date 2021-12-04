t = [[0]*5]*5
print (t)
t[0][0]=1
print (t)

print([sum(col) for col in zip(*t)])

