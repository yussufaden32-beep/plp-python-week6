def unbreakable_number(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return "Invalid input"


if __name__ == "__main__":
    print(unbreakable_number("100"))
    print(unbreakable_number("abc"))
    print(unbreakable_number(None))