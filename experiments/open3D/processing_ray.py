"""
Ray Casting
Отчего у меня вообще не работает
"""

import open3d as o3d
import numpy as np

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Load mesh and convert to open3d.t.geometry.TriangleMesh
cube = o3d.geometry.TriangleMesh.create_box().translate([0, 0, 0])
cube = o3d.t.geometry.TriangleMesh.from_legacy(cube)

# Create a scene and add the triangle mesh
scene = o3d.t.geometry.RaycastingScene()
cube_id = scene.add_triangles(cube)

print(cube_id)

# We create two rays:
# The first ray starts at (0.5,0.5,10) and has direction (0,0,-1).
# The second ray start at (-1,-1,-1) and has direction (0,0,-1).
rays = o3d.core.Tensor([[0.5, 0.5, 10, 0, 0, -1], [-1, -1, -1, 0, 0, -1]],
                       dtype=o3d.core.Dtype.Float32)

ans = scene.cast_rays(rays)

print(ans.keys())

print(ans['t_hit'].numpy(), ans['geometry_ids'].numpy())

# Create meshes and convert to open3d.t.geometry.TriangleMesh
cube = o3d.geometry.TriangleMesh.create_box().translate([0, 0, 0])
cube = o3d.t.geometry.TriangleMesh.from_legacy(cube)

torus = o3d.geometry.TriangleMesh.create_torus().translate([0, 0, 2])
torus = o3d.t.geometry.TriangleMesh.from_legacy(torus)

sphere = o3d.geometry.TriangleMesh.create_sphere(radius=0.5).translate([1, 2, 3])
sphere = o3d.t.geometry.TriangleMesh.from_legacy(sphere)

scene = o3d.t.geometry.RaycastingScene()
scene.add_triangles(cube)
scene.add_triangles(torus)
_ = scene.add_triangles(sphere)

rays = o3d.t.geometry.RaycastingScene.create_rays_pinhole(
    fov_deg=90,
    center=[0, 2, 0],
    eye=[2, 3, 0],
    up=[0, 1, 0],
    width_px=640,
    height_px=480,
)
# Ee can directly pass the rays tensor to the cast_rays function.
ans = scene.cast_rays(rays)

plt.imshow(ans['t_hit'].numpy())
plt.savefig("example_4.jpg")

# use abs to avoid negative values
plt.imshow(np.abs(ans['primitive_normals'].numpy()))
plt.savefig("example_5.jpg")

plt.imshow(ans['geometry_ids'].numpy(), vmax=3)
plt.savefig("example_6.jpg")


hit = ans['t_hit'].isfinite()
points = rays[hit][:,:3] + rays[hit][:,3:]*ans['t_hit'][hit].reshape((-1,1))
pcd = o3d.t.geometry.PointCloud(points)
# Press Ctrl/Cmd-C in the visualization window to copy the current viewpoint
o3d.visualization.draw_geometries([pcd.to_legacy()],
                                  front=[0.5, 0.86, 0.125],
                                  lookat=[0.23, 0.5, 2],
                                  up=[-0.63, 0.45, -0.63],
                                  zoom=0.7)
o3d.visualization.draw([pcd])  # new API
