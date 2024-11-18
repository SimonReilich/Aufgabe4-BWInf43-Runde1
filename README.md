# Aufgabe 4 - Krocket

# Lösungsidee

Das Problem kann gelößt werden, indem man eine Regressionsgerade durch die Mittelpunkte der Tore berechnet, und anschließend prüft, ob für jedes Tor ein Torpfosten oberhalb, und einer unterhalb der Gerade liegt. Um den Ballradius zu berücksichtigen, kann der minimale Abstand der oberen $d_{über}$ und der unteren $d_{unter}$ Torpfosten zur Gerade berechnet werden. Ist $(d_{unter} + d_{über}) * \cos \alpha$ größer als der Radius des Balls, passt der Ball auf einer geraden Linie durch alle Tore, es ist also möglich, ihn in einem Schlag hindurch zuschießen.

Um die Parameter für Lauras Wurf zu finden, wird zunächst angenommen, dass Laura bei den Koordinaten $(0cm, 0cm)$ steht. Die Regressionsgerade ist durch die beiden Parameter $m$ (Steigung) und $d$ ($y$-Achsenabschnitt) bestimmt. $d$ gibt dabei an, um wieviel Laura von ihrem Startpunkt aus in $y$-Richtung laufen muss, $\alpha = \arctan(m)$ gibt den Abschlagwinkel zur $x$-Achse an.

# Umsetzung

*Die Lösungsidee wurde in Python mit dem Modul numpy erstellt. Auf die genaue Dokumentation des Einlesens wird verzichtet.*

Zunächst erwartet das Programm in der Methode `get_content()` vom Benutzer den Namen der Eingabedatei (für die Beispiele reicht es aus, die Nummer des Beispiels anzugeben). Die Methode gibt die Zeilen der Datei als Liste von Strings zurück.

Der Durchmesser des Balls wird mithilfe eines regulären Ausdrucks aus der ersten Zeile extrahiert. Dann werden die darauffolgenden Zeilen nacheinander in Paare von Punkten umgewandelt (dies geschieht in der Methode `to_goals()`, ebenfalls mittels eines regulären Ausdrucks) und in die Liste `goals` eingefügt. `goals` ist also eine Liste von Paaren von Punkten. Danach werden mit `avg_x()` bzw. `avg_y()` die x- und die y-Koordinaten der Mittelpunkte der Tore ausgerechnet und in der Liste `x` bzw. `y` gespeichert. Über diesen Punkten wird nun mit `coef = np.polyfit(x,y,1)` die lineare Regression ausgeführt. `regression_line = np.poly1d(coef)` erzeugt anschließend eine Funktion `regression_line()`, die der Regressionsgerade entspricht.

Nun wird für alle Torpfostenpaare mittels  `(regression_line(goal[0][0]) >= goal[0][1] and regression_line(goal[1][0]) <= goal[1][1]) or (regression_line(goal[0][0]) <= goal[0][1] and regression_line(goal[1][0]) >= goal[1][1])` geprüft, ob einer der beiden oberhalb, und der andere unterhalb der Regressionsgerade liegen. Ist dies nicht der Fall, wird abgebrochen und auf der Konsole eine Nachricht ausgegeben, dass es keine Möglichkeit gibt, in einem Schlag alle Tore zu treffen.

Andernfalls werden die beiden Parameter `m` und `d` aus dem Tupel `coef` extrahiert. Um den maximalen Radius des Balls zu berechnen wird nun die Liste von Paaren von Punkten `goals` durch die Methode `split()` in zwei Listen von Punkten `l` und `u` aufgeteilt, sodass in `l` alle Pfosten-Koordinaten enthalten sind, die unterhalb der Geraden liegen, und in `u` alle, die oberhalb liegen. `get_min_distance()` berechnet dann die Betragsmäßig kleinste Distanz von einem der Punkte aus `l` bzw. `u`. Das Ergebnis wird in `dl` bzw. `du` gespeichert.

Ausgegeben werden nun die Distanz, die Laura in y-Richtung gehen muss (`d`), sowie der Abschlagwinkel $\alpha$ in Grad, der sich aus `np.rad2deg(np.arctan(m))` berechnet. Der maximale Balldurchmesser berechnet sich aus `(dl + du) * np.cos(np.arctan(m))`. Auch wenn dieser kleiner als der angegebene Durchmesser ist, wird das Ergebnis trotzdem angezeigt, zusätzlich wird aber noch ein Hinweis ausgegeben, dass der tatsächliche Durchmesser des Balls zu groß ist, um alle Tore in einem Schlag zu treffen.

