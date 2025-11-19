#!/usr/bin/python3
import dis
import marshal

if __name__ == "__main__":
    with open("/tmp/hidden_4.pyc", "rb") as f:
        f.read(16)  # .pyc header at most recent versions
        code = marshal.load(f)  # load code object

    names = [name for name in code.co_names if not name.startswith("__")]
    for name in sorted(names):
        print(name)
