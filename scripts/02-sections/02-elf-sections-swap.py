import lief
SWAP_LIST = [
    (".rela.dyn", ".data.rel.ro"),
    (".got",      ".got.plt"),
    #(".got",      ".data"),
    (".plt",      ".text"),
    (".dynsym",   ".gnu.version"),

    #(".preinit_array", ".bss"),
]

target = lief.parse("mbedtls_self_test.arm64.elf")

for (lhs_name, rhs_name) in SWAP_LIST:
    print(lhs_name, rhs_name)
    lhs = target.get_section(lhs_name).as_frame()
    rhs = target.get_section(rhs_name).as_frame()
    tmp = lhs.offset, lhs.size, lhs.name, lhs.type, lhs.virtual_address

    lhs.offset          = rhs.offset
    lhs.size            = rhs.size
    lhs.name            = rhs.name
    lhs.type            = rhs.type
    lhs.virtual_address = rhs.virtual_address

    rhs.offset          = tmp[0]
    rhs.size            = tmp[1]
    rhs.name            = tmp[2]
    rhs.type            = tmp[3]
    rhs.virtual_address = tmp[4]

target.write("swapped_mbedtls_self_test.arm64.elf")
