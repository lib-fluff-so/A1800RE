import re
import os

print("Finding headers...")

a = open("rom/rom_dump.bin", "rb")
g = a.read()
ma = re.finditer(bytes.fromhex("803e"), g)
mab = list(re.finditer(bytes.fromhex("803e"), g))

print(f"Headers found!")

i = 0

for t in ma:
    i += 1
    p1 = t.start() - 4
    try:
        p2 = mab[i].start() - 5
    except IndexError:
        p2 = os.path.getsize("rom/rom_dump.bin") - 1

    print(p1, p2)

    file = a

    file.seek(p1, 0)
    out = file.read(p2 - p1)

    with open("splitted/"+"out"+str(i)+".a18", "wb") as outfile:
        outfile.write(out)

a.close()
outfile.close()
