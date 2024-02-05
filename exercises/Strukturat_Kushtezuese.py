
def ex1_struktura_kushtezuese():
    # Të shkruhet programi duke përdorur operatorët && dhe || përmes të cilit kontrollohet vlera hyrëse
    # nga tastiera nëse është shkronjë apo jo, dhe shfaqet mesazhi perkatës
    text = input("Give an input to see if it a character: ")
    if len(text) > 1 or text.isdigit() or len(text) < 1:
        print("This is not a single character")
    else:
        print("This is a character")


def ex2_struktura_kushtezuese():
    # Të shkruhet programi i cili kontrollon nëse numri i dhënë përmes tastierës është më i madh se apo
    # më i vogël se 10.
    number = int(input("Enter a number: "))
    if number < 10:
        print("The number you entered is < 10")
    elif number > 10:
        print("The number you entered is > 10")
    else:
        print("The number you entered is equal to 10")


def ex3_struktura_kushtezuese():
    # Të shkruhet programi i cili cakton notën e studentit në varësi të pikëve të cilat merren si vlerë hyrëse
    # dhe shfaq mesazhin perkatës
    grade = int(input("Enter students grade: "))
    if grade in range(0, 50):
        print("0%")
    elif grade in range(50, 60):
        print("4%")
    elif grade in range(60, 70):
        print("8%")
    elif grade in range(70, 80):
        print("10%")
    elif grade in range(80, 90):
        print("12%")
    elif grade in range(90, 100):
        print("14%")
    else:
        print("Unknown value")


def ex4_struktura_kushtezuese():
    # Të shkruhet programi për konvertimin e inçëve në centimetra. Vlera e inçëve të jepet përmes
    # tastierës (1 inç=2.54 cm). Kahu i konvertimit të jetë me zgjedhje
    conversionmode = str(input("Select mode A for cm -> inch or B inch -> cm: "))
    cm_inch = "aA"
    inch_cm = "bB"
    if conversionmode in cm_inch:
        print("CM to INCH")
        length = int(input("Enter the length you want to convert: "))
        converted_length = length / 2.45
        print("Converted value: ", round(converted_length, 2), "cm")
    elif conversionmode in inch_cm:
        print("INCH to CM")
        length = int(input("Enter the length you want to convert: "))
        converted_length = length * 2.45
        print("Converted value: ", round(converted_length, 2), "inch")
    else:
        print("Please select correct option")
        ex4_struktura_kushtezuese()


def ex5_struktura_kushtezuese():
    # Të shkruhet programi për konvertimin e feets në cm. Vlera e centimetrave të jepet përmes tastierës.
    # Kahu i konvertimit të jetë me zgjedhje
    conversionmode = str(input("Select mode A for cm -> feet or B feet -> cm: "))
    cm_feet = "aA"
    feet_cm = "bB"
    if conversionmode in cm_feet:
        print("CM to FEET")
        length = int(input("Enter the length you want to convert: "))
        converted_length = length / 30.48
        print("Converted value: ", round(converted_length, 2), "cm")
    elif conversionmode in feet_cm:
        print("FEET to CM")
        length = int(input("Enter the length you want to convert: "))
        converted_length = length * 30.48
        print("Converted value: ", round(converted_length, 2), "FEET")
    else:
        print("Please select correct option")
        ex5_struktura_kushtezuese()


def ex6_struktura_kushtezuese():
    # Të shkruhet programi i cili konverton temperaturën nga Celsius në Fahrenheit dhe anasjelltas. Kahu i
    # konvertimit të jetë me zgjedhje
    conversionmode = str(input("Select mode A for celsius -> fahrenheit or B fahrenheit -> celsius: "))
    celsius_fahrenheit = "aA"
    fahrenheit_celsius = "bB"
    if conversionmode in celsius_fahrenheit:
        print("celsius to fahrenheit")
        temp = int(input("Enter the temp you want to convert: "))
        converted_temp = (temp * 9 / 5) + 32
        print("Converted value: ", round(converted_temp, 2), "Fahrenheit")
    elif conversionmode in fahrenheit_celsius:
        print("Fahrenheit to celsius")
        temp = int(input("Enter the temp you want to convert: "))
        converted_temp = (temp - 32) * 5 / 9
        print("Converted value: ", round(converted_temp, 2), "Celsius")
    else:
        print("Please select correct option")
        ex5_struktura_kushtezuese()


