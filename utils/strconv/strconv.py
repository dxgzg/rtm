def initialUpper(s):
    if len(s) < 0:
        print(f"error str:{s} too short")
        exit(-1)

    s = s[0].upper() + s[1:]
    return s
