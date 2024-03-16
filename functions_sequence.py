def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Start with the first two terms
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence[:n]

def main():
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))
    fibonacci_sequence = generate_fibonacci(n)
    print("Generated Fibonacci sequence:", fibonacci_sequence)

if __name__ == "__main__":
    main()
