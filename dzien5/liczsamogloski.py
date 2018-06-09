def licz(mtext: str)->int:
    """

    :param string:
    :return:
    """
    mtext=mtext.strip().lower()
    samog=["a","e","i","u"]
    counter=0
    for i in mtext:
        if mtext[i] in samog:
            counter=counter+1
    return counter

print(licz("zenek"))
