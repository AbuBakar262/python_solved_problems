import time
import concurrent.futures

import requests

start_time = time.perf_counter()

imgs_urls = [
    "https://unsplash.com/photos/SHkjxRu_uOQ",
    "https://unsplash.com/photos/xvSPt8CD6Vo",
    "https://unsplash.com/photos/SGY0LIfTKZ4",
    "https://unsplash.com/photos/z3slscK_WbI",
    "https://unsplash.com/photos/OG1fEESzfQA",
    "https://unsplash.com/photos/hEgwhy1KBL0",
    "https://unsplash.com/photos/gzIRAg_KK7A",
    "https://unsplash.com/photos/4Iwi-xPaTdA",
    "https://unsplash.com/photos/17EJ1H2-Fro",
    "https://unsplash.com/photos/4A9Cpf_tw9A",
    "https://unsplash.com/photos/_l4RUn0Zn_o"
]


def download_images(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f"{img_name}.jpg"
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded...")


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_images, imgs_urls)

finished_time = time.perf_counter()
print(f"Finished in {round(finished_time-start_time, 2)} second(s)...")
