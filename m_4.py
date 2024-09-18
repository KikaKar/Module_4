#Завдання № 1
path = 'salary_file.txt'
def total_salary(path):
    total = 0 # Загальна сума зарплат
    workers = 0 # Кількість робітників
    try:
        with open(path, 'r') as file: # Відкриття файлу 
            for line in file: 
                try:
                    name, salary = line.strip().split(',') # Розділення рядка на ім'я робітників та зарплату
                    salary = float(salary)  # Перетворюємо зарплату на число
                    total += salary  # Обрахунок заробітньої плати загалом
                    workers += 1 # Підрахунок робітників 
                except ValueError:
                    print(f"Помилка у форматі даних: {line.strip()}. Пропускаю цей рядок.")
            if workers > 0:
                    average = total / workers  # Обрахунок середньої зарплати
            else:
                average = 0  # Якщо немає робітників, середня зарплата = 0
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0
    except IOError:
        print(f"Помилка при відкритті файлу {path}.")
        return 0, 0
    
    return total, average  # Повертаємо загальну і середню зарплати

total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")