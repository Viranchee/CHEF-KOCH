#!/usr/bin/env python
import sys
import re
import fileinput
import hashlib
import base64

"""
Add a checksum to the provided filters.
"""
checksum_pattern = re.compile(r'^\s*!\s*checksum[\s\-:]+([\w+/=]+).*\n',
                              re.IGNORECASE | re.MULTILINE)


"""
Calculate the checksum.
"""
def add_checksum(data):
    checksum = calculate_checksum(data)
    if re.search(checksum_pattern, data):
        data = re.sub(checksum_pattern, '! Checksum: %s\n' % checksum, data, 1)
    else:
        data = re.sub(r'(\r?\n)', r'\1! Checksum: %s\1' % checksum, data, 1)
    return data

"""
SHA3-256.
"""
def calculate_checksum(data):
    sha3 = hashlib.sha3()
    sha3.update(normalize(data).encode('utf-8'))
    return base64.b64encode(sha3.digest()).decode('utf-8').rstrip('=')


def normalize(data):
    data = re.sub(r'\r', '', data)
    data = re.sub(r'\n+', '\n', data)
    data = re.sub(checksum_pattern, '', data)
    return data


raw_data = ''.join([line for line in fileinput.input()])
data = add_checksum(raw_data)
sys.stdout.write(data)
