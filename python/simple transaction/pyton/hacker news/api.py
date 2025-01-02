import requests

HN_PREFIX = 'https://hacker-news.firebaseio.com/v0/'
HN_TOP_STORIES = 'topstories.json?print=pretty'
HN_ITEM = 'item/{}.json?print=pretty'

def get_top_stories():
    response = requests.get(HN_PREFIX + HN_TOP_STORIES)
    if response.status_code == 200:
        return response.json()  # מחזיר מערך של ID-ים
    else:
        print(f"Error fetching top stories: {response.status_code}")
        return []

def get_story_info(id):
    response = requests.get(HN_PREFIX + HN_ITEM.format(id))
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching story info for ID {id}: {response.status_code}")
        return {}
