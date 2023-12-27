import queue
import time

def generate_request(q, counter):
    request_id = counter
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

# Лічильник для ID заявок
request_counter = 1

# Головний цикл програми
try:
    while True:
        generate_request(request_queue, request_counter)
        request_counter += 1
        time.sleep(1)
        process_request(request_queue)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nПрограма завершена користувачем")