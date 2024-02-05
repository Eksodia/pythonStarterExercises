import math
import random
pi = 3.14


def ex1_funksioner(n):
    # Të shkruhet funksioni abs() për llogaritjen e vlerës absolute për një vlerë të caktuar.
    print("The absolute value of", n, "is =", abs(n))


def ex2_funksionet(a, b):
    # Të shkruhet funksioni hip() për llogaritjen e gjatësisë së hipotenuzës për trekëndëshin kënddrejtë,
    # nëse dihen gjatësia e brinjës a dhe brinjës b
    c = math.sqrt(pow(a, 2) + pow(b, 2))
    print("The hypotenuse with legs a =", a, "and b =", b, "is :", c)


def ex3_funksionet(r):
    # Të shkruhet programi për llogaritjen e sipërfaqes së rrethit duke përdorur funksionin pow()
    a = pi * pow(r, 2)
    print("The area of the circle with r ", r, "is =", a)


def ex4_funksionet(n):
    # Të shkruhet programi për llogaritjen e rrënjës katrore të një numri të dhënë, duke e përdorur
    # funksionin sqrt
    print("The square root of the input is = to:", math.sqrt(n))


def ex5_funkisonet(n):
    # Të shkruhet programi për llogaritjen e sinusit të një këndi të caktuar duke përdorur funksionin sin
    print("The sine of the angle is = to", math.sin(n))


def ex6_funksionet(n):
    # Të shkruhet programi për llogaritjen e kosinusit të një këndi të caktuar duke përdorur funksionin cos.
    print("The cosine of the angle is = to", math.cos(n))


def ex7_funksionet(n):
    # Të shkruhet programi për llogaritjen e tangjentit për një vlerë të caktuar, duke përdorur funksionin tan
    print("The tangent of the angle is = to", math.tan(n))


def ex8_funkionet(x):
    # Të shkruhet programi për llogaritjen e shprehjes y=ex duke përdorur funksionin exp
    y = math.exp(x)
    print("y exp =", y)


def ex9_funksionet(x):
    # Të shkruhet programi për llogaritjen e ln(x) për një vlerë të caktuar duke e përdorur funksionin log.
    print("ln(x) = ", math.log(x))


def ex10_funksionet(x, y):
    # Të shkruhet programi i cili përmes funksionit max e kthen si rezultat numrin më të madh në mes
    # numrave x dhe y.
    print("max of the number is =", max(x, y))


def ex11_funksitonet():
    # Krijo funksionin hipotenuza i cili llogarit gjatësinë e hipotenuzës së trekëndëshit kur dihet dihen
    # gjatësitë e dy krahëve tjerë. Funksioni duhet të ketë dy parametra hyrës të tipit double dhe të kthejë
    # hipotenuzën të tipit double
    x = float(input("Enter the first leg: "))
    y = float(input("Enter the second leg: "))
    c = float(math.sqrt(pow(x, 2) + pow(y, 2)))
    print("The hypotenuse is", c)


def ex12_funksionet(x, y):
    # Të shkruhet funksioni shumefishi i cili përcakton për çiftin e numrave të plotë nëse numri i dytë
    # është shumëfish i numrit të parë. Funksioni duhet të ketë dy parametra të tipit të plotë dhe të kthejë
    # si rezultat true ose false.
    print(bool(x % y == 0))


def ex13_funksionet(x, y, z):
    # Të shkruhet funksioni sekondat i cili merr tre parametra të tipit int (meqenëse koha është pozitive,
    # parametrat dhe funksioni të jenë të unsigned int). Funksioni të llogarit diferencën në mes dy kohëve
    # të dhëna dhe ta kthejë rezultatin në sekonda.
    print("Question not clear")


def ex14_funksionet():
    # Të shkruhet funksioni perfekt i cili përcakton nëse parametri i tij është numër perfekt. (Numri është
    # perfekt nëse shuma e faktorëve/plotpjesëtuesve të tij duke përfshirë edhe 1, por jo vetveten është
    # baras me numrin. p.sh 6=1+2+3). Duke shfrytëzuar funksionin perfekt të shtypen të gjithë numrat
    # perfekt nga 1 deri në 5000.
    i = 1
    while i < 500:
        perfect_sum = 0
        j = 1
        while j < i:
            if i % j == 0:
                perfect_sum += j
            j += 1
        if perfect_sum == i:
            print(perfect_sum)
        i += 1


def ex15_funksionet():
    # Të shkruhet funksioni distanca i cili llogarit distancën në mes dy pikave. Funksioni të ketë 4
    # parametra të tipit double dhe si rezultat të kthejë distancën e tipit double
    x1 = float(input("enter x1: "))
    y1 = float(input("enter y1: "))
    x2 = float(input("enter x2: "))
    y2 = float(input("enter y2: "))
    d = math.sqrt((pow(x2 - x1, 2) + pow(y2 - y1, 2)))
    print("The distance between the 2 points is =", d)


def ex16_funksionet():
    # Të shkruhet funksioni shumezimi i cili gjeneron në mënyrë të rastësishme dy numra nga 0-10 dhe
    # shfaq për prodhimin në mes e tyre
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(a, "*", b, "=", a * b)


def ex17_funksionet():
    # Të shkruhet programi i cili përmes funksionit aritmetika kryen veprimet e mbledhjes, zbritjes,
    # shumëzimit dhe pjesëtimit për dy numra të gjeneruar në mënyrë të rastësishme. Përmes funksionit
    # menyja të pyetet për veprimin që duhet të kryhet (mbledhje, zbritje, shumëzim, pjesëtim apo
    # kombinim i rastësishëm)
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    calculation = int(input("Enter witch calculation should be done (1 => +) (2 => -) (3 => / ) or (4 => *) 5 = "
                            "random: "))
    print(a, "and", b)
    if calculation == 1 or 2 or 3 or 4 or 5:
        if calculation == 5:
            calculation = random.randint(1, 4)
        if calculation == 1:
            print("Adding", a + b)
        elif calculation == 2:
            print("Subtracting", a - b)
        elif calculation == 3:
            print("Multiplying", a * b)
        elif calculation == 4:
            print("Dividing", a / b)
    else:
        print("Enter valid calculation")


def ex18_funksionet():
    # Të shkruhen 2 funksione me emrin maksimumi(). Njëri funksion të gjejë dhe ta shtyp numrin më të
    # madh në vektorin A(m), kurse funksioni tjetër numrin më të madh në matricën B(m,m). Vektori dhe
    # matrica gjatë deklarimit të iniciohen me vlera fillestare
    vector = [1, 2, 3, 4, 5, 1]
    maximum_vector = max(vector)
    print("Max of the vector:", maximum_vector)
    print()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    maximum_matrix = max(max(matrix))
    print("Max of the matrix:", maximum_matrix)


def ex19_funksionet():
    # Të shkruhen 3 funksione me emrin siperfaqja() të cilat llogarisin sipërfaqen e kubit, sferës dhe konit.
    # Funksionet të thirren për vlera të lexuara përmes tastierës.
    a = int(input("Enter the length of the edge of the cube: "))
    cubea = 6 * pow(a, 2)
    r = int(input("Enter the radius of the sphere: "))
    spherea = 4 * pi * pow(r, 2)
    rc = int(input("Enter the radius of the cone: "))
    hc = int(input("Enter the height of the cone: "))
    conea = pi * rc * (rc + math.sqrt(pow(hc, 2) + pow(rc, 2)))
    print("The areas of the objects are CUBE =", cubea, " SPHERE =", spherea, "and CONE =", conea)
