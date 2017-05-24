# coding: utf-8

import os
import sys
import zipfile

import log


def unzip_file(path):
    try:
        log.print_log("File name: {}".format(path))
        if not os.path.exists(path):
            log.print_log("..: File {} not exist!!! :..".format(path))
            sys.exit(-1)
        else:
            zfile = zipfile.ZipFile(path)
            zfile.extractall()
            log.print_log("File Extracted!!!")
    except IOError:
        raise RuntimeError("Error unzipping file: {} ".format(path))