"""

This Downloads the book from fliphtml5. The recently changed their file structures, so most of the codes on github will not work. This is the latest written in 2024 and is working in January 2024.

It will fetch the images of pages from fliphtml5, and then make pdf from them. Make sure that you have installed the dependencies, before executing this code.

It's a pretty simple and basic code with no complexities. For understanding, there will be more comment lines than the actual code :D

I was able to make this code in two days altogether which includes major time of research on fliphtml5.

"""

# One way is to import everything beforhand, but we will import the libraries, the moment we have to use them.


"""
First we need to see the url structure, the url structure is https://online.fliphtml5.com/*****/**** where the aestricks are different for every book, so we need to get this as input from you, so that you can download your favorite book. 


Just punch in the format mentioned below.

*****/****

"""

#Taking Book reference/link from user
book_name = input("Enter the book link in the format *****/****:\n")

# We will fetch config file below

#url of config file
config_file_url = 'https://online.fliphtml5.com/{0}/javascript/config.js'.format(book_name)

#Request to get config file
import requests
import json
config_file = requests.get(config_file_url)
config_dict = json.loads(config_file.text.split('= ')[1].split(';')[0])
fliphtml5_pages = config_dict['fliphtml5_pages']

#Let's prepare where to save our images, creates folder as per title of book
folder_name = config_dict['meta']['title']
import os
os.makedirs(folder_name, exist_ok=True)

#Let's download our images now
page_images=[]
for page in range(len(fliphtml5_pages)):
	page_url = 'https://online.fliphtml5.com/{0}/files/large/{1}'.format(book_name,fliphtml5_pages[page]['n'][0])
	file_path = "{0}/{1}.jpg".format(folder_name, page + 1)
	page_image = requests.get(page_url)
	page_images.append(page_image.content)
	print('Downloading Page ' + str(page + 1) + ' / ' + str(len(fliphtml5_pages)) + ' .....')
	with open(file_path, "wb") as f:
        	f.write(page_image.content)
        	
        	
print("Downloading Complete. Don't Close, hold-on. We are yet to make PDF.")

#Let's make pdf now.
import img2pdf
with open("{0}.pdf".format(folder_name), "wb") as file:
    file.write(img2pdf.convert(page_images))
    
    
print('The pdf named ' + folder_name + '.pdf has been saved in your working directory.')
print('Thank you for using this script written by Engr Moaz Dev.')



