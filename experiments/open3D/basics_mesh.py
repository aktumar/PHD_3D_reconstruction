import open3d as o3d
import open3d_tutorial as o3dtut
import numpy as np
import copy
import time

"""
Introduction
Просто выводит точки и треугольники в виде матриц
"""
# print("Testing mesh in Open3D...")
# mesh = o3dtut.get_knot_mesh()
# print(mesh)
# print('Vertices:')
# print(np.asarray(mesh.vertices))
# print('Triangles:')
# print(np.asarray(mesh.triangles))

"""
only contains vertices, but no triangles
"""
# mesh = o3dtut.get_armadillo_mesh()
# mesh = o3dtut.get_brain_mesh()
# mesh = o3dtut.get_bunny_mesh()
# mesh = o3dtut.get_cow_mesh()
# mesh = o3dtut.get_elephant_mesh()
# mesh = o3dtut.get_golfball_mesh()
# mesh = o3dtut.get_heptoroid_mesh()
# mesh = o3dtut.get_hippo_mesh()
# mesh = o3dtut.get_horse_mesh()
# mesh = o3dtut.get_igea_mesh()
# mesh = o3dtut.get_knot_mesh()
# mesh = o3dtut.get_lion_mesh()
# mesh = o3dtut.get_lucy_mesh()
# mesh = o3dtut.get_maxplanck_mesh()
# mesh = o3dtut.get_pear_mesh()
# mesh = o3dtut.get_santa_mesh()
# mesh = o3dtut.get_torus_mesh()
# o3d.visualization.draw_geometries([mesh])

"""
Visualize a 3D mesh
"""
# mesh = o3dtut.get_knot_mesh()
# print("Try to render a mesh with normals (exist: " + str(mesh.has_vertex_normals()) + ") and colors (exist: " + str(
#     mesh.has_vertex_colors()) + ")")
# o3d.visualization.draw_geometries([mesh])

"""
Surface normal estimation
"""
# mesh = o3dtut.get_knot_mesh()
# mesh.compute_vertex_normals()
# print(np.asarray(mesh.triangle_normals))
# o3d.visualization.draw_geometries([mesh])

"""
Crop mesh
"""
# mesh = o3dtut.get_knot_mesh()
# mesh1 = copy.deepcopy(mesh)
# mesh1.triangles = o3d.utility.Vector3iVector(np.asarray(mesh1.triangles)[:len(mesh1.triangles) // 2, :])
# mesh1.triangle_normals = o3d.utility.Vector3dVector(np.asarray(mesh1.triangle_normals)[:len(mesh1.triangle_normals) // 2, :])
# print(mesh1.triangles)
# o3d.visualization.draw_geometries([mesh1])

"""
Paint mesh
"""
# mesh = o3dtut.get_knot_mesh()
# mesh.paint_uniform_color([1, 0.706, 0])
# o3d.visualization.draw_geometries([mesh])

