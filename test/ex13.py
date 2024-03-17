import sys
script,  encoding, error = sys.argv

def main(file_name, encoding, errors):
    line = file_name.readline()
    if line:
        print_line(line, encoding, errors)
        return main(file_name, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<==>", cooked_string)


text = open("ex13_sample.txt", encoding="utf-8")
main(text, encoding, error)
