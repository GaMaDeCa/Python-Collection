#194979 = 1**5 9**5 4**5 9**5 7**5 9**5?
def findNarcNumbers(limit,init=0):
    #text=''
    for i in range(init,limit+1):
        si=str(i)
        li=len(si)
        ji=0
        stmp=''
        for j in range(li):
            ji+=int(si[j])**li
            stmp+=f'{si[j]}**{li} '
        if i==ji:print(f'{si} = {stmp}')#text+=f'{si} = {stmp}\n'
    #return text
