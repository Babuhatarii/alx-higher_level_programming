#!/usr/bin/python3
import py_compile
import sys

if __name__ == "__main__":
    # Compile the .pyc file into a .py file
    py_compile.compile('hidden_4.pyc')

    # Import the module
    import hidden_4

    # Get all the names defined in the module
    module_names = dir(hidden_4)

    # Filter and print the names that do not start with double underscores
    for name in sorted(module_names):
        if not name.startswith('__'):
            print(name)
