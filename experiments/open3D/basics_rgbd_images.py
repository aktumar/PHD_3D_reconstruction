import open3d as o3d
import open3d_tutorial as o3dtut
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

import matplotlib.image as mpimg
import re

"""
Redwood dataset
"""
print("Read Redwood dataset")
# redwood_rgbd = o3d.data.SampleRedwoodRGBDImages()
# color_raw = o3d.io.read_image(redwood_rgbd.color_paths[0])
# depth_raw = o3d.io.read_image(redwood_rgbd.depth_paths[0])

# color_raw = o3d.io.read_image("input-output/t_rgbd_images/4_600_800_r.jpg")  # colored
# color_raw = o3d.io.read_image("input-output/t_rgbd_images/4_600_800_rl_dm_cvstereo.jpg")  # color of depth map
# depth_raw = o3d.io.read_image("input-output/t_rgbd_images/4_600_800_rl_dm_cvstereo.png")  # without layers
# depth_raw = o3d.io.read_image("input-output/t_rgbd_images/4_600_800_rl_dm_cvstereo.jpg")  # with layers
color_raw = o3d.io.read_image("input-output/t_rgbd_images/with_ground_truth/IMG_2071_scl.png")
depth_raw = o3d.io.read_image("input-output/t_rgbd_images/with_ground_truth/IMG_2071_scl.png")
####################################################################################################
# img = cv.imread("input-output/t_rgbd_images/frame-000003.depth.png")
# print("min pixel of image = ", np.amin(img))
# print("max pixel of image = ", np.amax(img))
# print(img.dtype)
# print(img)
####################################################################################################

# color_raw = o3d.geometry.Image.flip_horizontal(coloJPGr_raw)
# depth_raw = o3d.geometry.Image.flip_horizontal(depth_raw)

rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, depth_scale=15000, depth_trunc=3)

# Показывет две картинки в виде графиков
plt.subplot(1, 2, 1)
plt.title('Redwood grayscale image')
plt.imshow(rgbd_image.color)
plt.subplot(1, 2, 2)
plt.title('Redwood depth image')
plt.imshow(rgbd_image.depth)
# plt.show()

rgbd_image.color = color_raw  # дала цвет этим облочкам, хотя казалось бы фигня
# rgbd_image.color = depth_raw  # с пнг в жпг надо поменять чтобы цвета появились от глубин

# Изображение RGBD можно преобразовать в облако точек с учетом набора параметров камеры.
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd_image,
    o3d.camera.PinholeCameraIntrinsic(
        o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
# Flip it, otherwise the pointcloud will be upside down
pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
aabb = pcd.get_axis_aligned_bounding_box()
aabb.color = (1, 0, 0)
o3d.visualization.draw_geometries([pcd, aabb], zoom=0.7)

# Voxels
# pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()), center=pcd.get_center())
# # o3d.visualization.draw_geometries([pcd])
# voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd, voxel_size=0.02)
# o3d.visualization.draw_geometries([voxel_grid])

"""
SUN dataset
"""
# print("Read SUN dataset")
# # sun_rgbd = o3d.data.SampleSUNRGBDImage()
# # color_raw = o3d.io.read_image(sun_rgbd.color_path)
# # depth_raw = o3d.io.read_image(sun_rgbd.depth_path)
#
#
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/donut_img.jpg")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/donut_depth.jpeg")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/samples/exam2_img.jpg")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/samples/exam2_depth.png")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/exam4_img.png")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/exam4_depth.png")
# color_raw = o3d.io.read_image("input-output/t_rgbd_images/with_ground_truth/IMG_2071_scl.jpeg")
# depth_raw = o3d.io.read_image("input-output/t_rgbd_images/with_ground_truth/IMG_2071_scl.png")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/frame-000003.color.jpg")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/frame-000003.depth.png")
# rgbd_image = o3d.geometry.RGBDImage.create_from_sun_format(color_raw, depth_raw)
# print("rgbd_image", rgbd_image)
#
# # # Показывет две картинки в виде графиков
# # plt.subplot(1, 2, 1)
# # plt.title('SUN grayscale image')
# # plt.imshow(rgbd_image.color)
# # plt.subplot(1, 2, 2)
# # plt.title('SUN depth image')
# # plt.imshow(rgbd_image.depth)
# # plt.show()
#
# pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
#     rgbd_image,
#     o3d.camera.PinholeCameraIntrinsic(
#         o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
# # Flip it, otherwise the pointcloud will be upside down
# pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
# o3d.visualization.draw_geometries([pcd], zoom=0.5)

"""
NYU dataset
"""

