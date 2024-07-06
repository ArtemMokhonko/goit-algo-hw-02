from collections  import deque

def is_palindrome(some_txt: str) -> bool:
    
    # Приведення рядка до нижнього регістру та видалення пробілів
    some_txt = some_txt.lower().replace(' ', '')
    
    # Створення двосторонньої черги
    d = deque(some_txt)
    
    # Порівняння символів з обох кінців черги
    while len(d)>1:
        if d.popleft() != d.pop():
            return False
    return True    

# Використання функції
print(is_palindrome("Козак з казок"))  
print(is_palindrome("Hello"))



