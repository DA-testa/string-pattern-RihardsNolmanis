def read_input():
    choice = input().strip()
    if choice == "F":
        with open("tests/06") as f_file:
            pattern = f_file.readline().strip()
            text = f_file.readline().strip()
        return pattern, text
    elif choice == "I":
        return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 31
    m = 10**9 + 9
    n = len(pattern)
    t = len(text)
    h = 1
    for i in range(n - 1):
        h = (h * p) % m
    pattern_hash = 0
    text_hash = 0
    for i in range(n):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % m
        text_hash = (text_hash * p + ord(text[i])) % m
    occurrences = []
    for i in range(t - n + 1):
        if pattern_hash == text_hash and pattern == text[i:i+n]:
            occurrences.append(i)
        if i < t - n:
            text_hash = (text_hash - ord(text[i]) * h) % m
            text_hash = (text_hash * p + ord(text[i + n])) % m
            text_hash = (text_hash + m) % m
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

# Rihards Nolmanis 16.grupa 221RDB431