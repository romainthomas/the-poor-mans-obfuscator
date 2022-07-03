import lief
import random

target: lief.ELF.Binary = lief.parse("mbedtls_self_test.arm64.elf")

dynsym = target.get_section(".dynsym").as_frame()

sizeof = dynsym.entry_size
osize = dynsym.size
nsyms = osize / sizeof
dynsym.size = sizeof * min(3, nsyms)

target.write("dynsym-mbedtls_self_test.arm64.elf")
