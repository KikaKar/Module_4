# Завдання № 2
path = 'cats_file.txt' # Змфна шляху до файлу
def get_cats_info(path):
    with open(path, 'r') as file: # Відкриття файлу
        