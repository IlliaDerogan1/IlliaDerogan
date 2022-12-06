s  = input("Input text ")
PATTERN = "[a - z, A - Z] +"
rr = re.compile(PATTERN)
res = rr.findall(s)
print(res)

def printWords(fname, pattern):
    rgx = re.compile(pattern)
    with open(fname, 'r') as f:
        rows = f.readlines()
        for row in rows:
           for word in rgx.finditer(row):
               print(word, end = ' ')

SENTENCE = "[a - z, A - Z,\s, \.,\,] * [\.?!\b]"

SENTENCE = r"[A - ZA - ЯІЇЄ].*?[\.\!\?](?)"

if __name__ == "__main__":
    fn = "3.txt"
    rexp = SENTENCE
    printWords(fn, rexp)
