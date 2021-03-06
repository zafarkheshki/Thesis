from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.io import loadmat
import numpy as np
import time

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(21):
    xfile = open('/home/zafar/catkin_ws/src/Thesis/reading_angle_values/Data_collection/ar_tracker_pose'+str(i)+'.txt')
    lines = xfile.readline()
    counter = 3
    x = []
    y = []
    z = []

    while lines:
        if lines.strip() == '* * * * * * *':
            lines = xfile.readline()
        if lines.strip() == 'position:':
            lines = xfile.readline()
        if counter == 0:
            lines = xfile.readline()
            lines = xfile.readline()
            lines = xfile.readline()
            lines = xfile.readline()
            lines = xfile.readline()
            counter = 3
            continue

        wds = lines.split()
        # print(wds)
        if wds[0] == 'x:':
            x.append(float(wds[1]))
        if wds[0] == 'y:':
            y.append(float(wds[1]))
        if wds[0] == 'z:':
            z.append(float(wds[1]))
        
        lines = xfile.readline()
        counter = counter - 1

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x, y, z, c='r', marker='o')
    ax.plot(x, y, z, c='r')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
# ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.set_zlim(-2, 2)
plt.axis('equal')
plt.show()

