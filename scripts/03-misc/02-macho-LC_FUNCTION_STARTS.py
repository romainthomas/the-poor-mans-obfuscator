#!/usr/bin/env python3
import lief
import random

bin = lief.parse("./mbedtls_self_test.arm64.macho")
LC_FUNCTION_STARTS = bin[lief.MachO.LOAD_COMMAND_TYPES.FUNCTION_STARTS]

functions = [f for f in LC_FUNCTION_STARTS.functions]

for idx, f in enumerate(functions):
    if idx % 2 == 0:
        functions[idx] += 4 * 7
    else:
        functions[idx] -= 4 * 7

bin.write("./fstarts_mbedtls_self_test.arm64.macho")



