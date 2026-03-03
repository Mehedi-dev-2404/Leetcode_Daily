import time

# --------------------------
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# --------------------------
# Prime dense window function (TASK 3: Set version)
# --------------------------
def prime_dense_window(s, w, n):

    # Check if input is numeric
    if not s.isdigit():
        return 0, 0, "Invalid input"

    max_count = 0
    best_index = 0
    best_primes = set()   # CHANGED: list -> set

    # Move sliding window across the string
    for i in range(len(s) - w + 1):
        window = s[i:i + w]
        primes_found = set()   # CHANGED: list -> set

        # Generate all substrings inside the window
        for start in range(w):
            for end in range(start + 1, w + 1):
                substring = window[start:end]
                number = int(substring)

                # Check limit and primality
                if number < n and is_prime(number):
                    primes_found.add(number)   # CHANGED: no "not in", just add

        # Update densest window (tie-breaking unchanged: earliest stays)
        if len(primes_found) > max_count:
            max_count = len(primes_found)
            best_index = i
            best_primes = primes_found.copy()  # still works for sets

    best_primes_sorted = sorted(best_primes)   # CHANGED: sort after converting view

    # Output formatting rule (if 6 or more primes)
    if max_count >= 6:
        display_primes = best_primes_sorted[:3] + best_primes_sorted[-3:]
    else:
        display_primes = best_primes_sorted

    return best_index, max_count, display_primes

# --------------------------
# PI constants as strings
# --------------------------
PI_10 = "3141592653"
PI_20 = "31415926535897932384"
PI_40 = "314159265358979323846264338327950288419"
PI_60 = "314159265358979323846264338327950288419716939937510582097"
PI_80 = "31415926535897932384626433832795028841971693993751058209749445923"
PI_100 = "3141592653589793238462643383279502884197169399375105820974944592307816406286"

# --------------------------
# Test cases
# --------------------------
test_cases = [
    ("Case 1", PI_10, 2, 50),
    ("Case 2", PI_10, 4, 5000),
    ("Case 3", PI_20, 6, 5000),
    ("Case 4", PI_20, 8, 500000),
    ("Case 5", PI_40, 8, 500000),
    ("Case 6", PI_40, 10, 50000000),
    ("Case 7", PI_60, 12, 500000000),
    ("Case 8", PI_60, 14, 500000000),
    ("Case 9", PI_80, 16, 5000000000),
    ("Case 10", PI_100, 20, 500000000000),
]

# --------------------------
# Run test cases
# --------------------------
for label, string_input, window_size, N in test_cases:
    print(label)
    start_time = time.time()
    result = prime_dense_window(string_input, window_size, N)
    end_time = time.time()
    print("Output:", result)
    print("Execution time:", end_time - start_time, "seconds")
    print("-" * 40)