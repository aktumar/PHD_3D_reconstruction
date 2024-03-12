import open3d as o3d
import numpy as np
import open3d_tutorial as o3dtut
import os

"""
From triangle mesh
`create_from_triangle_mesh`,- создает сетку вокселей из сетки треугольников
Он возвращает сетку вокселей, где все воксели, которые пересекаются треугольником, имеют значение 1, 
а все остальные - 0. 
Аргумент `voxel_size` определяет разрешение сетки вокселей.
"""
# print('input')
# mesh = o3dtut.get_knot_mesh()
# mesh.scale(1 / np.max(mesh.get_max_bound() - mesh.get_min_bound()), center=mesh.get_center())
# o3d.visualization.draw_geometries([mesh])
#
# print('voxelization')
# voxel_grid = o3d.geometry.VoxelGrid.create_from_triangle_mesh(mesh, voxel_size=0.05)
# o3d.visualization.draw_geometries([voxel_grid])


"""
From point cloud
`create_from_point_cloud` Сетка вокселей также может быть создана из облака точек
Воксель занят, если хотя бы одна точка облака точек находится внутри вокселя. 
Аргумент `voxel_size` определяет разрешение сетки вокселей.
"""
# print('input')
# N = 2000
# pcd = o3dtut.get_knot_mesh().sample_points_poisson_disk(N)
# pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()), center=pcd.get_center())
# pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(N, 3)))
# o3d.visualization.draw_geometries([pcd])
#
# print('voxelization')
# voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd, voxel_size=0.05)
# o3d.visualization.draw_geometries([voxel_grid])

"""
Inclusion test
Сетка вокселей также может использоваться для проверки того, находятся ли точки в занятом вокселе. 
`check_if_included` принимает массив (n, 3) в качестве входных данных и выводит массив bool.
"""
# queries = np.asarray(pcd.points)
# output = voxel_grid.check_if_included(o3d.utility.Vector3dVector(queries))
# print(output[:10])

"""
Voxel carving
методы `carve_depth_map` и `carve_sil_silhouette` для вырезания вокселей из нескольких карт глубины или силуэтов.
"""

