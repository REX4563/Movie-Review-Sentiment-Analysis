import os
import json

# Initializing all the directoy paths

current_dir = os.path.dirname(os.path.abspath(__file__))

file_dir = fr'{current_dir}\Reviews'
save_path = fr'{current_dir}\reviews.json'

# Loading all the reviews

file_list = os.listdir(file_dir)

def content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

# Converting all the text files to single JSON file

json_dict = {}    # Empty dictionary to catch all the file names and their contents to save as key : value pairs.

for file_name in file_list:
    file_path = os.path.join(file_dir, file_name)

    if os.path.exists(file_path):
        review_content = content(file_path)

        # Extracting movie title from file name

        if review_content is not None:
            movie_title = os.path.splitext(file_name)[0]
            json_dict[movie_title] = review_content

# Write the dictionary to a JSON file

with open(save_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_dict, json_file, ensure_ascii=False, indent=4)
