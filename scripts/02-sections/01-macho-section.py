import lief

target = lief.parse("test_objc_arm64.macho")

__text  = target.get_section("__text")
__stubs = target.get_section("__stubs")

SHIFT = 0x100

__text.size             -= SHIFT
__stubs.offset          -= SHIFT
__stubs.virtual_address -= SHIFT
__stubs.size            += SHIFT

target.write("test_objc_arm64_shifted.macho")
