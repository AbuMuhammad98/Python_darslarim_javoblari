def shortcut( s ):
    # ...
    v = ('a', 'e', 'i', 'o', 'u')
    for i in s:
        if i in v:
            s = s.replace(i,"")
    return s