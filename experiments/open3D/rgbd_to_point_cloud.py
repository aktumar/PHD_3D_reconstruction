"""
Короче я протестировала этот код. Он дает абсолютно такие же результаты как из туториала open3d

https://betterprogramming.pub/point-cloud-computing-from-rgb-d-images-918414d57e80
"""
import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d
import cv2 as cv

# # Reading 4-th channel
# bgrd = cv.imread("input-output/t_rgbd_images/with_ground_truth/IMG_2071_org_rgbd.JPG", cv.IMREAD_UNCHANGED)
# img = bgrd[:, :, 0:3]  # First 3 channels are the image.
# depth = bgrd[:, :, 3]  # Last channel is the depth
# cv.imshow('img', img)
# cv.imshow('depth', depth)
# cv.waitKey()
# cv.destroyAllWindows()


# Read depth image:
depth_image = cv.imread("input-output/t_rgbd_images/with_ground_truth/IMG_2071_org_rgbd.JPG", cv.IMREAD_UNCHANGED)
# depth_image = cv.imread("input-output/t_rgbd_images/with_ground_truth/frame-000003.depth.png", cv.IMREAD_GRAYSCALE)
print(f"Image resolution: {depth_image.shape}")
print(f"Data type: {depth_image.dtype}")
print(f"Min value: {np.min(depth_image)}")
print(f"Max value: {np.max(depth_image)}")
print(depth_image)

# # помогает осветлить темную картинку
# depth_instensity = np.array(256 * depth_image / 0x0fff, dtype=np.uint8)
# cv.imshow('graycsale image', depth_instensity)
# cv.waitKey(0)


# # Display depth and grayscale image:
# fig, axs = plt.subplots(1, 1)
# axs.imshow(depth_image, cmap="gray")
# axs.set_title('Depth image')
# plt.show()
# plt.close()

# Depth camera parameters:
FX_DEPTH = 5.8262448167737955e+02
FY_DEPTH = 5.8269103270988637e+02
CX_DEPTH = 3.1304475870804731e+02
CY_DEPTH = 2.3844389626620386e+02

# compute point cloud:

pcd = []
height, width = depth_image.shape

print(depth_image[0][0])

for i in range(height):
    for j in range(width):
        z = depth_image[i][j]
        x = (j - CX_DEPTH) * z / FX_DEPTH
        y = (i - CY_DEPTH) * z / FY_DEPTH
        pcd.append([x, y, z])
pcd_o3d = o3d.geometry.PointCloud()  # create point cloud object
pcd_o3d.points = o3d.utility.Vector3dVector(pcd)  # set pcd_np as the point cloud points
# Visualize:
o3d.visualization.draw_geometries([pcd_o3d])

# Read the rgb image:
rgb_image = cv.imread("input-output/t_rgbd_images/with_ground_truth/IMG_2071_scl.jpeg")

# # Display depth and grayscale image:
# fig, axs = plt.subplots(1, 2)
# axs[0].imshow(depth_image, cmap="gray")
# axs[0].set_title('Depth image')
# axs[1].imshow(rgb_image)
# axs[1].set_title('RGB image')
# plt.show()

# Rotation matrix:
R = -np.array([[9.9997798940829263e-01, 5.0518419386157446e-03, 4.3011152014118693e-03],
                   [-5.0359919480810989e-03, 9.9998051861143999e-01, -3.6879781309514218e-03],
                   [- 4.3196624923060242e-03, 3.6662365748484798e-03, 9.9998394948385538e-01]])
# Translation vector:
T = np.array([2.5031875059141302e-02, -2.9342312935846411e-04, 6.6238747008330102e-04])

"""
  Convert the point from depth sensor 3D coordinate system
  to rgb camera coordinate system:
"""
[x_RGB, y_RGB, z_RGB] = np.linalg.inv(R).dot([x, y, z]) - np.linalg.inv(R).dot(T)

# RGB camera intrinsic Parameters:
FX_RGB = 5.1885790117450188e+02
FY_RGB = 5.1946961112127485e+02
CX_RGB = 3.2558244941119034e+0
CY_RGB = 2.5373616633400465e+02

"""
  Convert from rgb camera coordinate system
  to rgb image coordinate system:
"""
j_rgb = int((x_RGB * FX_RGB) / z_RGB + CX_RGB + width / 2)
i_rgb = int((y_RGB * FY_RGB) / z_RGB + CY_RGB)

colors = []
pcd = []
for i in range(height):
    for j in range(width):
        """
            Convert the pixel from depth coordinate system
            to depth sensor 3D coordinate system
        """
        z = depth_image[i][j]
        x = (j - CX_DEPTH) * z / FX_DEPTH
        y = (i - CY_DEPTH) * z / FY_DEPTH

        """
            Convert the point from depth sensor 3D coordinate system
            to rgb camera coordinate system:
        """
        [x_RGB, y_RGB, z_RGB] = np.linalg.inv(R).dot([x, y, z]) - np.linalg.inv(R).dot(T)

        """
            Convert from rgb camera coordinates system
            to rgb image coordinates system:
        """
        j_rgb = int((x_RGB * FX_RGB) / z_RGB + CX_RGB + width / 2)
        i_rgb = int((y_RGB * FY_RGB) / z_RGB + CY_RGB)

        # Add point to point cloud:
        pcd.append([x, y, z])

        # Add the color of the pixel if it exists:
        if 0 <= j_rgb < width and 0 <= i_rgb < height:
            colors.append(rgb_image[i_rgb][j_rgb] / 255)
        else:
            colors.append([0., 0., 0.])

# Convert to Open3D.PointCLoud:
pcd_o3d = o3d.geometry.PointCloud()  # create a point cloud object
pcd_o3d.points = o3d.utility.Vector3dVector(pcd)
pcd_o3d.colors = o3d.utility.Vector3dVector(colors)
# Visualize:
o3d.visualization.draw_geometries([pcd_o3d])

"""
https://medium.com/yodayoda/from-depth-map-to-point-cloud-7473721d3f
"""


def convert_from_uvd(self, u, v, d):
    d *= self.pxToMetre
    x_over_z = (self.cx - u) / self.focalx
    y_over_z = (self.cy - v) / self.focaly
    z = d / np.sqrt(1. + x_over_z ** 2 + y_over_z ** 2)
    x = x_over_z * z
    y = y_over_z * z
    return x, y, z
