def ex1_matricat():
# Të shkruhet programi në C++ për krijimin dhe mbushjen e matricës katrore A(m,m), nëse m=5.
# Anëtarët e matricës të mbushen sipas shprehjes aij=i
    matr = []
    m = 5

    for i in range(m):
        a = []
        for j in range(m):
            a.append(i)
        matr.append(a)

    print(matr)
    
def ex2_matricat():
    # Të shkruhet programi në C++ për krijimin dhe mbushjen e matricës katrore A(m,m), nëse m=3.
    # Mbushja të realizohet përmes strukturës ciklike while, kurse shfaqja e anëtarëve të realizohet përmes
    # strukturës ciklike do-while. Anëtarët e matricës të jepen përmes tastierës.
    matr = []
    m = 3
    i = 0
    while i < m:
        j = 0
        a = []
        while j < m:
            a.append(int(input("Enter number in {} {}:".format(i,j))))
            j += 1
        matr.append(a)
        i += 1

    print(matr)

def ex3_matricat():
    # Të shkruhet programi në C++ për mbushjen e matricës A(m,m), nëse m=6. Pjesa e brendshme e
    # matricës të mbushet me 0, kurse korniza e matricës të mbushet me 1.
    m = 6
    matr = []
    i = 0
    while i < m:
        j = 0
        a = []
        while j < m:
            if i and j != 0 and j != 5 and i != 5:
                a.append(1)
            else:
                a.append(0)
            j += 1
        matr.append(a)
        i += 1
    print(matr)


def ex4_matricat():
    #  Të formohet matrica katrore a(m,m) përmes shprehjes së mëposhtme, nëse m=8. Më pas të gjendet
    #  shuma absolute e anëtarëve mbi diagonalen kryesore dhe prodhimi i anëtarëve nën diagonale
    m = 8
    matr = []
    i = 0
    bellowDiag = 1
    aboveDiag = 0
    while i < m:
        j = 0
        a = []
        while j < m:
            if i < j:
                a.append(-2)
                aboveDiag += -2
            elif i > j:
                a.append(2)
                bellowDiag *= 2
            else:
                a.append(2*i+j)
            j += 1
        matr.append(a)
        i += 1
    print(aboveDiag, "sum", bellowDiag, "prod", "\n" ,matr)


def ex5_matricat():
    #Të formohet matrica katrore a(m,m) përmes shprehjes së mëposhtme, nëse m=8. Më pas të gjendet
    # prodhimi i anëtarëve të diagonales kur indekset e anëtarëve janë tek dhe shuma e anëtarëve kur indekset
    # janë çift. tek * cift +
    m = 8
    matr = []
    i = 0
    tek = 1
    cift = 0
    while i < m:
        j = 0
        a = []
        while j < m:
            if i < j:
                a.append(i)
            elif i > j:
                a.append(i - j)
            else:
                a.append(i + j)
                if i%2 == 0:
                    cift += (i+j)
                else:
                    tek *= (i+j)
            j += 1
        matr.append(a)
        i += 1
    print(cift, "sum", tek, "prod", "\n" ,matr)


def ex6_matricat(m: int):
    #Të formohet matrica C(2*m,2*m) duke i bashkuar matricën A(m,m) dhe B(m,m) në diagonale (si në
    # pamje). Matrica A të mbushet me 1-sha kurse matrica B me 2-sha. Anëtaret tjerë të jenë zero
    matr = []
    i = 0
    while i < m:
        j = 0
        a = []
        while j < m:
            if i < m/2 and j < m/2:
                a.append(1)
            elif i+1 > m/2 and j+1 > m/2:
                a.append(2)
            else:
                a.append(0)
            j += 1
        matr.append(a)
        i += 1
    print(matr)


def ex7_matricat():
    # Të formohen matrica A(m,m) e cila përmban notat e studentëve. Të llogaritet nota mesatare e secilit
    # student dhe ajo të ruhet në vektorin B(m,n).
    grades = [[10,7,9,10],[7,10,10,9],[9,8,9,9],[9,10,9,8]]
    medianVec = []
    for i in range(4):
        median = 0
        for j in range(4):
            median += grades[i][j]
        medianVec.append(median/4)
    print(medianVec)


def ex8_matricat(m: int):
    # Të krijohet matrica A(m,n). Anëtarët e matricës të mbushen sipas shprehjes së mëposhtme dhe më pas
    # të shtypen anëtarët e matricës së krijuar.
    matr = []
    i = 0
    while i < m:
        j = 0
        a = []
        while j < m:
            if i < j:
                a.append(i + j)
            elif i > j:
                a.append(i - j)
            else:
                a.append(0)
            j += 1
        matr.append(a)
        i += 1
    print(matr)

