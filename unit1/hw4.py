colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []
rows = len(colors)
cols = len(colors[0])
num_cells = len(colors) * len(colors[0]);

def sense(p, Z):
    q=[]
    for (color, prob) in zip(colors, p):
        new_row = [];
        for i in range(len(color)):
            if Z == color[i]:
                new_row.append(prob[i]*sensor_right)
            else:
                new_row.append(prob[i]*(1-sensor_right))
        q.append(new_row)

    s = sum(map(sum, q))
    for row in q:
        for i in range(len(row)):
            row[i] = row[i] / s
    return q

def move(p, motion):
    down = motion[0]
    right = motion[1]
    q = [[0]*cols for i in range(rows)];

    for i in range(len(p)):
        row = p[i]
        for j in range(len(row)):
            s = p_move * p[(i-down) % len(p)][(j-right) % len(row)]
            s = s + (1-p_move) * p[i][j]
            q[i][j] = s

    return q

# initialize to uniform distribution
p = [[1.0/(rows*cols)]*cols for i in range(rows)]

for motion, measurement in zip(motions, measurements):
    p = sense(move(p, motion), measurement)

#Your probability array must be printed 
#with the following code.

show(p)

