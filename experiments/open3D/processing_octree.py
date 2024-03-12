import open3d as o3d
import numpy as np
import open3d_tutorial as o3dtut
import os

"""
From point cloud
`convert_from_point_cloud` Октодерево можно построить из облака точек
`size_expand` увеличивает размер корневого узла октодерева,
поэтому он немного больше, чем границы исходного облака точек, чтобы вместить все точки.
"""
# print('input')
# N = 2000
# pcd = o3dtut.get_knot_mesh().sample_points_poisson_disk(N)
# # fit to unit cube
# pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()), center=pcd.get_center())
# pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(N, 3)))
# o3d.visualization.draw_geometries([pcd])
#
# print('octree division')
# octree = o3d.geometry.Octree(max_depth=4)
# octree.convert_from_point_cloud(pcd, size_expand=0.01)
# o3d.visualization.draw_geometries([octree])

"""
From voxel grid
`create_from_voxel_grid` Октодерево может быть построено из воксельной сетки 
"""
print('input')
N = 2000
pcd = o3dtut.get_knot_mesh().sample_points_poisson_disk(N)
# fit to unit cube
pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()), center=pcd.get_center())
pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(N, 3)))

print('voxelization')
voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd, voxel_size=0.05)
o3d.visualization.draw_geometries([voxel_grid])

print('octree division')
octree = o3d.geometry.Octree(max_depth=4)
octree.create_from_voxel_grid(voxel_grid)
o3d.visualization.draw_geometries([octree])

"""
Traversal
"""

# def f_traverse(node, node_info):
#     early_stop = False
#
#     if isinstance(node, o3d.geometry.OctreeInternalNode):
#         if isinstance(node, o3d.geometry.OctreeInternalPointNode):
#             n = 0
#             for child in node.children:
#                 if child is not None:
#                     n += 1
#             print(
#                 "{}{}: Internal node at depth {} has {} children and {} points ({})"
#                     .format('    ' * node_info.depth,
#                             node_info.child_index, node_info.depth, n,
#                             len(node.indices), node_info.origin))
#
#             # we only want to process nodes / spatial regions with enough points
#             early_stop = len(node.indices) < 250
#     elif isinstance(node, o3d.geometry.OctreeLeafNode):
#         if isinstance(node, o3d.geometry.OctreePointColorLeafNode):
#             print("{}{}: Leaf node at depth {} has {} points with origin {}".
#                   format('    ' * node_info.depth, node_info.child_index,
#                          node_info.depth, len(node.indices), node_info.origin))
#     else:
#         raise NotImplementedError('Node type not recognized!')
#
#     # early stopping: if True, traversal of children of the current node will be skipped
#     return early_stop
#
#
# octree = o3d.geometry.Octree(max_depth=4)
# octree.convert_from_point_cloud(pcd, size_expand=0.01)
# octree.traverse(f_traverse)

"""
Find leaf node containing point

У меня ничего не вывел
"""
# octree.locate_leaf_node(pcd.points[0])
