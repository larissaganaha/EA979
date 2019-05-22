import pptk
import numpy as np
import plyfile

data = plyfile.PlyData.read('germany.ply')['vertex']

xyz = np.c_[data['x'], data['y'], data['z']]          # Eixos
rgb = np.c_[data['red'], data['green'], data['blue']] # RGB
n = np.c_[data['nx'], data['ny'], data['nz']]         # Normais

v = pptk.viewer(xyz)
v.set(point_size=0.005)
v.attributes(rgb / 255., 0.5 * (1 + n))
