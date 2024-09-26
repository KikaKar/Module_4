# Завдання № 2
path = 'cats_file.txt' # Змфна шляху до файлу
def get_cats_info(path):
    try:
        with open(path, 'r') as file: # Відкриття файлу
            cats_data = [] # Створення списку для словників
            for line in file:
                try:
                    id, name, age = line.strip().split(',') # Розділення рядка на id номер, ім'я кота, рік 
                    age = int(age) # Перетворення років на ціле число
                except ValueError: # Перевірка формату рядка у файлі
                    print(f"Помилка у форматі даних: {line.strip()}.")
                cats_dict = dict(id = id, name = name, age = age) # Створення словника із ключами: id, name, age та відповідними значеннями
                cats_data.append(cats_dict) # Додавання словників у список      
    except FileNotFoundError: # Перевірка на відсутність файлу
        print(f'Файл {path} не знайдено.')
        return 0, 0 
    except IOError: # Перевірка доступу до файлу
        print(f'Помилка при відкриті файлу {path}.')
        return 0, 0
    return cats_data
print(get_cats_info(path))