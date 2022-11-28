import base64
#####IMGUR######

from pathlib import Path
import requests, json
import pyimgur
from imgurpython import ImgurClient


def upload_image(code):
    image = base64.b64decode(code)
    img_file = open('image_to_imgur/image.jpeg', 'w+')
    img_file.write(image)
    img_file.close()

    directory = 'image_to_imgur/image.jpeg'

    CLIENT_ID = '851c881d15a628e'
    CLIENT_SECRET = 'de18eba31b31c91cc3134f1bea74c39b80e099ed'
    imgr_username = "rheejan"   
    imgr_password = "09491751465"

    client = ImgurClient(CLIENT_ID, CLIENT_SECRET)

    auth_url = client.get_auth_url('pin')

    #PATH =f'../images/{receipt}'
    PATH = f'image_to_imgur/image.jpeg' 
    album=  None

    config={
           'album' :album,
           'name': '0',
           'title': '0',
           'description': '0',
           }
    image = client.upload_from_path(PATH, config = config, anon=False)
    return image['link']
