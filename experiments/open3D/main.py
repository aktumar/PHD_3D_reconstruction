import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

OBJECT = {
    "sushi": "1/input-output/t_mesh/my_3d/material_for_open3d/sushi.ply",
    "broken_cude": "1/input-output/t_mesh/my_3d/material_for_open3d/broken_cube.ply",
    "cube2": "1/input-output/t_mesh/my_3d/material_for_open3d/cube2.ply",
    "donut": "1/input-output/t_mesh/my_3d/material_for_open3d/donut.ply",
    "face": "1/input-output/t_mesh/my_3d/material_for_open3d/face.ply",
    "petroglyph_neon": "1/input-output/t_mesh/my_3d/material_for_open3d/petroglyph_neon.ply",
    "petroglyph_scene": "1/input-output/t_mesh/my_3d/material_for_open3d/petroglyph_scene.ply",
    "pyramid": "1/input-output/t_mesh/my_3d/material_for_open3d/pyramid.ply",
    "reservoir_1": "1/input-output/t_mesh/my_3d/material_for_open3d/reservoir_1.ply",
    "reservoir_2": "1/input-output/t_mesh/my_3d/material_for_open3d/reservoir_2.ply",
    "reservoir_3": "1/input-output/t_mesh/my_3d/material_for_open3d/reservoir_3.ply",
    "reservoir_4": "1/input-output/t_mesh/my_3d/material_for_open3d/reservoir_4.ply",
    "reservoir_5": "1/input-output/t_mesh/my_3d/material_for_open3d/reservoir_5.ply",
    "reservoir_6": "1/input-output/t_mesh/my_3d/material_for_open3d/reservoir_6.ply",
    "reservoir_7": "1/input-output/t_mesh/my_3d/material_for_open3d/reservoir_7.ply",
    "reservoir_8": "1/input-output/t_mesh/my_3d/material_for_open3d/reservoir_8.ply",
    "reservoir_9": "1/input-output/t_mesh/my_3d/material_for_open3d/reservoir_9.ply",
    "reservoir_sample": "1/input-output/t_mesh/my_3d/material_for_open3d/reservoir_sample.ply",

    "room_mesh_1": "1_geometry/input-output/t_mesh/from_rgbd_ex/room_mesh_1.ply",
    "room_point_clouds_1": "1_geometry/input-output/t_mesh/from_rgbd_ex/room_point_clouds_1.ply",
    "room_mesh_2": "1_geometry/input-output/t_mesh/from_rgbd_ex/room_mesh_2.ply",
    "room_point_clouds_2": "1_geometry/input-output/t_mesh/from_rgbd_ex/room_point_clouds_2.ply",
    "room_mesh_3": "1_geometry/input-output/t_mesh/from_rgbd_ex/room_mesh_3.ply",
    "room_point_clouds_3": "1_geometry/input-output/t_mesh/from_rgbd_ex/room_point_clouds_3.ply",

    "env_mesh_1": "1_geometry/input-output/t_mesh/from_rgbd_my_env/env_mesh_1.ply",
    "env_pc_1": "1_geometry/input-output/t_mesh/from_rgbd_my_env/env_pc_1.ply",
    "env_mesh_2": "1_geometry/input-output/t_mesh/from_rgbd_my_env/env_mesh_2.ply",
    "env_pc_2": "1_geometry/input-output/t_mesh/from_rgbd_my_env/env_pc_2.ply",
    "env_mesh_3_vox0.2": "1_geometry/input-output/t_mesh/from_rgbd_my_env/env_mesh_3_vox0.2.ply",
    "env_pc_3_vox0.2": "1_geometry/input-output/t_mesh/from_rgbd_my_env/env_pc_3_vox0.2.ply",
    "env_mesh_4_vox0.002": "1_geometry/input-output/t_mesh/from_rgbd_my_env/env_mesh_4_vox0.002.ply",
    "env_pc_4_vox0.002": "1_geometry/input-output/t_mesh/from_rgbd_my_env/env_pc_4_vox0.002.ply",

    "car_mesh": "1_geometry/input-output/t_mesh/from_rgbd_ex/car_mesh.ply",
    "car_pc": "1_geometry/input-output/t_mesh/from_rgbd_ex/car_pc.ply",
    "car_mesh_1": "1_geometry/input-output/t_mesh/from_rgbd_ex/car_mesh_1.ply",
    "car_pc_1": "1_geometry/input-output/t_mesh/from_rgbd_ex/car_pc_1.ply",
}


