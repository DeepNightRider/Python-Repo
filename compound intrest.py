def ci():
    p=1200
    r=2
    t=5.4
    A=p*((1+(r/100))**t)
    ci=A-p
    return ci
print(ci())

