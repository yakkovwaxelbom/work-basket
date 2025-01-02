import csv

PATH = 'lst.csv'


def get_all_story_info(stories_id, limit=5, get_story_info_func=None):
    if not get_story_info_func:
        raise ValueError("No function provided to fetch story information.")

    lst = []
    for id in stories_id[:limit]:
        info = get_story_info_func(id)
        if info:
            lst.append(info)
    return lst


def save_info(lst):
    if not lst:
        print("No data to save.")
        return

    keys = set()
    for info_dict in lst:
        keys.update(info_dict.keys())
    with open(PATH, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=list(keys))
        dict_writer.writeheader()
        dict_writer.writerows(lst)
    print(f"Data saved to {PATH}")
