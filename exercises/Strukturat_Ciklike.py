
def ex1_struktura_ciklike(n):
    # Fë shkruhet programi për llogaritjen e faktorielit të shprehjes: F=(2n-1)!
    x = 2 * n - 1
    i = x
    factorial = 1
    while i > 1:
        factorial = factorial * i
        i -= 1
    else:
        print(x, "! =", factorial)


def ex2_struktura_ciklike():
    # Të shkruhet programi për shfaqjen e karaktereve të alfabetit amerikan në formë trekëndëshi si në
    # pamjen e mëposhtme duke e përdorur strukturën ciklike while.
    # A
    # B B
    # C C C
    # D D D D
    # E E E E E
    letters = ["A", "B", "C", "D", "E"]
    i = 0
    while i < len(letters):
        j = -1
        while j < i:
            print(letters[i], end=" ")
            j += 1
        print()
        i += 1


def ex3_struktura_ciklike():
    # Të shkruhet programi për numrimin e shifrave për numrin e futur përmes tastierës. Programi të
    # realizohet përdorur strukturës ciklike while.
    num = int(input("Please enter a integer number: "))
    print("The digits of", num, "are: ")
    while num >= 1:
        digit = int(num % 10)
        print(digit, end=" / ")
        num = int(num / 10)


def ex4_struktura_ciklike(n):
    # Të shkruhet programi për llogaritjen e shumës së numrave 3 + 5 + 7+... përmes strukturës ciklike dowhile.
    i = 0
    total = 0
    start = 3
    while i < n:
        total += start
        start += 2
        i += 1
    print("The total sum for n=", n, "iteration of 3+5+7+.. is =", total)


def ex5_struktura_ciklike(n):
    # Të shkruhet programi për llogaritjen e shumës së katrorëve të numrave tek dhe kubeve të numrave
    # çift nga 1 deri në n duke e përdorur strukturën ciklike do while
    i = 1
    total = 0
    while i <= n:
        if i % 2 != 0:
            total = total + pow(i, 2)
        else:
            total = total + pow(i, 3)
        i += 1

    print("SUM = ", total)


# def ex6_struktura_ciklike(): SAME EX as EX2


