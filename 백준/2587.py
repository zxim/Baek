r = []

for i in range(5):
    a = int(input()) 
    r.append(a)
r.sort()
print(int(sum(r)/5))
print(r[2])