
def ex1_vektoret():
    # Të deklarohet fusha numerike një-dimensionale (vektori) me madhësi 5 dhe me pas anëtarët të
    # mbushen me vlerat e indeksit përmes strukturës ciklike for si dhe të shfaqen vlerat e anëtarëve duke
    # përdorur strukturën ciklike while.
    vector = []
    i = 0
    while i < 5:
        vector.append(i)
        i += 1
    for cell in vector:
        print(cell, end=" ")


def ex2_vektoret():
    # Të deklarohet vektori dite në të cilin do të ruhen numri i ditëve për secilin muaj dhe më pas të
    # shfaqet sa ditë i ka secili muaj.
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for days, month in zip(days_per_month, months):
        print(month, days)


def ex3_vektoret():
    # Të shkruhet programi për deklarimin, inicializimin dhe shfaqjen e vlerave të anëtarëve të vektorit
    # A(m)={1,-4,3,7,5,9}
    a = [1, -4, 3, 7, 5, 9]
    for cell in a:
        print(cell, end=" ")


def ex4_vektoret():
    # Të shkruhet programi për mbushjen e vektorit me 4 anëtarë. Mbushja të bëhet përmes tastierës. Pas
    # mbushjes të bëhet shfaqja e anëtarëve të vektorit
    vec = []
    i = 0
    while i < 4:
        data = input("Enter data for the vector: ")
        vec.append(data)
        i += 1
    for cell in vec:
        print(cell, end=" ")


def ex5_vektoret():
    # Të shkruhet programi i cili mbush vektorin me 8 anëtarë. Mbushja të realizohet me strukturën ciklike
    # while, kurse vlerat e anëtarëve të mbushen me kubin e indekseve. Shfaqja të bëhet me strukturën
    # ciklike for
    vec = []
    i = 0
    while i < 8:
        vec.append(pow(i, 3))
        i += 1
    for cell in vec:
        print(cell, end=" ")


def ex6_vektoret():
    # Të shkruhet programi i cili e llogarit shumën e anëtarëve të vektorit A(m)={3,1,6,8,2,9,3,6}
    vec = [3, 1, 6, 8, 2, 9, 3, 6]
    summ = 0
    for cell in vec:
        summ += cell
    print(summ)


def ex7_vektoret():
    # Të shkruhet programi i cili gjen anëtarin me vlerë më të vogël të vektorit A(m)={12,13,4,6,-8,6,-11,4}.
    vec = [12, 13, 4, 6, -8, 6, -11, 4]
    print(min(vec))


def ex8_vektoret():
    # Të deklarohet dhe të mbushet vektori[5] me katrorët e indekseve. Më pas të kërkohet për vlerën 4
    # nëse ekziston. Nëse gjendet dhe të shfaqet pozita ku është gjetur në të kundërtën të shfaqet mesazhi
    # se nuk është gjetur.
    vec = []
    i = 0
    msg = "4 not found"
    while i < 5:
        vec.append(pow(i, 2))
        i += 1
    for cell in vec:
        if cell == 4:
            msg = "Found 4 at index: ", vec.index(4)
            break
        else:
            continue
    print(msg)


def ex9_vektoret():
    # Të shkruhet programi i cili nga vektori i dhënë a[m]={2,4,-1,3,5,4} e krijon vektorin e ri b[m] me
    # renditje të kundërt nga vektori a[m].
    a = [2, 4, -1, 3, 5, 4]
    b = []
    x = len(a)
    while x > 0:
        x -= 1
        b.append(a[x])
    print(b)


def ex10_vektoret():
    # Të shkruhet programi i cili llogarit shumën e anëtarëve pozitiv dhe prodhimin e anëtarëve negativ
    # të vektorit të dhënë: a[m]={-2,-3,2,6,-8,33,-1,4}.
    vec = [-2, -3, 2, 6, -8, 33, -1, 4]
    prod = 1
    summ = 0
    for cell in vec:
        if cell >= 0:
            summ += cell
        else:
            prod *= cell
    print("sum + ", summ, "prod -", prod)