def ex7_struktura_kushtezuese():
    # Të shkruhet programi për përcaktimin e pagesës së punëtorit në bazë të numrit të orëve. Nëse
    # punëtori ka punuar më shumë se 40 orë në javë, atëherë ora paguhet sa 1.5 e çmimit normal
    wage_per_hr = 20
    nr_of_hrs_worked = int(input("Enter the number of hrs worked: "))
    if nr_of_hrs_worked > 40:
        overtime_hrs = nr_of_hrs_worked % 40
        wage = (wage_per_hr * 40) + (wage_per_hr * 1.5 * overtime_hrs)
    else:
        wage = wage_per_hr * nr_of_hrs_worked
    print("Wage to be fotten forW ", nr_of_hrs_worked, " is ", wage, "$")


def ex8_struktura_kushteuese():
    # Të shkruhet programi i cili llogarit pagën NETO (pn) nëse dihet paga BRUTO (pb).
    # a. Punëtorit i ndalen 5% të pagës bruto për trustin pensional (pen), kurse 5% i paguan
    # punëdhënësi.
    # b. Punëtorit i ndalet tatimi në pagë (tat) e i cili është i përshkallëzuar në varësi të pagës bruto
    # dhe llogaritet pasi të jetë hequr pagesa për trustin pensional.
    pb = int(input("Enter BRUTO wage"))
    value_to_tat = pb * 0.95
    if 0 <= value_to_tat <= 80:
        tat = 0
    elif value_to_tat <= 250:
        tat = value_to_tat * 0.04
    elif value_to_tat <= 450:
        tat = value_to_tat * 0.08
    elif value_to_tat > 450:
        tat = value_to_tat * 0.1
    else:
        print("Invalid input")
        return
    pn = value_to_tat - tat
    print("Neto wage is:", pn)


def ex9_struktura_kushtezuese():
    # Të shkruhet programi për mbledhjen, zbritjen, shumëzimin dhe pjesëtimin e dy numrave të plotë:
    # a. Nëse a dhe b janë pozitiv: shfaq a+b
    # b. Nëse a është pozitiv dhe b është negativ: shfaq a
    # c. Nëse a është negativ dhe b është pozitiv: shfaq b
    # d. Nëse a dhe b janë negativ: shfaq a*b
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if a >= 0 and b >= 0:
        print("A>0 B>0 we show A+B", a + b)
    elif a >= 0:
        print("B<0 we show A", a)
    elif b >= 0:
        print("A<0 we show B", b)
    else:
        print("A<0 B<0 we show A*B", a * b)


def ex10_struktura_kushtezuese():
    # Të shkruhet programi duke përdorur IF, &&, || dhe != për të llogaritur shprehjen (A && B || C) &&!D
    # nëse dihet se: A=(0, 5, 10, 15…) ; B= (më i vogël se 100); C= (0, 3, 6, 9…); D <> 6
    A = int(input("Enter the value of A"))
    B = int(input("Enter the value of B"))
    C = int(input("Enter the value of C"))
    D = int(input("Enter the value of D"))

    if A % 5 == 0 and B < 100 or C % 3 == 0 and D == 6:
        print("true")
    else:
        print("false")


def ex11_struktura_kushtezuese():
    #  Të shkruhet programin për makinen llogaritëse të thjeshtë duke përdorur switch e i cili kryen
    # llogaritje për dy numra të plotë. Nëse shtypet + të kryhet mbledhja, nëse shtypet - të kruhet zbritja,
    # nëse shtypet / të kryhet pjesëtimi, nëse shtypet * të kryhet shumëzimi, për karaktere tjera të shfaqet
    # mesazhi "Gabim në llogaritje"
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    calculation = input("Enter witch calculation should be done (+ - / or *): ")
    if calculation == "+":
        print("Adding", a, calculation, b, "=", a + b)
    if calculation == "-":
        print("Subtracting", a, calculation, b, "=", a - b)
    if calculation == "*":
        print("Multiplying", a, calculation, b, "=", a * b)
    if calculation == "/":
        print("Dividing", a, calculation, b, "=", a / b)
    else:
        print("Enter valid calculation")


def ex12_struktura_kushtezuese():
    # Të shkruhet programi duke përdorur switch, i cili identifikon karakterin e shtypur në tastierë nëse
    # është zanore apo jo.
    vowels = ("a", "e", "i", "o", "u", "y")
    letter = str(input("Enter the character to see if its a vowel or no: "))
    if letter in vowels:
        print(letter, "is a vowel")
    else:
        print(letter, "is not a vowel")


