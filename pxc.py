import sys

def process(file):
    counts = {}
    f = open(file, 'r')
    while True:
        l = f.readline()
        if not l:
            break
        ws = l.split(' ')
        for w in ws:
            if w not in counts:
                counts[w] = 0
            counts[w] += 1
    return counts

if __name__ == "__main__":
    counts = process(sys.argv[1])
    print(f"counts: {counts}")