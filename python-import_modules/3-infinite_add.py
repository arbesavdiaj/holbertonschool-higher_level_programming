#!/usr/bin/python3
if __name__ == "__main__":
    import sys

sum = 0
max_length = len(sys.argv) - 1
for i in range(1, max_length + 1):
    sum += int(sys.argv[i])
print(sum)
