#!/usr/bin/env python3
"""
This script creates exports with random names.
"""

import lief
import random
import string
target: lief.ELF.Binary = lief.parse("mbedtls_self_test.arm64.elf")

for idx, function in enumerate(target.functions):
    name = "".join(random.choice(string.ascii_letters) for i in range(20))
    target.add_exported_function(function.address, name)

target.write("01-mbedtls_self_test.arm64.elf")
