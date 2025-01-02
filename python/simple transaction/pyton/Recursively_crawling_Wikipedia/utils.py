import os
import urllib.parse
import requests
from bs4 import Tag
from typing import List, Tuple, Optional

from config import MAX_NAME_IMAGE_SIZE


def get_random_user_agent() -> str:
    from fake_useragent import UserAgent
    ua = UserAgent()
    return ua.random


def get_html(url: str) -> requests.Response | None:
    headers = {
        'User-Agent': get_random_user_agent()
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
    return None


def path_image(name_img: str, dir_path: str) -> str:
    return os.path.join(dir_path, name_img)


def save_img(img_data: requests.Response, path: str) -> None:
    with open(path, 'wb') as file:
        file.write(img_data.content)


def truncate_text(text: str, max_length: int) -> str:
    if len(text) > max_length:
        return text[:max_length] + '...'
    return text


def fixed_images(data: List[List[Optional[Tag]]], base_url: str) -> List[Tuple[str, Optional[str]]]:
    fixed_images_list = []
    for img_tag, figcaption_tag in data:
        if img_tag and img_tag.has_attr('src'):
            src = img_tag['src']
            if src.startswith('//'):
                src = "https:" + src
            elif src.startswith('/'):
                src = urllib.parse.urljoin(base_url, src)
            caption = figcaption_tag.get_text(strip=True) if figcaption_tag else None
            if caption:
                caption = truncate_text(caption, MAX_NAME_IMAGE_SIZE)
            fixed_images_list.append((src, caption))
    return fixed_images_list
