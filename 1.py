points = []
while True:
    point = int(input())
    if point == -1:
        break
    else:
        points.append(point)
max_p = 0
for i in range (0, len(points)):
    if points[i] > max_p:
        max_p = points[i]
print(max_p)