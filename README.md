# 3D_CellposeSegmentation
A python script to loop through a directory and segment 3D images

This python script uses [cellpose](https://cellpose.readthedocs.io/en/latest/) to create binary masks for single time frame z stack tiffs for all tiff files in a specified folder. In this specific case we are segmenting cell membrane, but parameters for the model can be changed to segment other objects. Specifically, this script also applies denoising to the images before performing the segemntation.

## How to set up:
Follow the instructions [here](https://github.com/MouseLand/cellpose/tree/main) to install cellpose. I recommend following option 1 (the installation with conda).

## Things to change:
The variable `img_dir` needs to be changed to specify the path to the folder where the z stack tiffs you want to segment are located. The variable `save_dir` is the path to the folder where you want to save the segmented images to. (Note: the folder where you want to save your semgented images to does not have to exist since the python script will create the folder if it does not exist already).

If the segmentation is not performing as expected, additional parameters may need to be adjusted. This includes `diameter` and `cellprob_threshold` in the following line `masks, flows, styles, imgs_dn = model.eval(img, channels=[0,0], z_axis=0, diameter=60., cellprob_threshold=-5, do_3D=True)`. To get a full description of the parameters, go [here](https://cellpose.readthedocs.io/en/latest/settings.html) and [here](https://cellpose.readthedocs.io/en/latest/api.html).

## How to run:
Make sure your cellpose environment is activated before running the code! If you installed cellpose with conda, simply run `conda activate cellpose`. Next, simply run the python script `segment_cellpose.py` from your command line.
