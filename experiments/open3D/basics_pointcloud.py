import open3d as o3d
import numpy as np
import open3d_tutorial as o3dtut
import matplotlib.pyplot as plt

"""
returns an instance of the PointCloud class. 
ALSO WE CAN - o3d.io.read_point_cloud("my_points.txt", format='xyz')
"""
pcd = o3d.io.read_point_cloud("input-output/t_pointclouds/cloud_bin_0.pcd")
print(pcd)

"""
provides a description of the PointCloud class.
"""
# help(open3d)

"""
provides a description of the input arguments and return type of the read_point_cloud function.
"""
# help(o3d.io.read_point_cloud)

"""
Visualize point cloud
`read_point_cloud` считывает облака точек из файла (например .xyz, .xyzn, .xyzrgb, .pts, .ply, .pcd)
`draw_geometries` визуализирует облака точек, так же можно взаимодействовать с объектом с помощью мыши.
"""
# pcd = o3d.io.read_point_cloud("input-output/t_pointclouds/fragment.ply")
# print(np.asarray(pcd.points))
# o3d.visualization.draw_geometries([pcd],
#                                   zoom = 0.3412,
#                                   front=[0.4257, -0.2125, -0.8795],
#                                   lookat=[2.6172, 2.0475, 1.532],
#                                   up=[-0.0694, -0.9768, 0.2024])

"""
Voxel downsampling
"""
# pcd = o3d.io.read_point_cloud("input-output/t_pointclouds/fragment.ply")
# downpcd = pcd.voxel_down_sample(voxel_size=0.05)
# o3d.visualization.draw_geometries([downpcd],
#                                   zoom=0.3412,
#                                   front=[0.4257, -0.2125, -0.8795],
#                                   lookat=[2.6172, 2.0475, 1.532],
#                                   up=[-0.0694, -0.9768, 0.2024])

"""
Vertex normal estimation
`estimation_normals` вычисляет нормаль для каждой точки. 

Функция принимает в качестве аргумента экземпляр класса KDTreeSearchParamHybrid.

Два ключевых аргумента: radius = 0.1 и max_nn = 30 задают радиус поиска и максимальный ближайший сосед. 
Он имеет радиус поиска 10 см и учитывает только до 30 соседей для экономии времени вычислений.

Дополнительные функции ориентации: 
`orient_normals_to_align_with_direction`
`orient_normals_towards_camera_location` 
если ориентация кажется неправильной
"""
# pcd = o3d.io.read_point_cloud("input-output/t_pointclouds/fragment.ply")
# downpcd = pcd.voxel_down_sample(voxel_size=0.05)
# downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
# o3d.visualization.draw_geometries([downpcd],
#                                   zoom=0.3412,
#                                   front=[0.4257, -0.2125, -0.8795],
#                                   lookat=[2.6172, 2.0475, 1.532],
#                                   up=[-0.0694, -0.9768, 0.2024],
#                                   point_show_normal=True)

"""
Access estimated vertex normal
Print a normal vector of the 0th point or 10 points
"""
# print(downpcd.normals[0])
# print(np.asarray(downpcd.normals)[:10, :])


"""
Crop point cloud
Load a polygon volume and use it to crop the original point cloud
`read_selection_polygon_volume` читает файл json, который определяет область выбора многоугольника. 
`vol.crop_point_cloud(pcd)` отфильтровывает точки. Остается только стул.
"""
# pcd = o3d.io.read_point_cloud("input-output/t_pointclouds/fragment.ply")
# vol = o3d.visualization.read_selection_polygon_volume("input-output/t_pointclouds/cropped.json")
# chair = vol.crop_point_cloud(pcd)
# o3d.visualization.draw_geometries([chair],
#                                   zoom=0.7,
#                                   front=[0.5439, -0.2333, -0.8060],
#                                   lookat=[2.4615, 2.1331, 1.338],
#                                   up=[-0.1781, -0.9708, 0.1608])

"""
Paint point cloud
`paint_uniform_color` paints all the points to a uniform color
"""
# pcd = o3d.io.read_point_cloud("input-output/t_pointclouds/fragment.ply")
# vol = o3d.visualization.read_selection_polygon_volume("input-output/t_pointclouds/cropped.json")
# chair = vol.crop_point_cloud(pcd)
# chair.paint_uniform_color([1, 0.706, 0])
# o3d.visualization.draw_geometries([chair],
#                                   zoom=0.7,
#                                   front=[0.5439, -0.2333, -0.8060],
#                                   lookat=[2.4615, 2.1331, 1.338],
#                                   up=[-0.1781, -0.9708, 0.1608])

"""
Point cloud distance
`compute_point_cloud_distance` для вычисления расстояния от исходного облака точек до целевого облака точек
"""

