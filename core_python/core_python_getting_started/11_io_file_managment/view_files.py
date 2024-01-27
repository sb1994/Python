import sys

# needs to be run in f
f = open(
    sys.argv[1],
    mode="rt",
    encoding="utf-8",
)

for line in f:
    print(line)
f.close()
