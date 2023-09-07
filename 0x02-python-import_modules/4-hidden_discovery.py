#!/usr/bin/python3
import py_compile
import dis

# Decompile the .pyc(python compile) file and get the code object
py_compile.compile("hidden_4.pyc", cfile="hidden_4_compiled.py")
import hidden_4_compiled

# Print the names that do not start with '__'
names = [name for name in dir(hidden_4_compiled) if not name.startswith("__")]
for name in sorted(names):
    print(name)
