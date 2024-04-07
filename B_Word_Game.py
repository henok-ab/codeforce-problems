def calculate_points(words):
    word_count = {}
    for person_words in words:
        for word in person_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    points = [0, 0, 0]
    for word, count in word_count.items():
        if count == 1:
            for i, person_words in enumerate(words):
                if word in person_words:
                    points[i] += 3
        elif count == 2:
            for i, person_words in enumerate(words):
                if word in person_words:
                    points[i] += 1

    return points

# Read input until there's no more to read
test_cases = []
while True:
    try:
        t = int(input())  # Number of test cases
        for _ in range(t):
            n = int(input())  # Number of words written by each person
            words = [input().split() for _ in range(3)]  # List of words written by each person
            test_cases.append((n, words))
    except EOFError:
        break

# Process each test case and output the points earned by each player
for n, words in test_cases:
    points = calculate_points(words)
    print(*points)  # Output the points earned by each player
