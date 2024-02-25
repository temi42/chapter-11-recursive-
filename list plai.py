def pali(n):
    if n == "":
        return True
    elif n[0].lower() != n[-1].lower():
        return False
    else:
        return pali(n[1:-2])

pal= pali("temidayo")
print(pal)

