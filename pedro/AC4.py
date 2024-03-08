def ler_nome():
    return input("Informe o seu nome: ")

def ler_notas():
    ap1=    float(input("nota ap1:"))
    ap2=    float(input("nota ap2:"))
    asub=    float(input("nota as:"))
    ac=    float(input("nota ac:"))
    return ap1, ap2, asub, ac

def analisar_subst(ap1, ap2, asub):
    if asub > ap1:
        return asub, ap2
    if asub > ap2:
        return ap1, asub

    return ap1, ap2



def calcular_media(ap1, ap2, asub, ac):
    prova1, prova2 = analisar_subst(ap1, ap2, asub)
    return (prova1 + prova2) * 0.4 + ac * 0.2

def aluno_foi_aprovado(media):
    return media >= 7

def notas_sao_validas(ap1, ap2, asub, ac):
    if 0<= ap1 <= 10 and 0<= ap2 <= 10 and 0<= asub <= 10 and 0<= ac <= 10:
        return True
    return False





def main():
    nome= ler_nome()
    if nome:
        ap1, ap2, asub, ac= ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            media = calcular_media(ap1, ap2, asub, ac)
            if aluno_foi_aprovado (media):
                print("aluno foi aprovado")
            else:
                print("aluno foi reprovado")
main()