#Завдання № 1
path = open('salary_file.txt', mode='r')
def total_salary(path):
    
    symbols = path.read()
    print(symbols)
    path.close()

total_salary(path)