# Beispiele

## Beispiel 1

<aside>
📥

9 1
10 20 12 3
20 20 14 3
33 15 23 16
0 60 60 0
48 16 120 70
160 100 160 40
170 100 200 100
215 120 230 95
230 135 245 110

</aside>

<aside>
📤

It is not possible to hit all the gates in one shot

</aside>

## Beispiel 2

<aside>
📥

9 1
10 20 12 3
20 20 14 3
33 15 23 16
0 60 60 0
48 16 120 70
126 149 238 121
123 167 251 162
156 202 206 183
136 227 281 216

</aside>

<aside>
📤

It is not possible to hit all the gates in one shot

</aside>

## Beispiel 3

<aside>
📥

396 20
24 157 18 16
31634 256 31627 93
170 152 163 8
31451 260 31444 87
341 157 333 17
31292 249 31288 90
503 161 503 4
31148 256 31130 83
663 169 670 8
30994 257 30972 83

… [Der Übersichtlichkeit wegen gekürzt]

</aside>

<aside>
📤

Angle alpha = 0.0042002841752690825°; Distance d = 126.9349288876428cm
Maximum ball diameter: 48.87023294491248cm; Actual ball diameter: 20cm

</aside>

## Beispiel 4

<aside>
📥

344 25
19 3329 6 148
40 443 119 118
13 860 138 55
105 667 294 73
19 2458 318 221
324 310 300 358
157 1547 333 269
365 513 374 51
738 721 401 129
410 1237 908 550

… [Der Übersichtlichkeit wegen gekürzt]

</aside>

<aside>
📤

It is not possible to hit all the gates in one shot

</aside>

## Beispiel 5

<aside>
📥

406 484
300 13639 5611 19079
2337 15289 3859 13305
366 10133 5766 14593
6305 16496 6052 12582
6270 14699 6077 10300
6352 14757 6231 12480
6323 14050 6260 12394
6606 16260 6081 10309
6938 16557 6257 11441
7002 15909 6272 11423

… [Der Übersichtlichkeit wegen gekürzt]

</aside>

<aside>
📤

Angle alpha = -13.855505579147756°; Distance d = 14959.938738347519cm
Maximum ball diameter: 917.9188221851784cm; Actual ball diameter: 484cm

</aside>

# Quellcode

### Hauptprogramm

```python
import numpy as np
import re

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
    elif (regression_line(goal[0][0]) >= goal[0][1] 
		    and regression_line(goal[1][0]) <= goal[1][1]) 
			  or (regression_line(goal[0][0]) <= goal[0][1] 
			  and regression_line(goal[1][0]) >= goal[1][1]):
        continue
    else:
        possible = False

if possible:
    m, d = coef
    (l, u) = split(goals, regression_line)
    dl = get_min_distance(l, regression_line)
    du = get_min_distance(u, regression_line)
    print()
    print(f"""Angle alpha = {"%0.2f" % np.rad2deg(np.arctan(m))}°; 
		    Distance d = {"%0.2f" % d}cm""")
    print(f"""Maximum ball diameter: {"%0.2f" % (dl + du)}cm; 
		    Actual ball diameter: {"%0.2f" % diam}cm""")
    if dl + du < diam:
        print("""Ball diameter is too large, it is not possible 
		        to hit all the gates in one shot""")
else:
    print()
    print("It is not possible to hit all the gates in one shot")
    
```

### Hilfsmethoden

```python
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

```

### Methoden zum Einlesen der Eingabedatei

```python
def get_content():
    file_name = input("""Please provide the path of the 
		    .txt-file containing the input: """)
    if file_name == "1" or file_name == "2" or file_name == "3" 
		    or file_name == "4" or file_name == "5":
        file_name = f"krocket{file_name}.txt"
    file = open(file_name, encoding="UTF-8")
    return file.readlines()

def to_goals(line):
    ls = re.findall("[0-9]+", line)
    return (int(ls[0]), int(ls[1])), (int(ls[2]), int(ls[3]))

```