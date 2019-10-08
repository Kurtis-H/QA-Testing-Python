from challenges.numbertowords import convert_to_words


def Fibonacci(n):
    a = 0
    b = 1
    c = None
    e = 0

    while n > 0:
        if e < 1:
            print("0 - Zero")
            e += 1
            n -= 1

        else:
            c = a
            a = b + a
            b = c
            n -= 1

            d = convert_to_words(a)

