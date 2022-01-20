def main():
    from ape import convert

    converted_val = convert("8.1 API3", int)
    print(converted_val)  # prints 10000000000000000000

    converted_val = convert("8.234 LINK", int)
    print(converted_val)
