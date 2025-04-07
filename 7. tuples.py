t1 = (10, 20, 30, 40)
print(type(t1))

print(t1[0])

t2 = (10,)
print(t2)
print(len(t2))

lst = [[10, 20, 30], [40, 50, 60]]
for l in lst:
    for item in l:
        print(item)

tpl = ((10, 20, 30), (40, 50, 60), [1, 2, 3], (["a", "b"],))
print(tpl[0:2])
print(tpl[0:1])
print(tpl[2:])
print(tpl[0][0])
print(tpl[2][0])

for l in tpl:
    for item in l:
        print(item)

print(tpl.count((10, 20, 30)))
print(tpl.count((["a", "b"],)))
