def riadok(n, text=''):
        if text != '':
            text = ' '+text+' '
        lava = (n - len(text))//2
        prava = n - len(text) - lava
        print("*"*lava+text+"*"*prava)

riadok(40)
riadok(40,text="Eduard Mráz")
riadok(40,text="Prší")
riadok(40,text="-")
riadok(40,text="Prší, prší len sa leje")
riadok(40,text="Nezatváraj milá dvere")
riadok(40,text="Milá má dušá má")
riadok(40,text="Nezatváraj pred nama")
riadok(40)
