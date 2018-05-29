#!/usr/bin/env python
import re
import fileinput
import hashlib
import base64

"""
Validate checksum for all given rules.
"""
checksum_pattern = re.compile(r'^\s*!\s*checksum[\s\-:]+([\w+/=]+).*\n',
                              re.IGNORECASE | re.MULTILINE)


def validate_checksum(data):
    checksum = extract_checksum(data)
    if not checksum:
        raise Exception("This filter doesn't contain a checksum")
    expected_checksum = calculate_checksum(data)
    if checksum != expected_checksum:
        raise Exception('Wrong checksum: found {}, expected {}'
                        .format(checksum, expected_checksum))


def extract_checksum(data):
    match = re.search(checksum_pattern, data)
    return match.group(1) if match else None


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
validate_checksum(raw_data)