# pcd = o3d.io.read_point_cloud("input-output/t_pointclouds/fragment.ply")
# vol = o3d.visualization.read_selection_polygon_volume("input-output/t_pointclouds/cropped.json")
# chair = vol.crop_point_cloud(pcd)
#
# dists = pcd.compute_point_cloud_distance(chair)
# dists = np.asarray(dists)
# ind = np.where(dists > 0.01)[0]
# pcd_without_chair = pcd.select_by_index(ind)
#
# o3d.visualization.draw_geometries([pcd_without_chair],
#                                   zoom=0.3412,
#                                   front=[0.4257, -0.2125, -0.8795],
#                                   lookat=[2.6172, 2.0475, 1.532],
#                                   up=[-0.0694, -0.9768, 0.2024])

"""
Bounding volumes
AxisAlignedBoundingBox и OrientedBoundingBox - можно использовать для обрезки геометрии
"""
# pcd = o3d.io.read_point_cloud("input-output/t_pointclouds/fragment.ply")
# vol = o3d.visualization.read_selection_polygon_volume("input-output/t_pointclouds/cropped.json")
# chair = vol.crop_point_cloud(pcd)
#
# aabb = chair.get_axis_aligned_bounding_box()
# aabb.color = (1, 0, 0)
# obb = chair.get_oriented_bounding_box()
# obb.color = (0, 1, 0)
# o3d.visualization.draw_geometries([chair, aabb, obb],
#                                   zoom=0.7,
#                                   front=[0.5439, -0.2333, -0.8060],
#                                   lookat=[2.4615, 2.1331, 1.338],
#                                   up=[-0.1781, -0.9708, 0.1608])

"""
Convex hull
Не работатет .get_bunny_mesh() / нет треугольников 
"""
# pcl = o3dtut.get_knot_mesh().sample_points_poisson_disk(number_of_points=2000)
# hull, _ = pcl.compute_convex_hull()
# hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
# hull_ls.paint_uniform_color((1, 0, 0))
# o3d.visualization.draw_geometries([pcl, hull_ls])

"""
DBSCAN clustering
Алгоритм реализован в `cluster_dbscan` и требует двух параметров:
 1. `eps` определяет расстояние до соседей в кластере, 
 2. `min_points` определяет минимальное количество точек, необходимых для формирования кластера. 
Функция возвращает `labels`, где -1 указывает на шум.
"""
# pcd = o3d.io.read_point_cloud("input-output/t_pointclouds/fragment.ply")
# with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
#     labels = np.array(pcd.cluster_dbscan(eps=0.02, min_points=10, print_progress=True))
# max_label = labels.max()
# print(f"point cloud has {max_label + 1} clusters")
# colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
# colors[labels < 0] = 0
# pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
# o3d.visualization.draw_geometries([pcd],
#                                   zoom=0.455,
#                                   front=[-0.4999, -0.1659, -0.8499],
#                                   lookat=[2.1813, 2.0619, 2.0999],
#                                   up=[0.1204, -0.9852, 0.1215])

"""
Plane segmentation
Чтобы найти плоскость с наибольшей опорой в облаке точек - `segment_plane`. У метода есть три аргумента: 
1. `distance_threshold` определяет максимальное расстояние, которое точка может иметь до оцениваемой плоскости, чтобы считаться второстепенным, 
2. `ransac_n` определяет количество точек, которые выбираются случайным образом для оценки плоскости,
3. `num_iterations` определяет, как часто выбирается случайная плоскость. и проверено. 
Затем функция возвращает плоскость как (𝑎, 𝑏, 𝑐, 𝑑), 
так что для каждой точки (𝑥, 𝑦, 𝑧) на плоскости мы имеем 𝑎𝑥 + 𝑏𝑦 + 𝑐𝑧 + 𝑑 = 0. 
Далее функция возвращает список индексов точек вставки.
"""
# pcd = o3d.io.read_point_cloud("input-output/t_pointclouds/fragment.ply")
# plane_model, inliers = pcd.segment_plane(distance_threshold=0.01,
#                                          ransac_n=3,
#                                          num_iterations=1000)
# [a, b, c, d] = plane_model
# print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")
# inlier_cloud = pcd.select_by_index(inliers)
# inlier_cloud.paint_uniform_color([1.0, 0, 0])
# outlier_cloud = pcd.select_by_index(inliers, invert=True)
# o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud],
#                                   zoom=0.8,
#                                   front=[-0.4999, -0.1659, -0.8499],
#                                   lookat=[2.1813, 2.0619, 2.0999],
#                                   up=[0.1204, -0.9852, 0.1215])

"""
Hidden point removal
Не работатет .get_armadillo_mesh() / не нашла   
"""
# print("Convert mesh to a point cloud and estimate dimensions")
# pcd = o3dtut.get_knot_mesh().sample_points_poisson_disk(5000)
# diameter = np.linalg.norm(np.asarray(pcd.get_max_bound()) - np.asarray(pcd.get_min_bound()))
# o3d.visualization.draw_geometries([pcd])
#
# print("Define parameters used for hidden_point_removal")
# camera = [0, 0, diameter]
# radius = diameter * 100
#
# print("Get all points that are visible from given view point")
# _, pt_map = pcd.hidden_point_removal(camera, radius)
#
# print("Visualize result")
# pcd = pcd.select_by_index(pt_map)
# o3d.visualization.draw_geometries([pcd])

