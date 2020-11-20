#!/usr/bin/env python3
#
# Compute the merkle hash of a file tree.
#
import sys
import os
import subprocess
from functools import reduce
import hashlib

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: merk.py [folder]")
    rootDir = sys.argv[1]
    hashes = []
    for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
        fileList.sort()
        hashes.append("".join([ subprocess.run(["sha256sum", os.path.join(dirName, file)], capture_output=True, encoding="utf-8").stdout.split(" ")[0] for file in fileList]))

    def hash(x, y):
        summer = hashlib.sha256()
        summer.update(bytes.fromhex(x + y))
        return summer.hexdigest()

    print(reduce(hash, hashes))
