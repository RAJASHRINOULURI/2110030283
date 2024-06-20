from flask import Flask, jsonify
from sympy import isprime
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Utility functions
def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if isprime(num):
            primes.append(num)
        num += 1
    return primes

def generate_fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[2:]  # exclude the first two numbers (0 and 1)

def generate_even_numbers(n):
    return [2 * i for i in range(1, n + 1)]

def generate_random_numbers(n, start=1, end=100):
    return [random.randint(start, end) for _ in range(n)]

@app.route('/test/primes', methods=['GET'])
def test_primes():
    primes = generate_primes(5)  # generate first 5 primes for testing
    return jsonify({"numbers": primes})

@app.route('/test/fibo', methods=['GET'])
def test_fibo():
    fibo = generate_fibonacci(6)  # generate first 6 fibonacci numbers for testing
    return jsonify({"numbers": fibo})

# REST API endpoint
@app.route('/numbers/<string:number_id>', methods=['GET'])
def calculate_average(number_id):
    numbers = get_numbers(number_id)
    if numbers is None:
        return jsonify({"error": "Invalid number ID"}), 400
    average = sum(numbers) / len(numbers) if numbers else 0
    return jsonify({"average": average, "numbers": numbers})

def get_numbers(number_id):
    if number_id.startswith('p'):
        count = int(number_id[1:])
        return generate_primes(count)
    elif number_id.startswith('f'):
        count = int(number_id[1:])
        return generate_fibonacci(count)
    elif number_id.startswith('e'):
        count = int(number_id[1:])
        return generate_even_numbers(count)
    elif number_id.startswith('r'):
        count = int(number_id[1:])
        return generate_random_numbers(count)
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


