#!/usr/bin/env python3
"""
This scripts creates exports with names taken from the libc and
and addresses not aligned with the beginning of a function.
"""
import lief
import random

target: lief.ELF.Binary = lief.parse("mbedtls_self_test.arm64.elf")
libc = lief.parse("<ANDROID_HOME>/sdk/ndk/24.0.8215888/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/23/libc.so")

libc_symbols = {s.name for s in libc.exported_symbols}
libc_symbols -= {s.name for s in target.imported_symbols}
libc_symbols = list(libc_symbols)


for idx, function in enumerate(target.functions):
    if len(libc_symbols) == 0:
        break

    sym = random.choice(libc_symbols)
    libc_symbols.remove(sym)

    address = function.address
    address += random.randint(16, 32)
    address -= address % 4

    export = target.add_exported_function(address, sym)

    export.binding    = lief.ELF.SYMBOL_BINDINGS.GNU_UNIQUE
    export.visibility = lief.ELF.SYMBOL_VISIBILITY.INTERNAL

target.write("04-mbedtls_self_test.arm64.elf")
