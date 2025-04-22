# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for i in range(99, 0, -1):
        if i == 1:
            print("1 bottle of milk on the wall, 1 bottle of milk.")
            print("Take one down and pass it around, no more bottles of milk on the wall.\n")
        elif i == 2:
            print("2 bottles of milk on the wall, 2 bottles of milk.")
            print("Take one down and pass it around, 1 bottle of milk on the wall.\n")
        else:
            print(f"{i} bottles of milk on the wall, {i} bottles of milk.")
            print(f"Take one down and pass it around, {i - 1} bottles of milk on the wall.\n")

    # Parte final fuera del bucle
    print("No more bottles of milk on the wall, no more bottles of milk.")
    print("Go to the store and buy some more, 99 bottles of milk on the wall.")

# Llama la función
number_of_bottles()
