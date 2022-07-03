#!/usr/bin/env python3
import lief
import random

target = lief.parse("mbedtls_self_test.arm64.elf")
for sname in [".eh_frame", ".eh_frame_hdr"]:
    section = target.get_section(sname)
    if section is None:
        continue
    content = list(section.content)
    random.shuffle(content)
    section.content = content

target.write("eh-frame_mbedtls_self_test.arm64.elf")
