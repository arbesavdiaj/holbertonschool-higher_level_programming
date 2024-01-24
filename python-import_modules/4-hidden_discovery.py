#!/usr/bin/python3
import hidden_4 as secret_file

name = dir(secret_file)

for n in name():
    if n[0] != "__":
        print(n)
