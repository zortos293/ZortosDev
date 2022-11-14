def print_tabel (nummer :int):
    output = ""
    for i in range(10):
        output += f"\n {i+1} x {nummer} = {nummer*(i+1)}"
    return output
print(print_tabel(3))