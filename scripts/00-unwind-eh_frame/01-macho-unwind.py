#!/usr/bin/env python3
import lief
import random

target = lief.parse("mbedtls_self_test.arm64.macho")

section = target.get_section("__unwind_info")
content = list(section.content)
random.shuffle(content)
section.content = content

target.write("unwind_mbedtls_self_test.arm64.macho")
