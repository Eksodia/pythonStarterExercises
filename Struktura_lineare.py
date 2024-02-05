pi = 3.14


def ex1_struktura_lineare():
    # Të shkruhet programi i cili llogarit shprehjet 5/2 + 5.5 dhe 12.6/2 + 4
    print("First Expression: ", 5 / 2 + 5.5)
    print("Second Expression:", 12.6 / 2 + 4)


def ex2_struktura_lineare():
    # Të shkruhet programi për llogaritjen e mesatares së 4 numrave të dhënë përmes tastierës
    num1 = float(input("Give first number: "))
    num2 = float(input("Give second number: "))
    num3 = float(input("Give third number: "))
    num4 = float(input("Give fourth number: "))
    print("The average is:", (num1 + num2 + num3 + num4) / 4)


def ex3_struktura_lineare(r):
    # Të shkruhet programi për llogaritjen e perimetrit të rrethit,nëse dihet rrezja r.
    # π të deklarohet si konstante, π=3.14
    circumference = 2 * pi * r
    print("The Circumference is: ", circumference)


def ex4_struktura_lineare(r1, r2):
    # Të shkruhet programi për llogaritjen e sipërfaqes së elipsit, nëse dihen rrezet r1 dhe r2.
    area = r1 * r2 * pi
    print("The area is:", area)


def ex5_struktura_lineare():
    # Të shkruhet programi për shfaqjen e disa numrave në dy shtylla
    col1 = [1, 2, 3, 4, 5]
    col2 = [6, 7, 8, 9, 10]
    i = 0
    while i < len(col1) or i < len(col2):
        print(col1[i], "  ", col2[i])
        i += 1


def ex6_struktura_lineare():
    # Të shkruhet programi i cili numrin e sekondave të lexuar përmes tastierës e kthen në formatin HH:MM:SS
    second = int(input("Give me the number of seconds to convert: "))
    minutes = int(second / 60)
    hours = int(minutes / 60)
    print("Format HH:", hours, " MM:", minutes % 60, " SS:", second % 60)


def ex7_struktura_lineare():
    # Të shkruhet programi i cili shumën e lexuar përmes tastierës e kthen në 50, 20,10, 5, 2 dhe 1 cent.
    money = int(input("Give the amount of money (cents) to covert into cents: "))
    cents50 = int(money / 50)
    cents20 = int((money % 50) / 20)
    cents10 = int((money % 50 % 20) / 10)
    cents5 = int((money % 50 % 20 % 10) / 5)
    cents2 = int((money % 50 % 20 % 10 % 5) / 2)
    cents1 = int(money % 50 % 20 % 10 % 5 % 2)
    print("Money in coins: /50 cent:", cents50, "  /20 cent:", cents20, "  /10 cent:", cents10,
          "  /5 cent:", cents5, "  /2 cent:", cents2, "  /1 cent", cents1)


def ex8_struktura_lineare(m1, m2, dist):
    k = 6.67 * pow(10, -18)
    power = k * (m1 * m2 / pow(dist, 2))
    print("The power is: ", power)
