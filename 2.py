points = []
while True:
    point = int(input())
    if point == -1:
        break
    else:
        points.append(point)

k_friends = len(points)
print(k_friends)