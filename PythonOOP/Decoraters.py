# rozšíření decorateru někde jinde i wraper
# dekorater přidá něco před a za funkci. například měření času funkce. obalím funkci časem.

pricesUSD=[100.34,35,67.99,25.5]
print(pricesUSD)
USDrate=27.5
def toPriceNew(priceList):
    return list(map(lambda x: x*USDrate, priceList))

pricesUSD=[100.34,35,67.99,25.5]
print(pricesUSD)
def changePriceDecorator_v1(myFunction):
    print("Hello! Let's change your prices...")
    def simpleWrapper(argList):
        print("I've got list of prices with {} elements. Function starts wor")
        resutl=myFunction(argList)
        #resutlwithDisc=list(map(lambda x: x*(1-0.15), resutl)) #taky funguje jen kopíruji pro stejné hodnoty funkci
        resutlwithDisc = list(map(lambda x: x*USDrate, argList))
        print("Let's set a discount..")
        return resutl
    print("Konec ")
    return simpleWrapper

#pricesToGRN = changePriceDecorator_v1(toPriceNew)
print()
#print(pricesToGRN(pricesUSD))
print()
#print(toPriceNew(pricesUSD))


@changePriceDecorator_v1
def toPriceNew(priceList):
    #return list(map(lambda x: x*27.5, priceList))
    return list(map(lambda x: x*USDrate, priceList))

print(toPriceNew(pricesUSD)) # příklad volání dekorateru



