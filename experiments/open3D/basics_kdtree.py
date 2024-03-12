import open3d as o3d
import numpy as np

"""
`search_knn_vector_3d` возвращает список индексов k ближайших соседей точки привязки. 
Эти соседние точки закрашены синим цветом. Мы пропускаем первый индекс, так как это сама точка привязки.
`search_radius_vector_3d` для запроса всех точек с расстояниями до точки привязки меньше заданного радиуса. 
Закрашиваем эти точки зеленым цветом.
"""

print("Testing kdtree in Open3D...")
print("Load a point cloud and paint it gray.")
pcd = o3d.io.read_point_cloud("input-output/t_pointclouds/cloud_bin_0.pcd")
pcd.paint_uniform_color([0.5, 0.5, 0.5])
pcd_tree = o3d.geometry.KDTreeFlann(pcd)

print("Paint the 1500th point red.")
pcd.colors[15000] = [1, 0, 0]

print("Find its 200 nearest neighbors, and paint them blue.")
[k, idx, _] = pcd_tree.search_knn_vector_3d(pcd.points[15000], 200)
np.asarray(pcd.colors)[idx[1:], :] = [0, 0, 1]

print("Find its neighbors with distance less than 0.2, and paint them green.")
[k, idx, _] = pcd_tree.search_radius_vector_3d(pcd.points[150], 0.2)
np.asarray(pcd.colors)[idx[1:], :] = [0, 1, 0]

print("Visualize the point cloud.")
o3d.visualization.draw_geometries([pcd],
                                  zoom=0.5599,
                                  front=[-0.4958, 0.8229, 0.2773],
                                  lookat=[2.1126, 1.0163, -1.8543],
                                  up=[0.1007, -0.2626, 0.9596])