"""
Mesh properties
`is_edge_manifold` и `is_vertex_manifold` - проверить треугольную сетку, является ли это краевым многообразием 
`is_edge_manifold` имеет логический параметр `allow_boundary_edges` - должны ли быть разрешены граничные края
`is_self_intersecting` возвращает True, если в сетке существует треугольник, пересекающий другую сетку
`is_watertight` implements the test of self-intersection 
A watertight mesh can be defined as a mesh that is edge manifold, vertex manifold and not self intersecting. 
`is_orientable` cheeeck треугольники могут быть ориентированы таким образом, что все нормали направлены наружу

красным - Ребра, не являющиеся многообразием,
зеленым - граничные ребра, 
зелеными точками - вершины, не являющиеся многообразием, 
розовым - самопересекающиеся треугольники.
"""
# def check_properties(name, mesh):
#     mesh.compute_vertex_normals()
#
#     edge_manifold = mesh.is_edge_manifold(allow_boundary_edges=True)
#     edge_manifold_boundary = mesh.is_edge_manifold(allow_boundary_edges=False)
#     vertex_manifold = mesh.is_vertex_manifold()
#     self_intersecting = mesh.is_self_intersecting()
#     watertight = mesh.is_watertight()
#     orientable = mesh.is_orientable()
#
#     print(name)
#     print(f"  edge_manifold:          {edge_manifold}")
#     print(f"  edge_manifold_boundary: {edge_manifold_boundary}")
#     print(f"  vertex_manifold:        {vertex_manifold}")
#     print(f"  self_intersecting:      {self_intersecting}")
#     print(f"  watertight:             {watertight}")
#     print(f"  orientable:             {orientable}")
#
#     geoms = [mesh]
#     if not edge_manifold:
#         edges = mesh.get_non_manifold_edges(allow_boundary_edges=True)
#         geoms.append(o3dtut.edges_to_lineset(mesh, edges, (1, 0, 0)))
#     if not edge_manifold_boundary:
#         edges = mesh.get_non_manifold_edges(allow_boundary_edges=False)
#         geoms.append(o3dtut.edges_to_lineset(mesh, edges, (0, 1, 0)))
#     if not vertex_manifold:
#         verts = np.asarray(mesh.get_non_manifold_vertices())
#         pcl = o3d.geometry.PointCloud(
#             points=o3d.utility.Vector3dVector(np.asarray(mesh.vertices)[verts]))
#         pcl.paint_uniform_color((0, 0, 1))
#         geoms.append(pcl)
#     if self_intersecting:
#         intersecting_triangles = np.asarray(
#             mesh.get_self_intersecting_triangles())
#         intersecting_triangles = intersecting_triangles[0:1]
#         intersecting_triangles = np.unique(intersecting_triangles)
#         print("  # visualize self-intersecting triangles")
#         triangles = np.asarray(mesh.triangles)[intersecting_triangles]
#         edges = [
#             np.vstack((triangles[:, i], triangles[:, j]))
#             for i, j in [(0, 1), (1, 2), (2, 0)]
#         ]
#         edges = np.hstack(edges).T
#         edges = o3d.utility.Vector2iVector(edges)
#         geoms.append(o3dtut.edges_to_lineset(mesh, edges, (1, 0, 1)))
#     o3d.visualization.draw_geometries(geoms, mesh_show_back_face=True)
#

# check_properties('Moebius', o3d.geometry.TriangleMesh.create_moebius(twists=1))
# check_properties("non-manifold edge", o3dtut.get_non_manifold_edge_mesh())
# check_properties("non-manifold vertex", o3dtut.get_non_manifold_vertex_mesh())
# check_properties("open box", o3dtut.get_open_box_mesh())
# check_properties("intersecting_boxes", o3dtut.get_intersecting_boxes_mesh())

"""
Mesh filtering. Average filter
`number_of_iterations` в функции `filter_smooth_simple` определяет, как часто фильтр применяется к сетке.
"""
print('create noisy mesh')
mesh_in = o3dtut.get_knot_mesh()
vertices = np.asarray(mesh_in.vertices)
noise = 10
vertices += np.random.uniform(0, noise, size=vertices.shape)
mesh_in.vertices = o3d.utility.Vector3dVector(vertices)
mesh_in.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh_in])

print('filter with average with 1 iteration')
mesh_out = mesh_in.filter_smooth_simple(number_of_iterations=1)
mesh_out.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh_out])

print('filter with average with 5 iterations')
mesh_out = mesh_in.filter_smooth_simple(number_of_iterations=5)
mesh_out.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh_out])

"""
Mesh filtering. Laplacian
"""
# print('create noisy mesh')
# mesh_in = o3dtut.get_knot_mesh()
# vertices = np.asarray(mesh_in.vertices)
# noise = 5
# vertices += np.random.uniform(0, noise, size=vertices.shape)
# mesh_in.vertices = o3d.utility.Vector3dVector(vertices)
# mesh_in.compute_vertex_normals()
# o3d.visualization.draw_geometries([mesh_in])
#
# print('filter with Laplacian with 10 iterations')
# mesh_out = mesh_in.filter_smooth_laplacian(number_of_iterations=1)
# mesh_out.compute_vertex_normals()
# o3d.visualization.draw_geometries([mesh_out])
#
# print('filter with Laplacian with 50 iterations')
# mesh_out = mesh_in.filter_smooth_laplacian(number_of_iterations=20)
# mesh_out.compute_vertex_normals()
# o3d.visualization.draw_geometries([mesh_out])

"""
Mesh filtering. Taubin filter
"""
# print('create noisy mesh')
# mesh_in = o3dtut.get_knot_mesh()
# vertices = np.asarray(mesh_in.vertices)
# noise = 2
# vertices += np.random.uniform(0, noise, size=vertices.shape)
# mesh_in.vertices = o3d.utility.Vector3dVector(vertices)
# mesh_in.compute_vertex_normals()
# o3d.visualization.draw_geometries([mesh_in])
#
# print('filter with Taubin with 10 iterations')
# mesh_out = mesh_in.filter_smooth_taubin(number_of_iterations=10)
# mesh_out.compute_vertex_normals()
# o3d.visualization.draw_geometries([mesh_out])
#
# print('filter with Taubin with 100 iterations')
# mesh_out = mesh_in.filter_smooth_taubin(number_of_iterations=100)
# mesh_out.compute_vertex_normals()
# o3d.visualization.draw_geometries([mesh_out])

