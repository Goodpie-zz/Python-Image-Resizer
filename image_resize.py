usage = "usage: python resize_images.py [image_folder] [output_folder] [width] [height]"

from os import listdir
from os.path import isfile, join
import sys, glob
from PIL import Image

def resize(folder, out):
	#Getting all image formats
	all_images = glob.glob(folder + "/*.png") + glob.glob(folder + "/*.jpg") + glob.glob(folder + "/*.gif") + glob.glob(folder + "/*.bmp")
	count = 0
	for image in all_images:
		count += 1
		try:
			try:
				print("\nImage: " + image)
				width = input("Width (in pixels): ")
				height = input("Height (in Pixels): ")
				size = int(width), int(height)
			except:
				print("Invalid Size! ")
			image_directory =  image
			im = Image.open(image_directory)
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(out + "/" + str(count) + ".JPEG")
		except:
			print("Failed to resize image for '%s'" % image_directory)


if __name__ == "__main__":
	print("All images will maintain aspect ration no matter what the inputted dimensions may be.")
	_imaging = Image.core
	folder_name = sys.argv[1]
	if not sys.argv[2]:
		out_folder = folder_name
	else:
		out_folder = sys.argv[2]

	resize(folder_name, out_folder)
