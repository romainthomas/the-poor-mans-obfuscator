#!/usr/bin/env python3
"""
This script creates exports with names taken from the
unstripped version of the mbedtls binary
"""

import lief
import random

target: lief.ELF.Binary = lief.parse("mbedtls_self_test.arm64.elf")
non_striped = lief.parse("mbedtls_self_test.nostrip.arm64.elf")

SYMBOLS = [s.name for s in non_striped.symbols if s.name.startswith("mbedtls_")]

for idx, function in enumerate(target.functions):
    if len(SYMBOLS) == 0:
        break

    sym = random.choice(SYMBOLS)
    SYMBOLS.remove(sym)
    target.add_exported_function(function.address, sym)

target.write("02-mbedtls_self_test.arm64.elf")
