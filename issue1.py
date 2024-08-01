"""
This code downloads the book mentioned in Issue 1. The book is not on fliphtml5 but on another website something named as archive.alsharekh.org

The link mentioned in the issue is: https://archive.alsharekh.org/MagazinePages/MagazineBook/Ouyon_AL_Makalat/sana_1986/Issue_4/index.html
"""


#Taking Book reference/link from user
book_link = input("Enter the complete book link:\n")
url = book_link.split('index.html')[0]

# We will fetch config file below

#url of config file
config_file_url = '{0}mobile/javascript/config.js'.format(url)

#Request to get config file
import requests
#import json
config_file = requests.get(config_file_url)
#config_dict = json.loads(config_file.text.split('= ')[1][:-1])      #changed from split(';') to slicing to remove last semicolon.
total_pages = int(config_file.text.split('bookConfig.totalPageCount=')[1].split(';')[0])

import os
os.makedirs('bookdownload', exist_ok=True)

#Let's download our images now
page_images=[]
for page in range(total_pages):
    page_url = '{0}/files/mobile/{1}.jpg'.format(url, page+1)    #fliphtml5_pages[page]['n'][0]) #changed large to page
    file_path = "bookdownload/{0}.jpg".format(page + 1)
    page_image = requests.get(page_url)
    page_images.append(page_image.content)
    print('Downloading Page ' + str(page + 1) + ' / ' + str(total_pages) + ' .....')
    with open(file_path, "wb") as f:
        f.write(page_image.content)
        	
if page_images != []:
    print("Downloading Complete. Don't Close, hold-on. We are yet to make PDF.")

    #Let's make pdf now.
    import img2pdf
    with open("bookdownload.pdf", "wb") as file:
        file.write(img2pdf.convert(page_images))
        
        
    print('The pdf named bookdownload.pdf has been saved in your working directory.')
    print('Thank you for using this script written by Engr Moaz Dev.')