# def read_nyu_pgm(filename, byteorder='>'):
#     with open(filename, 'rb') as f:
#         buffer = f.read()
#     try:
#         header, width, height, maxval = re.search(
#             b"(^P5\s(?:\s*#.*[\r\n])*"
#             b"(\d+)\s(?:\s*#.*[\r\n])*"
#             b"(\d+)\s(?:\s*#.*[\r\n])*"
#             b"(\d+)\s(?:\s*#.*[\r\n]\s)*)", buffer).groups()
#     except AttributeError:
#         raise ValueError("Not a raw PGM file: '%s'" % filename)
#     img = np.frombuffer(buffer,
#                         dtype=byteorder + 'u2',
#                         count=int(width) * int(height),
#                         offset=len(header)).reshape((int(height), int(width)))
#     img_out = img.astype('u2')
#     return img_out
#
#
# print("Read NYU dataset")
# # Open3D does not support ppm/pgm file yet. Not using o3d.io.read_image here.
# # MathplotImage having some ISSUE with NYU pgm file. Not using imread for pgm.
#
# # nyu_rgbd = o3d.data.SampleNYURGBDImage()
# # color_raw = mpimg.imread(nyu_rgbd.color_path)
# # depth_raw = read_nyu_pgm(nyu_rgbd.depth_path)
#
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/donut_img.jpg")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/donut_depth.jpeg")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/exam2_img.jpg")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/exam2_depth.png")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/exam4_img.png")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/exam4_depth.png")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/exam5_img.png")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/exam5_depth.png")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/exam6_img.png")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/exam6_depth.png")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/exam7_img.png")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/exam7_depth.png")
# color_raw = o3d.io.read_image("input-output/t_rgbd_images/with_ground_truth/IMG_2071_scl.jpeg")
# depth_raw = o3d.io.read_image("input-output/t_rgbd_images/with_ground_truth/IMG_2071_scl.png")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/frame-000003.color.jpg")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/frame-000003.depth.png")
# color = o3d.geometry.Image(color_raw)
# depth = o3d.geometry.Image(depth_raw)
# rgbd_image = o3d.geometry.RGBDImage.create_from_nyu_format(color, depth)
# print("rgbd_image", rgbd_image)
#
# # plt.subplot(1, 2, 1)
# # plt.title('NYU grayscale image')
# # plt.imshow(rgbd_image.color)
# # plt.subplot(1, 2, 2)
# # plt.title('NYU depth image')
# # plt.imshow(rgbd_image.depth)
# # plt.show()
#
# pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
#     rgbd_image,
#     o3d.camera.PinholeCameraIntrinsic(
#         o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
# # Flip it, otherwise the pointcloud will be upside down
# pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
# o3d.visualization.draw_geometries([pcd], zoom=0.5)

"""
TUM dataset
"""
# print("Read TUM dataset")
# # tum_rgbd = o3d.data.SampleSUNRGBDImage()
# # color_raw = o3d.io.read_image(tum_rgbd.color_path)
# # depth_raw = o3d.io.read_image(tum_rgbd.depth_path)
#
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/4myleft.jpg")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/4my_depth.png")
#
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/donut_img.jpg")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/donut_depth.jpeg")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/exam2_img.jpg")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/exam2_depth.png")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/exam4_img.png")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/exam4_depth.png")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/exam5_img.png")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/exam5_depth.png")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/exam6_img.png")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/exam6_depth.png")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/exam7_img.png")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/exam7_depth.png")
# color_raw = o3d.io.read_image("input-output/t_rgbd_images/with_ground_truth/IMG_2071_scl.jpeg")
# depth_raw = o3d.io.read_image("input-output/t_rgbd_images/with_ground_truth/IMG_2071_scl.png")
# # color_raw = o3d.io.read_image("input-output/t_rgbd_images/frame-000003.color.jpg")
# # depth_raw = o3d.io.read_image("input-output/t_rgbd_images/frame-000003.depth.png")
# rgbd_image = o3d.geometry.RGBDImage.create_from_tum_format(color_raw, depth_raw)
# print("rgbd_image", rgbd_image)
#
# # plt.subplot(1, 2, 1)
# # plt.title('TUM grayscale image')
# # plt.imshow(rgbd_image.color)
# # plt.subplot(1, 2, 2)
# # plt.title('TUM depth image')
# # plt.imshow(rgbd_image.depth)
# # plt.show()
#
# pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
#     rgbd_image,
#     o3d.camera.PinholeCameraIntrinsic(
#         o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
# # Flip it, otherwise the pointcloud will be upside down
# pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
# o3d.visualization.draw_geometries([pcd], zoom=0.35)