"""
Sampling. 
.get_bunny_mesh() не работает, замена на knot

`sample_points_uniformly` равномерно выбирает точки с 3D-поверхности на основе площади треугольника. 
`number_of_points` определяет, сколько точек выбирается с поверхности треугольника
`sample_points_poisson_disk` реализует исключение выборки

"""
# mesh = o3d.geometry.TriangleMesh.create_sphere()
# mesh.compute_vertex_normals()
# o3d.visualization.draw_geometries([mesh])
# pcd = mesh.sample_points_uniformly(number_of_points=500)
# o3d.visualization.draw_geometries([pcd])

######################################################################

# mesh = o3d.geometry.TriangleMesh.create_sphere()
# pcd = mesh.sample_points_poisson_disk(number_of_points=500, init_factor=5)
# o3d.visualization.draw_geometries([pcd])
#
# pcd = mesh.sample_points_uniformly(number_of_points=1000)
# pcd = mesh.sample_points_poisson_disk(number_of_points=500, pcl=pcd)
# o3d.visualization.draw_geometries([pcd])

######################################################################

mesh = o3dtut.get_knot_mesh()
mesh.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh])
pcd = mesh.sample_points_uniformly(number_of_points=500)
o3d.visualization.draw_geometries([pcd])

#####################################################################

mesh = o3dtut.get_knot_mesh()
# pcd = mesh.sample_points_poisson_disk(number_of_points=50120, init_factor=5)
# o3d.visualization.draw_geometries([pcd])

pcd = mesh.sample_points_uniformly(number_of_points=2500)
pcd = mesh.sample_points_poisson_disk(number_of_points=500, pcl=pcd)
o3d.visualization.draw_geometries([pcd])

"""
Mesh subdivision
`subdivide_midpoint` вычисляем среднюю точку каждой стороны треугольника и делим треугольник на четыре меньших треугольника. 
3D-поверхность и площадь остаются прежними, но количество вершин и треугольников увеличивается. 
`number_of_iterations` определяет, сколько раз этот процесс должен быть повторен.
"""
# mesh = o3d.geometry.TriangleMesh.create_box()
# mesh.compute_vertex_normals()
# print(f'The mesh has {len(mesh.vertices)} vertices and {len(mesh.triangles)} triangles')
# o3d.visualization.draw_geometries([mesh], zoom=0.8, mesh_show_wireframe=True)
# mesh = mesh.subdivide_midpoint(number_of_iterations=1)
# print(f'After subdivision it has {len(mesh.vertices)} vertices and {len(mesh.triangles)} triangles')
# o3d.visualization.draw_geometries([mesh], zoom=0.8, mesh_show_wireframe=True)
#
# mesh = o3d.geometry.TriangleMesh.create_sphere()
# mesh.compute_vertex_normals()
# print(f'The mesh has {len(mesh.vertices)} vertices and {len(mesh.triangles)} triangles')
# o3d.visualization.draw_geometries([mesh], zoom=0.8, mesh_show_wireframe=True)
# mesh = mesh.subdivide_loop(number_of_iterations=2)
# print(f'After subdivision it has {len(mesh.vertices)} vertices and {len(mesh.triangles)} triangles')
# o3d.visualization.draw_geometries([mesh], zoom=0.8, mesh_show_wireframe=True)

# mesh = o3dtut.get_knot_mesh()
# mesh.compute_vertex_normals()
# print(f'The mesh has {len(mesh.vertices)} vertices and {len(mesh.triangles)} triangles')
# o3d.visualization.draw_geometries([mesh], zoom=0.8, mesh_show_wireframe=True)
# mesh = mesh.subdivide_loop(number_of_iterations=1) # subdivide_midpoint or subdivide_loop
# print(f'After subdivision it has {len(mesh.vertices)} vertices and {len(mesh.triangles)} triangles')
# o3d.visualization.draw_geometries([mesh], zoom=0.8, mesh_show_wireframe=True)

