def toStr(n, base):
    conventString = "0123456789ABCDF"
    if n < base:
        return conventString[n]
    else:
        return toStr(n//base, base) + conventString[n%base]

a = toStr(7,2)
print(a)