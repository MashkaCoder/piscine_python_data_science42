#!/usr/bin/env python
import os
import sys


def main():
    os.system("pip install beautifulsoup4 pytest")
    os.system('pip freeze')
    os.system('pip freeze > requirements.txt')


if __name__ == "__main__":
    try:
        if sys.base_prefix == sys.prefix:
            raise ValueError("This should run in env")
        else:
            main()
    except ValueError as e:
        print(e)