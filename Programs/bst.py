a = [2,3,1,5,8,9]
for elem in a:
    print(elem)
a.append(6)
a.remove(3)
a.sort()
a.reverse()
print(a)
a.pop()
print(a)

name = "hello world"
print(name[::-2])
b = a.copy()
print(b)
a.extend(b)
print(a)
print(a.count(8))
c = []
c = a.copy()
print(c)
c.insert(2,55)
print(c)
print(len(a))
print("max:")
print(max(a))
print("min")
print(min(a))
print(sum(a))
d = [1,2,3,4,5]
print(d)
for elem in d:
    if elem == max(d):
        d.remove(elem)
    print(d)
d.clear()
print(d)