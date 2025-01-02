import k_mean

from matplotlib import pyplot as plt
import requests
import numpy as np
import cv2
# URL of the image to download
image_url = 'https://cdn.pixabay.com/photo/2014/08/15/11/29/beach-418742_640.jpg'
image_url = 'https://media.istockphoto.com/id/1342421368/photo/modern-bright-office-space.jpg?s=612x612&w=0&k=20&c=bI4-2ilaPc_gsHe0QcYM3cVIjqsprETTvk5PVQ--BDA='
image_url = 'https://media.istockphoto.com/id/1198339126/photo/f35-jets-flypast-formation-over-the-ocean-low-attitude-flying-3d-render.jpg?s=612x612&w=0&k=20&c=jsALknHYB8zrX7DtfvGifJuwrEm8N9DmTZInh-6Bxm0='
# Send a GET request to the URL
response = requests.get(image_url)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the content of the response
    image_data = response.content
    # Convert the image data to a NumPy array
    nparr = np.frombuffer(image_data, np.uint8)
    # Decode the image array using OpenCV
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    desired_width = 426
    desired_height = 320
    desired_width, desired_height = image.shape[1] // 2,image.shape[0] // 2
    # Downsample the image
    # image = cv2.resize(image, (desired_width, desired_height))
    # Display the image
    plt.figure(figsize=(7, 7))
    plt.imshow(image[:, :, ::-1])
    plt.show()
else:
    print('Failed to download the image. Status code:',
          response.status_code)