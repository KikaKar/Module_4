# Завдання № 2
path = 'cats_file.txt' # Змфна шляху до файлу
def get_cats_info(path):
    with open(path, 'r') as file: # Відкриття файлу
        cats_data = []
        for line in file:
            id, name, age = line.strip().split(',') # Розділення рядка на id номер, ім'я кота, рік 
            age = int(age) # Перетворення років на ціле число
            cats_data.append(dict(id = id, name = name, age = age))
            print(cats_data)
get_cats_info(path)
