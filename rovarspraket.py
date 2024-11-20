def rovarspraket(n):
    thislist = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    text = n
    text = text.lower()
    rovartext = ''
    for i in range (0, len(text)):
        if text[i] in thislist:
            rovartext = rovartext+text[i]+'o'+text[i]  
        else:
                rovartext = rovartext+text[i]
    print(rovartext)            
        

rovarspraket("hello")