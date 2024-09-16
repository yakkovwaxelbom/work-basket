from crawler import crawl_wiki
from config import BASE_URL, IMAGE_SAVE_DIR, MAX_DEPTH, MAX_WIDTH, MAX_IMAGE_WIDTH


def main():
    crawl_wiki(BASE_URL + "Pablo_Picasso", IMAGE_SAVE_DIR, MAX_DEPTH, MAX_WIDTH, MAX_IMAGE_WIDTH, set())


if __name__ == "__main__":
    main()