def ex13_struktura_kushtezuese():
    # Të shkruhet programi i cili notën e shtypur si numër e shfaq me tekstin si në tabelën e mëposhtme
    # 1 Dobët
    # 2 Mjaftueshëm
    # 3 Mirë
    # 4 Shumë mirë
    # 5 Shkëlqyeshëm
    grade = int(input("Enter the grade (1-5):"))
    match grade:
        case 1:
            print("Dobët")
        case 2:
            print("Mjaftueshëm")
        case 3:
            print("Mirë")
        case 4:
            print("Shumë mirë")
        case 5:
            print("Shkëlqyeshëm")
        case _:
            print("Invalid input")


def ex14_struktura_kushtezuese():
    # Të shkruhet programi për konvertimin e valutës Euro në valutat Dollar amerikan, Jen Japonez, Lek
    # shqiptar, Lira turke dhe Pound anglez nëse dihet faktori i konvertimit. (Faktorin e konvertimin
    # merreni online)
    currency = input("Enter the current you want from EURO to (dollar, lek, yen , lira, pound ): ")
    currency_list = ["dollar", "lek", "yen", "lira", "pound"]
    if currency in currency_list:
        value = int(input("Enter the amount of EURO to convert: "))
        match currency:
            case "dollar":
                print(value * 1.09, "$")
            case "lek":
                print(value * 103.94, "Lek")
            case "yen":
                print(value * 158.90, "Yen")
            case "lira":
                print(value * 32.95, "Lira")
            case "pound":
                print(value * 0.85, "Pound")
    else:
        print("Invalid currency")


def ex15_struktura_kushtezuese():
    # Të shkruhet programi për llogaritjen e faktorielit n!. Struktura Ciklike të krijohet përmes etiketës
    n = int(input("Enter the value of n to find n!: "))
    i = n
    factorial = 1
    while i > 1:
        factorial = factorial * i
        i -= 1
    else:
        print(n, "! =", factorial)


def ex16_struktura_kushtezuese():
    # Të shkruhet programi duke përdorur operatorin e kushtëzuar ? përmes të cilit krahasohen vlerat e dy
    # variablave.
    operand = input("Enter operand (> < OR ==): ")
    operands = [">", "<", "=="]
    if operand in operands:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        match operand:
            case ">":
                print(a > b)
            case "<":
                print(a < b)
            case "==":
                print(a == b)
    else:
        print("Enter valid comparison operand")


def ex17_struktura_kushtezuese():
    # Të shkruhet programi për llogaritjen e shprehjes së mëposhtme duke përdorur operatorin e kushtëzuar?
    x = int(input("Enter the value of X: "))
    if x < 1:
        print("Calculating: 4x^2+2x-4")
        expression = 4 * pow(x, 2) + 2 * x - 4
        print(expression)
    else:
        print("Calculating: 6x-3")
        expression = 6 * x - 3
        print(expression)


def ex18_struktura_kushtezuese():
    # Të shkruhet programi që lexon nga tastiera numrin e muajit dhe shfaq emrin e tij
    x = int(input("Enter the month you want displayed (1-12): "))
    if 1 <= x <= 12:
        match x:
            case 1:
                print("January")
            case 2:
                print("February")
            case 3:
                print("March")
            case 4:
                print("April")
            case 5:
                print("May")
            case 6:
                print("June")
            case 7:
                print("July")
            case 8:
                print("August")
            case 9:
                print("September")
            case 10:
                print("October")
            case 11:
                print("November")
            case 12:
                print("December")
    else:
        print("Please enter value 1-12")


def ex19_struktura_kushtezuese():
    # Të shkruhet programi që lexon nga tastiera pikët e një provimi të një studenti dhe shfaq në ekran notën e tij.
    # Piket Nota
    # 45-54 5
    # 55-64 6
    # 65-74 7
    # 75-84 8
    # 85-94 9
    # 95-100 10

    grade = int(input("Enter students grade: "))
    if grade in range(45, 55):
        print("5")
    elif grade in range(55, 65):
        print("6")
    elif grade in range(65, 75):
        print("7")
    elif grade in range(75, 85):
        print("8")
    elif grade in range(85, 95):
        print("9")
    elif grade in range(95, 101):
        print("10")
    else:
        print("Unknown value")
