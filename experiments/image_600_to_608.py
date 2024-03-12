from PIL import Image

import os

# folder path
dir_path = r'/home/aktumar/1_Study/u_3D_Machine_Learning_Recognition_Py'
count = 0

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        if path[-3:] == "jpg":
            count += 1

            old_im = Image.open(path)
            old_size = old_im.size

            new_size = (int(old_size[0] / 32) * 32, int(old_size[1] / 32) * 32)
            print(f"{count}: {path} resized from {old_size} to {new_size}")

            new_im = Image.new("RGB", new_size)
            box = tuple((n - o) // 2 for n, o in zip(new_size, old_size))
            new_im.paste(old_im, box)

            new_im.save(f"new_data/{path[:-4]}_resize.{path[-3:]}")

print('Image count (jpg, png):', count)
