import re
from collections import Counter
from pathlib import Path

data = Path(__file__).parents[2] / "data"

shablon = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)'
    r'.*?\[(?P<chas>[^\]]+)\]'
    r' "(?P<metod>[A-Z]+) (?P<shlyakh>\S+)[^"]*"'
    r' (?P<kod>\d{3}) '
)

ip = Counter()
kody = Counter()
pomylky = []
pomylky_shlyakhy = Counter()
ne_znaideno = Counter()
khto_404 = {}
rozibrano = 0
propushcheno = 0

with open(data / "access.log", encoding="utf-8") as f:
    for ryadok in f:
        m = shablon.search(ryadok)
        if not m:
            propushcheno += 1
            continue
        rozibrano += 1
        ip[m["ip"]] += 1
        kody[m["kod"]] += 1
        if m["kod"].startswith("5"):
            pomylky.append((m["chas"], m["shlyakh"]))
            pomylky_shlyakhy[m["shlyakh"]] += 1
        if m["kod"] == "404":
            ne_znaideno[m["shlyakh"]] += 1
            khto_404.setdefault(m["shlyakh"], set()).add(m["ip"])

print("Розібрано:", rozibrano)
print("Пропущено:", propushcheno)

print()
print("Топ-5 IP:")
for adresa, kilkist in ip.most_common(5):
    print(kilkist, adresa)

print()
print("Коди відповіді:")
for kod, kilkist in sorted(kody.items()):
    print(kod, kilkist)

print()
print("Помилки 5xx:", len(pomylky))
for chas, shlyakh in pomylky:
    print(chas, shlyakh)

print()
print("5xx по шляхах:")
for shlyakh, kilkist in pomylky_shlyakhy.most_common():
    print(kilkist, shlyakh)

print()
print("404 по шляхах (і хто ходить):")
for shlyakh, kilkist in ne_znaideno.most_common():
    print(kilkist, shlyakh, "—", ", ".join(sorted(khto_404[shlyakh])))
