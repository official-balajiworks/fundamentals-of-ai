import random
import math

# Objective: maximize f(x) = x * sin(x)
fitness = lambda x: x * math.sin(x)
decode = lambda b: int(b, 2)

# Generate initial population using list comprehension
def init_population(size, length):
    return [''.join(random.choice('01') for _ in range(length)) for _ in range(size)]

# Selection using sorted() and slicing
def selection(pop):
    return sorted(pop, key=lambda c: fitness(decode(c)), reverse=True)[:2]

# Single-point crossover
def crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)
    return (p1[:point] + p2[point:], p2[:point] + p1[point:])

# Mutation using join() + generator expression
def mutate(ch, rate=0.1):
    return ''.join(
        '1' if bit == '0' and random.random() < rate else
        '0' if bit == '1' and random.random() < rate else bit
        for bit in ch
    )

# Main Genetic Algorithm
def genetic_algorithm(size=6, length=5, generations=8):
    pop = init_population(size, length)
    for gen in range(generations):
        decoded = list(map(decode, pop))
        fits = list(map(fitness, decoded))
        
        print(f"\nGeneration {gen}: {pop}")
        print("Fitness:", [round(f, 3) for f in fits])

        # Select parents using built-ins
        p1, p2 = selection(pop)

        # Generate children using map() and list comprehension
        children = []
        while len(children) < len(pop):
            c1, c2 = crossover(p1, p2)
            children.extend(map(mutate, (c1, c2)))

        # Elitism: keep top individuals
        pop = sorted(children, key=lambda c: fitness(decode(c)), reverse=True)[:len(pop)]

    # Get best chromosome using max() + lambda
    best = max(pop, key=lambda c: fitness(decode(c)))
    x = decode(best)
    print(f"\nBest Solution: {best}  x={x}  fitness={round(fitness(x), 3)}")

# Run the algorithm
genetic_algorithm()
