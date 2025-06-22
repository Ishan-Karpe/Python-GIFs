import imageio.v3 as iio

def create_gif(filenames: list, images: list = []):
    for filename in filenames:
        images.append(iio.imread(filename)) # read each image file and append to images list

    iio.imwrite('output.gif', images, duration=0.5, loop=2)
    # first parameter is the output filename, second is the list of images, third is gif duration in seconds.

create_gif(['dino1.png', 'dino2.png', 'dino3.png', 'dino4.png'])