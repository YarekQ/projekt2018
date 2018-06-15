def policz(zdanie:str,litera:str):
    if len(litera)!=1:
        raise ValueError("zmienna litera musi być jednoliterowym stringiem")
    else:
        return zdanie.count(litera)
