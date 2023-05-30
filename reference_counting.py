import ctypes

counter = [1, 2, 3]
new_counter = counter
counter_address = id(counter)

def ref_count(address):
    return ctypes.c_long.from_address(address).value

print(ref_count(counter_address))