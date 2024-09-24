from api import get_top_stories, get_story_info
from data_handler import get_all_story_info, save_info


def main():
    top_stories = get_top_stories()
    if not top_stories:
        print("No top stories found.")
        return

    stories_info = get_all_story_info(top_stories, limit=5, get_story_info_func=get_story_info)

    save_info(stories_info)


if __name__ == "__main__":
    main()