def draw_point_cloud(object):
    """
    ORIGIN POINT CLOUDS
    """

    pcd = o3d.io.read_point_cloud(object)
    # print(np.asarray(mesh.points))
    print(pcd)
    o3d.visualization.draw_geometries([pcd],
                                      zoom=0.3412,
                                      front=[0.4257, -0.2125, -0.8795],
                                      lookat=[2.6172, 2.0475, 1.532],
                                      up=[-0.0694, -0.9768, 0.2024])


def draw_triangle_mesh(object):
    """
    ORIGIN MESH
    """
    mesh = o3d.io.read_triangle_mesh(object)
    mesh.compute_vertex_normals()
    print(mesh)
    print("Try to render a mesh with normals (exist: " +
          str(mesh.has_vertex_normals()) + ") and colors (exist: " +
          str(mesh.has_vertex_colors()) + ")")
    o3d.visualization.draw_geometries([mesh])


def draw_voxel(object):
    """
    ORIGIN DISCRITIZATION AND VOXELIZATION
    """
    N = 2000
    mesh = o3d.io.read_triangle_mesh(object).compute_vertex_normals().sample_points_poisson_disk(N)
    mesh.scale(1 / np.max(mesh.get_max_bound() - mesh.get_min_bound()), center=mesh.get_center())
    mesh.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(N, 3)))
    o3d.visualization.draw_geometries([mesh])

    voxel = o3d.geometry.VoxelGrid.create_from_point_cloud(mesh, voxel_size=0.05)
    o3d.visualization.draw_geometries([voxel])


def draw_octree(object):
    """
    ORIGIN DISCRITIZATION AND OCTREE
    """
    print('input')
    N = 2000
    pcd = o3d.io.read_triangle_mesh(object).compute_vertex_normals().sample_points_poisson_disk(N)
    # fit to unit cube
    pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()), center=pcd.get_center())
    pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(N, 3)))
    o3d.visualization.draw_geometries([pcd])

    print('octree division')
    octree = o3d.geometry.Octree(max_depth=4)
    octree.convert_from_point_cloud(pcd, size_expand=0.01)
    o3d.visualization.draw_geometries([octree])


def draw_reconstruction_general(object):
    """
    RECONSTRUCTION (GENERALIZED)
    """
    N = 2000
    mesh = o3d.io.read_triangle_mesh(object).compute_vertex_normals().sample_points_poisson_disk(N)
    o3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)

    rec = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(mesh, 5.5)
    rec.compute_vertex_normals()
    o3d.visualization.draw_geometries([rec], mesh_show_back_face=True)


def draw_reconstruction_nearest(object):
    """
    RECONSTRUCTION (NEAREST POINT)
    """
    N = 10000
    mesh = o3d.io.read_triangle_mesh(object).compute_vertex_normals().sample_points_poisson_disk(N)
    o3d.visualization.draw_geometries([mesh])

    # radii = [0.005, 0.01, 0.02, 0.04]
    radii = [0.1, 0.1, 0.1, 0.1]
    rec = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(mesh, o3d.utility.DoubleVector(radii))
    o3d.visualization.draw_geometries([mesh, rec], mesh_show_back_face=True)


def draw_others(object):
    """
    OTHER INFORMATION
    """

    pcd = o3d.io.read_point_cloud(object)
    o3d.visualization.draw_geometries([pcd],
                                      zoom=0.664,
                                      front=[-0.4761, -0.4698, -0.7434],
                                      lookat=[1.8900, 3.2596, 0.9284],
                                      up=[0.2304, -0.8825, 0.4101])

    print('run Poisson surface reconstruction')
    with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
        mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)
    o3d.visualization.draw_geometries([mesh],
                                      zoom=0.664,
                                      front=[-0.4761, -0.4698, -0.7434],
                                      lookat=[1.8900, 3.2596, 0.9284],
                                      up=[0.2304, -0.8825, 0.4101])

    print('visualize densities')
    densities = np.asarray(densities)
    density_colors = plt.get_cmap('plasma')(
        (densities - densities.min()) / (densities.max() - densities.min()))
    density_colors = density_colors[:, :3]
    density_mesh = o3d.geometry.TriangleMesh()
    density_mesh.vertices = mesh.vertices
    density_mesh.triangles = mesh.triangles
    density_mesh.triangle_normals = mesh.triangle_normals
    density_mesh.vertex_colors = o3d.utility.Vector3dVector(density_colors)
    o3d.visualization.draw_geometries([density_mesh],
                                      zoom=0.664,
                                      front=[-0.4761, -0.4698, -0.7434],
                                      lookat=[1.8900, 3.2596, 0.9284],
                                      up=[0.2304, -0.8825, 0.4101])


draw_triangle_mesh(OBJECT["env_mesh_4_vox0.002"])
draw_point_cloud(OBJECT["env_pc_4_vox0.002"])
