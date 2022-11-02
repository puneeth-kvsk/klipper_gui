import requests
import helper
from concurrent.futures import ThreadPoolExecutor as pool
import time


# Fetch URL
def get_url(url):
    return requests.post(url)


# Move slide in 2D plane
def move_slide_in_2d_plane(h_value, i_value):
    params = {'H': h_value, 'I': i_value}
    command_pool = helper.move_multiple_axes_to(params)
    return command_pool


#