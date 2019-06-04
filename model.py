import pptk
import numpy as np
import plyfile

data = plyfile.PlyData.read('germany.ply')['vertex']

xyz = np.c_[data['x'], data['y'], data['z']]          # Eixos
rgb = np.c_[data['red'], data['green'], data['blue']] # RGB
n = np.c_[data['nx'], data['ny'], data['nz']]         # Normais

# v = pptk.viewer(xyz)
# v.set(point_size=0.005)
# v.attributes(rgb / 255., 0.5 * (1 + n))

# extractedData = rgb[:,[2]]  # gets x axis

# matrix = 1*[1*[256]]
# print(matrix)
# rgb[:,[2]][0] = matrix
# print(rgb[:,[2]])

P = np.array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           [10, 11, 12]])

print("\nP Array:")
print(P)

print("\nP[0] Array: selects first row")
print(P[0])

print("\nP[:, 0] Array: selects column")
print(P[:, 0])

P[0] = [0, 0, 0]
print("\nP[0] Modified Array")
print(P[0])

P[:, 0][0] = 12345678
print("\nP[:,1] Modified Array")
print(P)

print(type(P))

print("-------------- model rbg array --------------")

print("RGB Array:")
print(rgb)

print("\nRGB[0] Array: selects first row")
print(rgb[0])

print("\nP[:, 1] Array: selects green column")
print(rgb[:, 1])

rgb[0] = 0
print("\nRGB[0] Modified Array")
print(rgb[0])

# rgb[:, 1] = 0
print("\nRGB[:,1] Modified Array")
print(rgb)
print(type(rgb))


# size = len(rgb[:,[2]])
# for x in range(0, size):
#     rgb[:,[2]][x] = 255;


# Setup viewer
v = pptk.viewer(xyz)
v.set(point_size = 0.005)
v.attributes(rgb / 255., 0.5 * (1 + n))
v.set(bg_color = [0, 0, 0, 1])
v.set(floor_color = [0, 0, 0, 1])
v.set(show_grid = False)
v.set(show_axis = False)

# Rotates camera
poses = []
poses.append([0, 0, 0, 0 * np.pi/2, np.pi/4, 5])
poses.append([0, 0, 0, 1 * np.pi/2, np.pi/4, 5])
poses.append([0, 0, 0, 2 * np.pi/2, np.pi/4, 5])
poses.append([0, 0, 0, 3 * np.pi/2, np.pi/4, 5])
poses.append([0, 0, 0, 4 * np.pi/2, np.pi/4, 5])
v.play(poses, 2 * np.arange(5), repeat=True, interp='linear')


print(type(v))

#

# for x in extractedData
#     element = element % 256 * 1.5


# print(extractedData)
