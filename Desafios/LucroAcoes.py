def CalcularLucro(acoes):
    x=acoes[0]
    mLucro=0
    for i in range(len(acoes)):
        acao=acoes[i]
        y=acao
        if x>acao:x=acao
        lucro=y-x
        if mLucro<lucro:mLucro=lucro
    return -1 if mLucro==0 else mLucro

print(CalcularLucro([44,30,24,32,35,30,40,38,15]))
print(CalcularLucro([10,9,8,2]))
print(CalcularLucro([10,12,4,5,9]))
print(CalcularLucro([14,20,4,12,5,11]))
# [44,30,24,32,35,30,40,38,15]  16
# [10,12,4,5,9]                  5
# [14,20,4,12,5,11]              8
# [10,9,8,2]                    -1
