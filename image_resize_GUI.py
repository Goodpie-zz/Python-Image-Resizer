#!/usr/bin/env python
import tkinter as tk
import sys, glob, time
from tkinter.filedialog import *
from PIL import Image

_imaging = Image.core

class Application(tk.Frame):
	
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		self.input_directory = StringVar()
		self.output_directory = StringVar()
		self.progress = StringVar()
		self.progress = StringVar()
		self.width, self.height = StringVar(), StringVar()
		self.createWidgets()
		self.variable_dictionary = {}


	def createWidgets(self):
		self.input_directory.set("No Image Direcotry Selected")
		self.output_directory.set("No Output Directory Selected")

		self.file_Label = tk.Label(self, textvariable=self.input_directory)
		self.file_Label.grid(row=0, column=0)
		self.file_button = tk.Button(self, text="Open Folder", command = lambda:self.selectFolder("Input"))
		self.file_button.grid(row=0, column=1)

		self.output_label = tk.Label(self, textvariable=self.output_directory)
		self.output_label.grid(row=1, column=0)
		self.output_button = tk.Button(self, text = "Select Folder", command = lambda:self.selectFolder("Output"))
		self.output_button.grid(row=1, column=1)

		self.width_label = tk.Label(self, text="Width  (In Pixels): ")
		self.width_label.grid(row=2, column=0)
		self.width_entry = tk.Entry(self, textvariable=self.width)
		self.width_entry.grid(row=2, column=1)
		self.height_label = tk.Label(self, text="Height (In Pixels): ")
		self.height_label.grid(row=3, column=0)
		self.height_entry = tk.Entry(self, textvariable=self.height)
		self.height_entry.grid(row=3, column=1)

		self.resize_button = tk.Button(self, text="Resize Images", command=lambda:self.resizeImages(self.variable_dictionary["Input"], self.variable_dictionary["Output"]))
		self.resize_button.grid(row=4, column=0)

	def resizeImages(self, folder, output):
		folder = str(folder)
		output = str(output)
		all_images = glob.glob(folder + "/*.png") + glob.glob(folder + "/*.jpg") + glob.glob(folder + "/*.gif") + glob.glob(folder + "/*.bmp")
		print(all_images)
		image_count = 0
		for x in all_images:
			image_count += 1
		total_images = image_count
		self.progress.set("0/" + str(total_images) + " Images Resized.")
		self.status_label = tk.Label(self, textvariable = self.progress)
		self.status_label.grid(row=4, column=1)
		try:
			image_count = 0
			size = int(self.width.get()), int(self.height.get())
			for image in all_images:
				image_count += 1
				curent_image = Image.open(image)
				curent_image.thumbnail(size, Image.ANTIALIAS)
				curent_image.save(output + "/" + str(image_count) + ".JPEG")
				self.progress.set( str(image_count) + "/" + str(total_images) + " Images Resized. Resizing: " + image)
		except:
			print("Failed To Resize Images! ")


	def selectFolder(self, name):
		self.variable_dictionary[name] =  askdirectory(title="Choose The Appropriate Folder")
		if name == "Input":
			self.input_directory.set(self.variable_dictionary[name])
		else:
			self.output_directory.set(self.variable_dictionary[name])


if __name__ == "__main__":
	app = Application()
	app.master.title("Image Resizer")
	app.mainloop()
