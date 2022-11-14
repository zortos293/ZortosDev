

def print_hello(loop :int):
    output = ""
    for i in range(loop):
       output += f"\nHello from function town {i+1}!"
    return output


print(print_hello(3))
print(print_hello(7))



