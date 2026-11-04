import re
from collections import Counter

# 1.
def is_palindrome(text: str) -> bool:
    # Ignorujemy spacje i zamieniamy wszystko na małe litery
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

# 2.
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Liczba musi być nieujemna")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 3. 
def count_vowels(text: str) -> int:
    vowels = "aeiouyąęó"
    return sum(1 for char in text.lower() if char in vowels)

# 4.
def calculate_discount(price: float, discount: float) -> float:
    if not 0.0 <= discount <= 1.0:
        raise ValueError("Zniżka musi mieścić się w przedziale od 0 do 1")
    return price * (1 - discount)

# 5.
def flatten_list(nested_list: list) -> list:
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

# 6.
def word_frequencies(text: str) -> dict:
    if not text:
        return {}
    clean_text = re.sub(r'[^\w\s]', '', text.lower())
    words = clean_text.split()
    return dict(Counter(words))

# 7.
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