def ex7_struktura_ciklike(num):
    # Të shkruhet programi për konvertimin e numrit nga sistemi decimal në sistemin binar.
    if num >= 1:
        ex7_struktura_ciklike(num // 2)
    print(num % 2, end='')


def ex8_struktura_ciklike(n):
    # Të shkruhet programi për konvertimin e numrit nga sistemi decimal në sistemin oktal
    octalNum = [0] * 100
    i = 0

    while n != 0:
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1

    for j in range(i - 1, -1, -1):
        print(octalNum[j], end="")


def ex9_struktura_ciklike():
    # Të shkruhet programi për shfaqjen e karaktereve të alfabetit amerikan në formë trekëndëshi si në
    # pamjen e mëposhtme duke e përdorur strukturën ciklike for
    # A
    # B B
    # C C C
    # D D D D
    # E E E E E
    letters = ["A", "B", "C", "D", "E"]
    i = 0
    for letter in letters:
        j = -1
        while j < i:
            print(letter, end=" ")
            j += 1
        print()
        i += 1


def ex10_struktura_ciklike():
    # Të shkruhet programi për shfaqjen e piramidës në pozicionin si në pamjen e mëposhtme. Numri i
    # rreshtave të përcaktohet përmes tastierës. Të realizohet përmes strukturës ciklike for.
    # * * * * *
    # * * * *
    # * * *
    # * *
    # *
    i = int(input("Enter the number of ROWS: "))
    while i > 0:
        j = i
        while j > 0:
            print(" ", end=" * ")
            j -= 1
        print()
        i -= 1


def ex11_struktura_ciklike():
    # Të shkruhet programi për shfaqjen e piramidës të ndërtuar me numra si në pamje. Numri i rreshtave
    # të përcaktohet përmes tastierës. Të realizohet përmes strukturës ciklike while.
    # 1 2 3 4 5
    # 1 2 3 4
    # 1 2 3
    # 1 2
    # 1
    i = int(input("Enter the number of ROWS: "))
    while i > 0:
        j = i
        while j > 0:
            print(j, end="  ")
            j -= 1
        print()
        i -= 1


def ex12_struktura_ciklike():
    # Të shkruhet programi për shfaqjen e piramidës të ndërtuar me ylla (*) si në pamje. Numri i rreshtave
    # të përcaktohet përmes tastierës
    #         *
    #       * * *
    #     * * * * *
    #   * * * * * * *
    # * * * * * * * * *
    i = int(input("Enter the number of ROWS: "))
    a = 0
    while a < i:
        j = i
        while j > a:
            print(end=" ")
            j -= 1
        k = -1
        while k < a:
            print("*", end=" ")
            k += 1
        print()
        a += 1


def ex13_struktura_ciklike():
    # Të shkruhet programi për shfaqjen e piramidës të ndërtuar me numra si në pamje.
    #         1
    #       2 3 2
    #     3 4 5 4 4 3
    #    4 5 6 7 6 5 4
    #   5 6 7 8 9 8 7 6 5
    rows = int(input("Enter number of ROWS: "))

    k = 0
    count = 0
    count1 = 0

    for j in range(1, rows + 1):
        for space in range(1, (rows - j) + 1):
            print("  ", end="")
            count += 1

        while k != ((2 * j) - 1):
            if count <= rows - 1:
                print(j + k, end=" ")
                count += 1
            else:
                count1 += 1
                print(j + k - (2 * count1), end=" ")
            k += 1

        count1 = count = k = 0
        print()


def ex14_struktura_ciklike():
    # Të shkruhet programi për shfaqjen e piramidës të ndërtuar me numra si në pamje. X made out of tiny x
    rows = int(input("Enter number of ROWS you want the X to be: "))

    for i in range(rows):
        for j in range(rows):
            if (i == j) or ((rows - j - 1) == i):
                print('x', end='')
            else:
                print(' ', end='')
        print('')


def ex15_struktura_ciklike():
    # Të shkruhet programi për mbledhjen e numrave tek nga 1 deri në n. Për i>15 të ndërpritet struktura
    # ciklike duke përdorur urdhrin break
    n = int(input("ENTER n to find sum of odd: "))
    i = 0
    s = 0
    while i < n:
        if i > 15:
            break
        if i % 2 != 0:
            s += i
        i += 1
    print("SUM = ", s)


def ex16_struktura_ciklike():
    #  Të shkruhet programi për mbledhjen e numrave të njëpasnjëshëm prej 1 deri në n. Për s>99 të
    # ndërpritet struktura ciklike duke përdorur urdhrin break
    n = int(input("ENTER n to find sum of odd: "))
    i = 0
    s = 0
    while i < n:
        if s > 99:
            break
        s += i
        i += 1
    print("SUM = ", s)


def ex17_struktura_ciklike():
    # Të shkruhet programi për shfaqjen e numrave të njëpasnjëshëm nga 1 deri në 10. Për i=5 të
    # kapërcehet hapi duke përdorur urdhrin continue.
    i = 1
    while i <= 10:
        if i == 5:
            i += 1
            continue
        print(i)
        i += 1


def ex18_struktura_ciklike():
    # Të shkruhet programi për llogaritjen e vlerës së funksionit dhe të bëhet kapërcimi i hapit përmes
    # urdhrit continue për i=3.
    n = int(input("Enter the value of n: "))
    m = int(input("Enter the value of m: "))
    summ = 0
    i = 1
    while i <= n + m:
        if i == 3:
            i += 1
            continue
        summ += (4 * m - n * i)
        i += 1

    func = (2 * pow(m, 4)) + (n / 2 * summ)
    print("Y=2m^4+n/2* SUM[4m - ni] {from i=1 to i=m+m (i=!3)} = ", func)


def ex19_struktura_ciklike():
    # Të shkruhet programi për shfaqjen e tabelës së shumëzimit nga 1 deri në 10 në formë tabelare
    i = 1
    while i <= 10:
        j = 1
        while j <= 10:
            print(j * i, end=" | ")
            j += 1
        print()
        i += 1