# def xyz_spherical(xyz):
#     x = xyz[0]
#     y = xyz[1]
#     z = xyz[2]
#     r = np.sqrt(x * x + y * y + z * z)
#     r_x = np.arccos(y / r)
#     r_y = np.arctan2(z, x)
#     return [r, r_x, r_y]
#
#
# def get_rotation_matrix(r_x, r_y):
#     rot_x = np.asarray([[1, 0, 0], [0, np.cos(r_x), -np.sin(r_x)],
#                         [0, np.sin(r_x), np.cos(r_x)]])
#     rot_y = np.asarray([[np.cos(r_y), 0, np.sin(r_y)], [0, 1, 0],
#                         [-np.sin(r_y), 0, np.cos(r_y)]])
#     return rot_y.dot(rot_x)
#
#
# def get_extrinsic(xyz):
#     rvec = xyz_spherical(xyz)
#     r = get_rotation_matrix(rvec[1], rvec[2])
#     t = np.asarray([0, 0, 2]).transpose()
#     trans = np.eye(4)
#     trans[:3, :3] = r
#     trans[:3, 3] = t
#     return trans
#
#
# def preprocess(model):
#     min_bound = model.get_min_bound()
#     max_bound = model.get_max_bound()
#     center = min_bound + (max_bound - min_bound) / 2.0
#     scale = np.linalg.norm(max_bound - min_bound) / 2.0
#     vertices = np.asarray(model.vertices)
#     vertices -= center
#     model.vertices = o3d.utility.Vector3dVector(vertices / scale)
#     return model
#
#
# def voxel_carving(mesh,
#                   output_filename,
#                   camera_path,
#                   cubic_size,
#                   voxel_resolution,
#                   w=300,
#                   h=300,
#                   use_depth=True,
#                   surface_method='pointcloud'):
#     mesh.compute_vertex_normals()
#     camera_sphere = o3d.io.read_triangle_mesh(camera_path)
#
#     # setup dense voxel grid
#     voxel_carving = o3d.geometry.VoxelGrid.create_dense(
#         width=cubic_size,
#         height=cubic_size,
#         depth=cubic_size,
#         voxel_size=cubic_size / voxel_resolution,
#         origin=[-cubic_size / 2.0, -cubic_size / 2.0, -cubic_size / 2.0],
#         color=[1.0, 0.7, 0.0])
#
#     # rescale geometry
#     camera_sphere = preprocess(camera_sphere)
#     mesh = preprocess(mesh)
#
#     # setup visualizer to render depthmaps
#     vis = o3d.visualization.Visualizer()
#     vis.create_window(width=w, height=h, visible=False)
#     vis.add_geometry(mesh)
#     vis.get_render_option().mesh_show_back_face = True
#     ctr = vis.get_view_control()
#     param = ctr.convert_to_pinhole_camera_parameters()
#
#     # carve voxel grid
#     pcd_agg = o3d.geometry.PointCloud()
#     centers_pts = np.zeros((len(camera_sphere.vertices), 3))
#     for cid, xyz in enumerate(camera_sphere.vertices):
#         # get new camera pose
#         trans = get_extrinsic(xyz)
#         param.extrinsic = trans
#         c = np.linalg.inv(trans).dot(np.asarray([0, 0, 0, 1]).transpose())
#         centers_pts[cid, :] = c[:3]
#         ctr.convert_from_pinhole_camera_parameters(param)
#
#         # capture depth image and make a point cloud
#         vis.poll_events()
#         vis.update_renderer()
#         depth = vis.capture_depth_float_buffer(False)
#         pcd_agg += o3d.geometry.PointCloud.create_from_depth_image(
#             o3d.geometry.Image(depth),
#             param.intrinsic,
#             param.extrinsic,
#             depth_scale=1)
#
#         # depth map carving method
#         if use_depth:
#             voxel_carving.carve_depth_map(o3d.geometry.Image(depth), param)
#         else:
#             voxel_carving.carve_silhouette(o3d.geometry.Image(depth), param)
#         # print("Carve view %03d/%03d" % (cid + 1, len(camera_sphere.vertices)))
#     vis.destroy_window()
#
#     # add voxel grid survace
#     print('Surface voxel grid from %s' % surface_method)
#     if surface_method == 'pointcloud':
#         voxel_surface = o3d.geometry.VoxelGrid.create_from_point_cloud_within_bounds(
#             pcd_agg,
#             voxel_size=cubic_size / voxel_resolution,
#             min_bound=(-cubic_size / 2, -cubic_size / 2, -cubic_size / 2),
#             max_bound=(cubic_size / 2, cubic_size / 2, cubic_size / 2))
#     elif surface_method == 'mesh':
#         voxel_surface = o3d.geometry.VoxelGrid.create_from_triangle_mesh_within_bounds(
#             mesh,
#             voxel_size=cubic_size / voxel_resolution,
#             min_bound=(-cubic_size / 2, -cubic_size / 2, -cubic_size / 2),
#             max_bound=(cubic_size / 2, cubic_size / 2, cubic_size / 2))
#     else:
#         raise Exception('invalid surface method')
#     voxel_carving_surface = voxel_surface + voxel_carving
#
#     return voxel_carving_surface, voxel_carving, voxel_surface
#
#
# mesh = o3dtut.get_knot_mesh()
# output_filename = os.path.abspath("input-output/t_voxelization/voxelized.ply")
# camera_path = os.path.abspath("input-output/t_voxelization/sphere.ply")
# visualization = True
# cubic_size = 2.0
# voxel_resolution = 128.0
#
# voxel_grid, voxel_carving, voxel_surface = voxel_carving(mesh, output_filename, camera_path, cubic_size,
#                                                          voxel_resolution)
#
# print("surface voxels")
# print(voxel_surface)
# o3d.visualization.draw_geometries([voxel_surface])
#
# print("carved voxels")
# print(voxel_carving)
# o3d.visualization.draw_geometries([voxel_carving])
#
# print("combined voxels (carved + surface)")
# print(voxel_grid)
# o3d.visualization.draw_geometries([voxel_grid])
