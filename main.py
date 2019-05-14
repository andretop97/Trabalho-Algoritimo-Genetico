from Requisito import *
def gerar_gene(qReq,qRel):
    cromossomo = [0] * qReq
    for i in range(qReq):
        cromossomo[i] = int(random.random()*qRel)
    return cromossomo

r0 = Requisito(1, 60, 3)
r1 = Requisito(2, 40, 6)
r2 = Requisito(3, 40, 2)
r3 = Requisito(4, 30, 6)
r4 = Requisito(5, 20, 4)
r5 = Requisito(6, 20, 8)
r6 = Requisito(7, 25, 9)
r7 = Requisito(8, 70, 7)
r8 = Requisito(9, 50, 6)
r9 = Requisito(10, 20, 6)

listaReq = [r0,r1,r2,r3,r4,r5,r6,r7,r8,r9]
qReq = len(listaReq)
print(qReq)

release1 = Realise(1,125)
reliase2 = Realise(2,125)
reliase3 = Realise(3,125)

listaRel = [release1,reliase2,reliase3]
qRel = len(listaRel)
print(qRel)
g = Gene(gerar_gene(qReq,qRel))
print(g)