def ex11_vektoret(n, x):
    # Të formohet vektori A(n) duke llogaritur anëtarët ai përmes shprehjes së mëposhtme nëse dihet
    # vlera x dhe n
    vec = []
    i = 0
    while i < n:
        j = 0
        summ = 0
        if x >= 0:
            vec.append(pow(x, 2))
            i += 1
        else:
            while j <= i:
                summ += pow(i + j, 2)
                j += 1
            a1 = -x * summ
            vec.append(a1)
            i += 1
    print(vec)


def ex12_vektoret():
    # Të renditen anëtarët e vektorit A(m) sipas vlerës absolute duke filluar prej anëtarit me vlerë më të
    # madhe kah anëtari me vlerë me të vogël A[m]={5,1,-12,-5,16, 8,-16}, nëse m=10.
    vec = [5, 1, -12, -5, 16, 8, -16]

    def keyfunk(value):
        return abs(value)

    vec.sort(key=keyfunk, reverse=True)
    print(vec)


def ex13_vektoret():
    # Të formohet vektori C(m+2+n) nga anëtarët e vektorit A[m], vektorit me anëtar 0 dhe anëtarët e
    # vektori B[n]. Formimi i vektorit të bëhet sipas modelit të mëposhtëm, nëse A[m]={10,20,30,40}
    # dhe B[n]={-1,-2,-3,-4}
    a = [10, 20, 30, 40]
    b = [-1, -2, -3, -4]
    c = [0, 0]
    vec = a + c + b
    print(vec)


def ex14_vektoret():
    # Të shkruhet programi për numërimin e anëtarëve pozitiv dhe negativ të vektorit të dhënë A[m]=
    # {2,-3,-7,4,1,-2,2}
    vec = [2, -3, -7, 4, 1, -2, 2]
    neg = []
    poz = []
    for cell in vec:
        if cell >= 0:
            poz.append(cell)
        else:
            neg.append(cell)
    print("Positive:", poz)
    print("Negative:", neg)


def ex15_vektoret():
    # Të shkruhet programi për gjetjen e anëtarit me vlerë minimale për vektorin e dhënë a[m]={-12,3,22,6,-8,33,-18,4}
    vec = [-12, 3, 22, 6, -8, 33, -18, 4]
    print(min(vec), max(vec))


def ex16_vektoret(x):
    # Të shkruhet programi për numërimin e anëtarëve negativ të vektorit të dhënë a[m]={2,-1,8,-2,-6,8,-4,0,9}
    # të cilët për nga vlera absolute janë më të mëdhenj se numri pozitiv x.
    vec = [2, -1, 8, -2, -6, 8, -4, 0, 9]
    for cell in vec:
        if cell < 0:
            if abs(cell) > x:
                print(cell, end=" ")


def ex17_vektoret(n, x):
    # Të formohet vektori A(n) duke llogaritur anëtarët ai përmes shprehjes së mëposhtme nëse dihet vlera x dhe n
    print("Same as ex11")
    ex11_vektoret(n, x)


def ex18_vektoret():
    # Të renditen anëtarët e vektorit A(m) sipas vlerës absolute duke filluar prej anëtarit me vlerë më të
    # madhe kah anëtari me vlerë me të vogël A[m]={5,1,-12,-5,16, 8,-16}, nëse m=10
    print("Same as ex12")
    ex12_vektoret()


def ex19_vektoret():
    # Formoni një program që lexon vlerat e vektorit me n elemente dhe shfaq vlerat dhe indekset e
    # elemetit më të vogël dhe më të madh
    n = int(input("Enter the length of the vector: "))
    vec = []
    i = 0
    while i < n:
        vec.append(int(input("Enter numbers to fill the vector: ")))
        i += 1
    print(min(vec), "min at index:", vec.index(min(vec)))
    print(max(vec), "max at index:", vec.index(max(vec)))
