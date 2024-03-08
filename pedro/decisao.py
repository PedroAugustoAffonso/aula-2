""" estruturas de decisao
- if/elif/else
-match/case"""

def saudacao(turno):
    if turno == "M":
        print("Bom dia")
    else:
        if turno == "T":
            print("boa tarde")

def le_nome():
    nome=input("informe o seu nome ")
    #if nome == "":
    if not nome:
        print("Erro! Entrada invalida")

        return nome

#ternario
    def e_par(num):
        #if not num % 2
        if num % 2 == 0:
            return "é impar"
        return "é par"

def e_par2(num):
    return "é impar" if num % 2 else "é par"

def saudacao3(turno):
    match turno:
        case "M":
            print("bom dia")
        case "T":
            print("boa tarde")
        case "N":
            print("boa noite")
        case _: # default case, opcional
            print("dado invalido!")

print("_" * 30)
def aprovacao(conceito):
    match conceito:
        case "bom"|"otimo"|"excelente":
            return "aprovado"
        case _:
            return "reprovado"

aprovacao(bom)
aprovacao(otimo)
aprovacao(excelente)
aprovacao(ruim)