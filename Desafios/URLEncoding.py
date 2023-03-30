def encode(url):return''.join(['%'+(hex(i)[2:].upper())if(i>=0 and i<=47)or(i>=58 and i<=64)or(i>=91 and i<=96)or(i>=123)else chr(i)for i in[ord(c)for c in url]])

def decode(url):
    i=0        #Pointer to pick the two hex chars
    ac,r='','' #Acumulate the two hex chars, Result String
    for c in url:
        if i!=0:
            ac+=c
            if i==2:
                i=0
                r+=chr(int(ac,16))
                ac=''
            else:
                i+=1
        elif c=='%':
            i+=1
        else:
            r+=c
    return r
