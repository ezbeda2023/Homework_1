"""Find all Pythagorean triples whose side lengths are at most n."""


def find_Pythagorean(n):
    """Return all unique Pythagorean triples (a, b, c) up to n."""
    triples = []

    for a in range(1, n + 1):
        # Starting at a prevents duplicate triples such as (3, 4, 5)
        # and (4, 3, 5).
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                if a**2 + b**2 == c**2:
                    triples.append((a, b, c))

    return triples


n = int(input("Enter a positive integer n: "))

for triple in find_Pythagorean(n):
    print(triple)
