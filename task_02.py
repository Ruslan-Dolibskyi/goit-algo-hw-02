from collections import deque


def is_palindrome(s):
    # Видалення пробілів і перетворення на нижній регістр
    s = ''.join(s.split()).lower()

    char_deque = deque(s)

    # Перевірка на паліндром
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


# Test
test_strings = ["Радар", "No lemon, no melon", "Python", "Я несу гусеня"]
results = {s: is_palindrome(s) for s in test_strings}
print(results)
