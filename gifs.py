import imageio.v3 as iio
import os

def next_output_filename(prefix='output', extension='.gif'):
    i = 0
    while True:
        filename = f"{prefix}{i}{extension}"
        if not os.path.exists(filename): # check if the file already exists
            return filename              # if it doesn't, return the filename
        i += 1                           # else add i by 1 and try again

def create_gif(filenames: list, images: list = []):
    for filename in filenames:
        images.append(iio.imread(filename)) # read each image file and append to images list

    new_filenames = next_output_filename()
    iio.imwrite(new_filenames, images, duration=1.2, loop=10)
    # first parameter is the output filename, second is the list of images which is used to make the output.gif, third is gif duration in seconds.

create_gif(['dino1.png', 'dino2.png', 'dino3.png', 'dino4.png'])

#so basically, you're appending the images to a list and then writing that list to a gif file with a duration/loop count of your choice.

#NOT WRITTEN BY AI, if it was this project would be done in 10 minutes.