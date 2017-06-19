# coding: utf-8

import sys

from unzip import unzip_file


def main(path_file):
    unzip_file(path_file)

if __name__ == "__main__":
    main(sys.argv[1])


