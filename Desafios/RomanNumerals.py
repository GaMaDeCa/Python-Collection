roman_numerals=['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'III', 'II', 'I']
decimals=['1000', '900', '500', '400', '100', '90', '50', '40', '10', '9', '5', '4', '3', '2', '1']

def stringListToIntList(string_list):
    return [int(num) for num in string_list]

def createDictFromTwoLists(list_key,list_value):
    di={}
    for key,value in zip(list_key,list_value):
        di[key]=value
    return di

def ancientRomanListConverter(pop_list):
    for i in [1,2,3,4]:#9?
        pop_list.pop(i)
    return pop_list

modern_roman_decimal_dict=createDictFromTwoLists(stringListToIntList(decimals),roman_numerals)
ancient_roman_decimal_dict=createDictFromTwoLists(stringListToIntList(ancientRomanListConverter(decimals)),ancientRomanListConverter(roman_numerals))

def toRomanNumeral(integer,ancient=False):
    roman_dict=ancient_roman_decimal_dict if ancient else modern_roman_decimal_dict
    roman_numeral=''
    for d in roman_dict.keys():
        while integer>=d:
            roman_numeral+=roman_dict[d]
            integer-=d
    return roman_numeral

def toDecimal(roman_numeral):
    decimal=0
    special_dict={'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4}#TODO>Aprimorar, numeros romanos de duas casas causam erros.
    for cases,nums in special_dict.items():
        if roman_numeral.find(cases)!=-1:
            roman_numeral=roman_numeral.replace(cases,'')
            decimal+=nums
    for char in roman_numeral[::-1]:
        for key,value in modern_roman_decimal_dict.items():
            if value==char:
                decimal+=key
    return decimal
        

#toRomanNumeral(1974)
#'MCMLXXIV'

#toRomanNumeral(1974,ancient=True)
#'MDCCCCLXXIV'

#toDecimal('MDCCCCXIX')#Ancient Roman
#1919

#toDecimal('MCMXIX')# Modern Roman
#1919
