import queue
import random
import time


def generate_request(q):
    request_id = random.randint(1, 100)
    print(f"Генерується заявка з ID: {request_id}")
    q.put(request_id)


def process_request(q):
    if not q.empty():
        request_id = q.get()
        print(f"Обробляється заявка з ID: {request_id}")
    else:
        print("Черга пуста")


# Створення черги заявок
request_queue = queue.Queue()

# Запис часу початку роботи програми
start_time = time.time()

# Встановлення часового ліміту
time_limit = 30

# Головний цикл програми
while True:
    generate_request(request_queue)
    time.sleep(1)
    process_request(request_queue)
    time.sleep(1)

    # Перевірка, чи минув часовий ліміт
    if time.time() - start_time > time_limit:
        print("Часовий ліміт завершення програми")
        break