"""
Mesh simplification. Vertex clustering
.get_bunny_mesh() не работает, замена на knot 
`simpleify_vertex_clustering` и имеет параметры 
`voxel_size`, определяющие размер сетки вокселей, и сжатие, которое определяет, как вершины объединяются в пул. 
`o3d.geometry.SimplificationContraction.Average` вычисляет простое среднее.
"""
# mesh_in = o3dtut.get_knot_mesh()
# print(f'Input mesh has {len(mesh_in.vertices)} vertices and {len(mesh_in.triangles)} triangles')
# o3d.visualization.draw_geometries([mesh_in])
#
# voxel_size = max(mesh_in.get_max_bound() - mesh_in.get_min_bound()) / 32
# print(f'voxel_size = {voxel_size:e}')
# mesh_smp = mesh_in.simplify_vertex_clustering(voxel_size=voxel_size, contraction=o3d.geometry.SimplificationContraction.Average)
# print(f'Simplified mesh has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles')
# o3d.visualization.draw_geometries([mesh_smp])
#
# voxel_size = max(mesh_in.get_max_bound() - mesh_in.get_min_bound()) / 16
# print(f'voxel_size = {voxel_size:e}')
# mesh_smp = mesh_in.simplify_vertex_clustering(voxel_size=voxel_size, contraction=o3d.geometry.SimplificationContraction.Average)
# print(f'Simplified mesh has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles')
# o3d.visualization.draw_geometries([mesh_smp])

"""
Mesh simplification. Mesh decimation
`simpleify_quadric_decimation`, минимизирует квадрики ошибок (расстояния до соседних плоскостей). 
`target_number_of_triangles` определяет критерии остановки алгоритма прореживания.
"""
# mesh_in = o3dtut.get_knot_mesh()
# mesh_smp = mesh_in.simplify_quadric_decimation(target_number_of_triangles=6500)
# print(f'Simplified mesh has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles')
# o3d.visualization.draw_geometries([mesh_smp])
#
# mesh_smp = mesh_in.simplify_quadric_decimation(target_number_of_triangles=1746)
# print(f'Simplified mesh has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles')
# o3d.visualization.draw_geometries([mesh_smp])

"""
Connected components
.get_bunny_mesh() работает частично. Внутри bunny.ply есть только точки, но якобы нет треугольников. Хотя через обычный 3D viewer все хорошо 
`cluster_connected_triangles` алгоритм связанных компонентов, который назначает каждый треугольник кластеру связанных треугольников. 
Он возвращает для каждого треугольника индекс кластера в Triangle_clusters 
и для каждого кластера количество треугольников в `cluster_n_triangles` и площадь поверхности кластера в `cluster_area`.
"""
# mesh = o3dtut.get_knot_mesh().subdivide_midpoint(number_of_iterations=2)
# vert = np.asarray(mesh.vertices)
# min_vert, max_vert = vert.min(axis=0), vert.max(axis=0)
# for _ in range(30):
#     cube = o3d.geometry.TriangleMesh.create_box()
#     cube.scale(0.005, center=cube.get_center())
#     cube.translate(
#         (
#             np.random.uniform(min_vert[0], max_vert[0]),
#             np.random.uniform(min_vert[1], max_vert[1]),
#             np.random.uniform(min_vert[2], max_vert[2]),
#         ),
#         relative=False,
#     )
#     mesh += cube
# mesh.compute_vertex_normals()
# print("Show input mesh")
# o3d.visualization.draw_geometries([mesh])
#
# #################################################################
#
# mesh = o3dtut.get_knot_mesh().subdivide_midpoint(number_of_iterations=2)
# print("Cluster connected triangles")
# with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
#     triangle_clusters, cluster_n_triangles, cluster_area = (mesh.cluster_connected_triangles())
# triangle_clusters = np.asarray(triangle_clusters)
# cluster_n_triangles = np.asarray(cluster_n_triangles)
# cluster_area = np.asarray(cluster_area)
#
# #################################################################
#
# mesh = o3dtut.get_knot_mesh().subdivide_midpoint(number_of_iterations=2)
# print("Show mesh with small clusters removed")
# mesh_0 = copy.deepcopy(mesh)
# triangles_to_remove = cluster_n_triangles[triangle_clusters] < 100
# mesh_0.remove_triangles_by_mask(triangles_to_remove)
# o3d.visualization.draw_geometries([mesh_0])
#
# #################################################################
#
# print("Show largest cluster")
# mesh_1 = copy.deepcopy(mesh)
# largest_cluster_idx = cluster_n_triangles.argmax()
# triangles_to_remove = triangle_clusters != largest_cluster_idx
# mesh_1.remove_triangles_by_mask(triangles_to_remove)
# o3d.visualization.draw_geometries([mesh_1])
#
# #################################################################