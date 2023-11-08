import sys

stdin = sys.stdin.read().strip()
print("".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(stdin)]), end="")
