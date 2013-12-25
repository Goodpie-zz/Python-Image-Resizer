usage = "python image_resizer_CMD.py [image_folder] [output_folder] [width] [height]"

from os import listdir
from os.path import isfile, join
import sys, glob
from PIL import Image

def resize(folder, out):
	#Getting all image formats
	all_images = glob.glob(folder + "*.png") + glob.glob(folder + "*.jpg") + glob.glob(folder + "*.gif") + glob.glob(folder + "*.bmp")
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

def correct_usage():
	print("No system arguments provided.\nThe correct usage is: %s" % (usage))


if __name__ == "__main__":
	_imaging = Image.core
	folder_name = sys.argv[1]
	if not sys.argv[2]:
		out_folder = folder_name
	else:
		out_folder = sys.argv[2]

	if not sys.argv[1] and not sys.argv[2]:
		correct_usage()

	resize(folder_name, out_folder)
