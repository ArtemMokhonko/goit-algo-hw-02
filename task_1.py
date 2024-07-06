from queue import Queue
from time import sleep
from random import uniform

# Створити чергу заявок
queue = Queue()

# Лічильник для унікальних номерів заявок
request_id_counter = 1

def generate_request():
    global request_id_counter
    # Створити нову заявку
    request = {
        'id': request_id_counter,
        'data': f'Дані для заявки {request_id_counter}'
    }
    request_id_counter += 1
    # Додати заявку до черги
    queue.put(request)
    print(f'Заявку {request["id"]} створено')

def process_request():
    if not queue.empty():
        # Видалити заявку з черги
        request = queue.get()
        # Обробити заявку
        print(f'Обробка заявки {request["id"]} з даними: {request["data"]}')
        # Імітація обробки заявки
        sleep(uniform(0.5, 2.0))
        queue.task_done()
    else:
        print('Черга порожня, очікування нових заявок...')

def main():
    try:
        while True:
            # Генерація нових заявок кожні 1-3 секунди
            generate_request()
            sleep(uniform(1, 3))
            # Обробка заявки після кожної генерації нової заявки
            process_request()
    except KeyboardInterrupt:
        print('Програму завершено користувачем.')

if __name__ == '__main__':
    main()
