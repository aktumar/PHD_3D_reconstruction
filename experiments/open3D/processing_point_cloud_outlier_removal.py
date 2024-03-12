import open3d as o3d
import numpy as np
import open3d_tutorial as o3dtut
import matplotlib.pyplot as plt

"""
Prepare input data
Точно такой код был рассмотрен в предыдущей главе, такая же функция, почти такой же файл..
`uniform_down_sample` за исключением данной функции, которая очень похожа на
`voxel_down_sample`

`uniform_down_sample` альтернатива субдескритезации, чтобы уменьшить размер облака точек, собирая каждую n-ю точку.
"""
# print("Load a ply point cloud, print it, and render it")
# pcd = o3d.io.read_point_cloud("input-output/t_pointclouds/cloud_bin_0.pcd")
# o3d.visualization.draw_geometries([pcd],
#                                   zoom=0.3412,
#                                   front=[0.4257, -0.2125, -0.8795],
#                                   lookat=[2.6172, 2.0475, 1.532],
#                                   up=[-0.0694, -0.9768, 0.2024])
#
# print("Downsample the point cloud with a voxel of 0.02")
# voxel_down_pcd = pcd.voxel_down_sample(voxel_size=0.02)
# o3d.visualization.draw_geometries([voxel_down_pcd],
#                                   zoom=0.3412,
#                                   front=[0.4257, -0.2125, -0.8795],
#                                   lookat=[2.6172, 2.0475, 1.532],
#                                   up=[-0.0694, -0.9768, 0.2024])
#
# print("Every 5th points are selected")
# uni_down_pcd = pcd.uniform_down_sample(every_k_points=5)
# o3d.visualization.draw_geometries([uni_down_pcd],
#                                   zoom=0.3412,
#                                   front=[0.4257, -0.2125, -0.8795],
#                                   lookat=[2.6172, 2.0475, 1.532],
#                                   up=[-0.0694, -0.9768, 0.2024])

"""
Select down sample
`select_by_index` принимает двоичную маску для вывода только выбранных точек. 
Отображаются выбранные точки и невыбранные точки.
"""

def display_inlier_outlier(cloud, ind):
    inlier_cloud = cloud.select_by_index(ind)
    outlier_cloud = cloud.select_by_index(ind, invert=True)

    print("Showing outliers (red) and inliers (gray): ")
    outlier_cloud.paint_uniform_color([1, 0, 0])
    inlier_cloud.paint_uniform_color([0.8, 0.8, 0.8])
    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud],
                                      zoom=0.3412,
                                      front=[0.4257, -0.2125, -0.8795],
                                      lookat=[2.6172, 2.0475, 1.532],
                                      up=[-0.0694, -0.9768, 0.2024])


"""
Statistical outlier removal
`statistics_outlier_removal` удаляет точки, которые находятся дальше от своих соседей по сравнению со средним значением для облака точек. 

Требуется два входных параметра:
`nb_neighbors` - сколько соседей учитывается для вычисления среднего расстояния для данной точки.
`std_ratio` - установить пороговый уровень на основе стандартного отклонения средних расстояний через облако точек. 
Чем ниже это число, тем более агрессивным будет фильтр.
"""
print("Statistical oulier removal")
cl, ind = voxel_down_pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
display_inlier_outlier(voxel_down_pcd, ind)


"""
Radius outlier removal
`radius_outlier_removal` удаляет точки, у которых есть несколько соседей в данной сфере вокруг них. 
Для настройки фильтра на ваши данные можно использовать два параметра:
`nb_points`, - выбрать минимальное количество точек, которое должна содержать сфера.
`radius`, - определяет радиус сферы, который будет использоваться для подсчета соседей.
"""
print("Radius oulier removal")
cl, ind = voxel_down_pcd.remove_radius_outlier(nb_points=16, radius=0.05)
display_inlier_outlier(voxel_down_pcd, ind)
