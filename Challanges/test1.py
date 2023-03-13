x = 100

while x > 0:
    x -= 1
    if x == 1:
        print(f"{x} bottles of beer on the wall, {x}  bottle of beer.Take one down and pass it around, no more bottles of beer on the wall.")
        x = 0
        break
    else:
        print(f"{x} bottles of beer on the wall, {x}  bottles of beer.Take one down and pass it around, {x -1}  bottles of beer on the wall.")
print("No more bottles of beer on the wall, no more bottles of beer.Go to the store and buy some more, 99 bottles of beer on the wall.")