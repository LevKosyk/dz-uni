from pathlib import Path

data = Path(__file__).parents[2] / "data"

with open(data / "words.txt", encoding="utf-8") as f:
    for ryadok in f:
        print(ryadok.rstrip().upper())

print()

sum = 0.0
number = 0
with open(data / "mbox-short.txt", encoding="utf-8") as f:
    for ryadok in f:
        if not ryadok.startswith("X-DSPAM-Confidence:"):
            continue
        sum += float(ryadok.split(":")[1])
        number += 1

print(number)
print(sum)
