from cellpose import denoise, io
import os

#path to folder where the images you want to segment are located
img_dir = r"Y:\Gupton\Edward\3d_cellpose"
#path to where you want to save the masks
save_dir = r"Y:\Gupton\Edward\3d_cellpose\masks"
#what base name you want your mask images to have
save_name = "test_mask"

#make save directory if it doesn't exist
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

#specify model you want to use. In this case, the model also denoises the image
model = denoise.CellposeDenoiseModel(model_type="cyto3", restore_type="denoise_cyto3")

#loop through images in your directory (assumes each image is a z stack per time frame)
for filename in os.listdir(img_dir):
    if filename.endswith('.tif'):
        # read in image
        img = io.imread(os.path.join(img_dir, filename))

        #note: this line assumes that the first axis is the z axis
        masks, flows, styles, imgs_dn = model.eval(img, channels=[0,0], z_axis=0, diameter=60., cellprob_threshold=-5, do_3D=True)

        io.imsave(os.path.join(save_dir, "mask_"+filename), masks)