from Requisito import *

r0 = Requisito(1, 60, 3,(3*10+4*10+2*5))
r1 = Requisito(2, 40, 6, (3*8+4*10+2*6))
r2 = Requisito(3, 40, 2, (3*6+4*4+2*8))
r3 = Requisito(4, 30, 6, (3*5+4*9+2*1))
r4 = Requisito(5, 20, 4, (3*7+4*7+2*5))
r5 = Requisito(6, 20, 8, (3*8+4*6+2*2))
r6 = Requisito(7, 25, 9, (3*6+4*6+2*4))
r7 = Requisito(8, 70, 7, (3*9+4*8+2*3))
r8 = Requisito(9, 50, 6, (3*6+4*7+2*5))
r9 = Requisito(10, 20, 6, (3*10+4*10+2*7))

listaReq = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9]
qReq = len(listaReq)

release1 = Realise(1, 125)
reliase2 = Realise(2, 125)
reliase3 = Realise(3, 125)

listaRel = [release1, reliase2, reliase3]
qRel = len(listaRel)

elite = []

def gerar_gene(qReq,qRel):
    cromossomo = [0] * qReq
    for i in range(qReq):
        numero = int(random.random()*(qRel+1))
        if(numero==1):
            if( release1.Veri_cheia(listaReq[i].custo)):
                release1.add_custo(listaReq[i].custo)
            else:
                numero = random.choice([0,2,3])
        if(numero==2):
            if (reliase2.Veri_cheia(listaReq[i].custo)):
                reliase2.add_custo(listaReq[i].custo)
            else:
                numero = random.choice([0, 3])
        if(numero==3):
            if (reliase3.Veri_cheia(listaReq[i].custo)):
                reliase3.add_custo(listaReq[i].custo)
            else:
                numero = 0
        cromossomo[i]=numero

    #print(release1.custoAtual,reliase2.custoAtual,reliase3.custoAtual)
    release1.zerar_custo()
    reliase2.zerar_custo()
    reliase3.zerar_custo()
    return cromossomo

def gerar_individuo():
    g = Gene(gerar_gene(qReq,qRel))
    g.score(listaReq,qRel)
    return g

def gerar_população(tamanho):
    populacao = []
    for i in range(tamanho):
        populacao.append(gerar_individuo())
    return populacao

def crusar_individuo(individuo1, individuo2):
    indice = int(random.random()*len(individuo1.gene))
    aux = [release1.get_customax(),reliase2.cutosmax,reliase3.cutosmax]
    filho1 = []
    filho2 = []
    filho1.extend(individuo1.parte_inferior(indice))
    filho1.extend(individuo2.parte_superior(indice))
    f1=Gene(filho1)
    filho2.extend(individuo2.parte_inferior(indice))
    filho2.extend(individuo1.parte_superior(indice))
    f2=Gene(filho2)
    i=0
    for numero in f1.get_gene():
        f1.mutacao(taxa_mutacao,i)
        if(f1.get_gene()[i]==1):
            if (aux[0] - listaReq[i].custo >= 0):
                aux[0]=aux[0]-listaReq[i].custo
            else:
                f1.corrigir_gene(i,0)
        if(f1.get_gene()[i]==2):
            if (aux[1] - listaReq[i].custo >= 0):
                aux[1] = aux[1] - listaReq[i].custo
            else:
                f1.corrigir_gene(i,0)
        if(f1.get_gene()[i]==3):
            if (aux[2] - listaReq[i].custo >= 0):
                aux[2] = aux[2] - listaReq[i].custo
            else:
                f1.corrigir_gene(i,0)
        #print(release1.custoAtual,reliase2.custoAtual,reliase3.custoAtual)
        i=i+1
    i=0
    aux2 = [release1.get_customax(),reliase2.cutosmax,reliase3.cutosmax]

    for numero in f2.get_gene():
        f2.mutacao(taxa_mutacao,i)
        if(f2.get_gene()[i]==1):
            if(aux2[0]-listaReq[i].custo>=0):
                aux2[0] = aux2[0] - listaReq[i].custo
            else:
                f2.corrigir_gene(i,0)
        if(f2.get_gene()[i]==2):
            if (aux2[1] - listaReq[i].custo >= 0):
                aux2[1] = aux2[1] - listaReq[i].custo
            else:
                f2.corrigir_gene(i,0)
        if(f2.get_gene()[i]==3):
            if (aux2[2] - listaReq[i].custo >= 0):
                aux2[2] = aux2[2] - listaReq[i].custo
            else:
                f2.corrigir_gene(i,0)
        #print(release1.custoAtual,reliase2.custoAtual,reliase3.custoAtual)
        i=i+1
    f1.score(listaReq,qRel)
    f2.score(listaReq,qRel)
    filhos=[individuo1,individuo2,f1,f2]
    filhos.sort(key=Gene.fitness,reverse=True)
    del(filhos[2:])
    return filhos

def crusar_populacao(populacao):
    tamanho = (len(populacao)*taxa_cruzamento)//200
    if(tamanho//2==0):
        tamanho=tamanho+1
  #  del(populacao[tamanho:])
 #   tamanho = (len(populacao))//2
    populacao_r = []
    for i in range(tamanho):
        populacao_r.extend(crusar_individuo(populacao[2*i],populacao[2*i+1]))
    while(len(populacao_r) <  tamanho_populacao):
        populacao_r.append(gerar_individuo())
    populacao_r.sort(key=Gene.fitness,reverse=True)
    return populacao_r

def gerações(populacao , quantidade):
    populacao_r = populacao
    for i in range(quantidade):
        populacao_r =  crusar_populacao(populacao_r)

        media_populacao = 0
        for ind in populacao_r:
            media_populacao = media_populacao + ind.fitness
        media_populacao = media_populacao // tamanho_populacao
        print(i, populacao_r[0].fitness ,media_populacao)
    return populacao_r

def elitismo(populacao,nElite):
    if(elite == []):
        elite.append(populacao[:nElite])
    else:
        for i in range(elite):
            if(populacao[i].fitness >= elite[i].fitness):
                elite[i]=populacao[i]
taxa_mutacao = 80
taxa_cruzamento = 80
qGera = 100000
populacao_inicial = 100
tamanho_populacao = 100
nElite = 1
a = gerar_população(populacao_inicial)
a = gerações(a,qGera)
count = 0
for i in a[0].get_gene():
    if (i == 1):
        release1.add_custo(listaReq[count].custo)
    if (i == 2):
        reliase2.add_custo(listaReq[count].custo)
    if (i == 3):
        reliase3.add_custo(listaReq[count].custo)
    count = count +1
print(release1.custoAtual,reliase2.custoAtual,reliase3.custoAtual)


    # for i in range(50):
    #    a.append(gerar_individuo())

    # g = Gene(gerar_gene(qReq,qRel))
    # for i in a:
    #    print(i)
    #    print(i.fitness)