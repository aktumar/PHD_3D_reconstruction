from PIL import Image

im = Image.open("2_re_608_800_r_dm_densedepth.png")
rgb_im = im.convert('RGB')
rgb_im.save("2_re_608_800_r_dm_densedepth.jpg")

im = Image.open("3_re_608_800_l_dm_densedepth.png")
rgb_im = im.convert('RGB')
rgb_im.save("3_re_608_800_l_dm_densedepth.jpg")

im = Image.open("3_re_608_800_r_dm_densedepth.png")
rgb_im = im.convert('RGB')
rgb_im.save("3_re_608_800_r_dm_densedepth.jpg")

im = Image.open("4_re_608_800_r_dm_densedepth.png")
rgb_im = im.convert('RGB')
rgb_im.save("4_re_608_800_r_dm_densedepth.jpg")

im = Image.open("5_re_608_800_r_dm_densedepth.png")
rgb_im = im.convert('RGB')
rgb_im.save("5_re_608_800_r_dm_densedepth.jpg")

im = Image.open("6_re_384_608_r_dm_densedepth.png")
rgb_im = im.convert('RGB')
rgb_im.save("6_re_384_608_r_dm_densedepth.jpg")

im = Image.open("7_re_1920_1080_dm_densedepth.png")
rgb_im = im.convert('RGB')
rgb_im.save("7_re_1920_1080_dm_densedepth.jpg")


# im = Image.open("1myright_depth_dense.png")
# rgb_im = im.convert('RGB')
# rgb_im.save("1myright_depth_dense.jpg")
