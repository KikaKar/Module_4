#Завдання № 1
path = 'salary_file.txt'
def total_salary(path):
    total = 0 # Загальна сума зарплат
    workers = 0 # Кількість робітників
    with open(path, 'r') as file: # Відкриття файлу 
        for line in file: 
            name, salary = line.strip().split(',') # Розділення рядка на ім'я робітників та зарплату
            salary = int(salary)  # Перетворюємо зарплату на число
            total += salary  # Обрахунок заробітньої плати загалом
            workers += 1 # Підрахунок робітників 
        average = total / workers if workers > 0 else 0 # Обрахунок середгьої заробітньої платні 
        return total, average

total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")