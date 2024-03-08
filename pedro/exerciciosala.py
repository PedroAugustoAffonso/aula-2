def maior(n1, n2):
    if n1 > n2:
        return n1
    return n2

maior(n1, n2)
maior(n1, n2)

print("_"*30)

def e_vogal(letra):
    match letra:
        case "a"| "e"|"i"|"o"|"u":
            return "é vogal"
    return "é consoante"




print("_"*30)

def nota_e_valida(nota):
    return 0<= nota <=10

def aprovacao(ap1, ap2, ap3):
    media = (ap1+ap2+ap3)/3
    if nota_e_valida(ap1) and nota_e_valida(ap2) and nota_e_valida(ap3):
        if 7<= media < 10:
            print( "aprovado")
        elif media == 10:
            print("aprovado com distincao")
        elif 0<= media <7:
            print("reprovado")
    else:
        print ("nota invalida")

aprovacao(10,10,10)
aprovacao(10,8,9)
aprovacao(6,5,5)
aprovacao(11,19,10)
aprovacao(11,11,11)
aprovacao(-1,1,10)

print("_"*30)

