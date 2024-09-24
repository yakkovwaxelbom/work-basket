import os
import random
import urllib.parse
import requests
from bs4 import BeautifulSoup, Tag
from typing import Tuple, List, Optional

from utils import get_html, path_image, save_img, fixed_images


def scan_html(html: requests.Response) -> Tuple[str, List[List[Optional[Tag]]], List[Tag]]:
    html_parser = BeautifulSoup(html.text, 'html.parser')
    all_images = []
    name_dir = ""
    figures = html_parser.findAll('figure')
    if len(figures) > 0:
        for figure in figures:
            img_tag = figure.find('img')
            figcaption_tag = figure.find('figcaption')
            all_images.append([img_tag, figcaption_tag])
        name_dir = html_parser.title.string.replace(' - Wikipedia', '')
    all_urls = html_parser.find_all('a', href=True)
    return name_dir, all_images, all_urls


def get_random_image(all_images: List[List[Optional[Tag]]], max_img: int) -> List[List[Optional[Tag]]]:
    return random.sample(all_images, min(len(all_images), max_img))


def get_random_urls(all_urls: List[Tag], max_urls: int, visited_links: set, base_url: str) -> List[str]:
    links_url = []
    unvisited_links = set(link.get('href') for link in all_urls) - visited_links
    randomly_sampled_urls = random.sample(list(unvisited_links), min(len(unvisited_links), max_urls))
    for tag in randomly_sampled_urls:
        if tag.startswith("/wiki"):
            full_url = urllib.parse.urljoin(base_url, tag)
            links_url.append(full_url)
    return links_url


def download_images(url_images: List[Tuple[str, Optional[str]]], directory: str) -> None:
    os.makedirs(directory, exist_ok=True)
    for url_image, caption in url_images:
        img_response = get_html(url_image)
        if img_response:
            image_name = caption + '.jpg' if caption else 'image.jpg'
            file_path = path_image(image_name, directory)
            save_img(img_response, file_path)


def get_data(url: str, width: int, image_width: int, visited: set) -> Tuple[str, List[tuple[str, str | None]], List[str]]:
    html = get_html(url)
    name_dir, images, urls = scan_html(html)
    images = get_random_image(images, image_width)
    urls = get_random_urls(urls, width, visited, url)
    images = fixed_images(images, url)
    return name_dir, images, urls


def crawl_wiki(url: str, directory: str, depth: int, width: int, image_width: int, visited_links: set):
    visited_links.add(url)
    name_dir, images, urls = get_data(url, width, image_width, visited_links)
    current_directory = os.path.join(directory, name_dir)
    download_images(images, current_directory)

    if depth > 0:
        for url in urls:
            crawl_wiki(url, directory, depth - 1, width, image_width, visited_links)
