import numpy as np
import re

def get_content():
    file_name = input("Please provide the path of the .txt-file containing the input: ")
    if file_name == "1" or file_name == "2" or file_name == "3" or file_name == "4" or file_name == "5":
        file_name = f"krocket{file_name}.txt"
    file = open(file_name, encoding="UTF-8")
    return file.readlines()

def to_goals(line):
    ls = re.findall("[0-9]+", line)
    return (int(ls[0]), int(ls[1])), (int(ls[2]), int(ls[3]))

def avg_x(goals):
    res = []
    for goal in goals:
        res.append((goal[0][0] + goal[1][0]) / 2)
    return res

def avg_y(goals):
    res = []
    for goal in goals:
        res.append((goal[0][1] + goal[1][1]) / 2)
    return res

def split(goals, line):
    lower = []
    upper = []
    for goal in goals:
        if line(goal[0][0]) >= goal[0][1] and line(goal[1][0]) <= goal[1][1]:
            lower.append(goal[0])
            upper.append(goal[1])
        elif line(goal[0][0]) <= goal[0][1] and line(goal[1][0]) >= goal[1][1]:
            lower.append(goal[1])
            upper.append(goal[0])
    return lower, upper

def get_min_distance(points, line):
    min_dist = line(points[0][0]) - points[0][1]
    if min_dist < 0:
        min_dist = 0 - min_dist
    for point in points[1 : ]:
        dist = line(point[0]) - point[1]
        if dist < 0:
            dist = 0 - dist
        if dist < min_dist:
            min_dist = dist
    return min_dist

content = get_content()
goals = []
diam = int(re.findall("[0-9]+", content[0])[1])
for line in content[1 : ]:
    goals.append(to_goals(line))


x = avg_x(goals)
y = avg_y(goals)

coef = np.polyfit(x,y,1)
regression_line = np.poly1d(coef)
# regression_line is now a function which takes in x and returns y

possible = True
for goal in goals:
    if not possible:
        break
    elif (regression_line(goal[0][0]) >= goal[0][1] and regression_line(goal[1][0]) <= goal[1][1]) or (regression_line(goal[0][0]) <= goal[0][1] and regression_line(goal[1][0]) >= goal[1][1]):
        continue
    else:
        possible = False

if possible:
    m, d = coef
    (l, u) = split(goals, regression_line)
    dl = get_min_distance(l, regression_line)
    du = get_min_distance(u, regression_line)
    print()
    print(f"Angle alpha = {np.rad2deg(np.arctan(m))}°; Distance d = {d}cm")
    print(f"Maximum ball diameter: {(dl + du) * np.cos(np.arctan(m))}cm; Actual ball diameter: {diam}cm")
    if dl + du < diam:
        print("Ball diameter is too large, it is not possible to hit all the gates in one shot")
else:
    print()
    print("It is not possible to hit all the gates in one shot")