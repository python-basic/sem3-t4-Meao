import math

def calc_accuracy(accuracy=0.00001):
    i = 10
    mant_digit = 0
    while (i * accuracy < 1):
      mant_digit += 1
      i *= 10
    return mant_digit

def discr(a=0, b=0, c=0, accuracy=0.00001):
    """
    Дискриминант
         
    Многострочный текст, описывающий функцию
    и ОДЗ для входных и выходных значений 
         
    TODO: дополнить вычисление указанием точности
         
         
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        res = float(b**2 - 4*a*c)
        return float(round(res, calc_accuracy(accuracy)))
    else:
      return 0.0

def solve_eq(a, b, c, accuracy=0.00001):
    """
    Решение квадратного уравнения с помощью дискриминанта
         
    TODO: Дополнить докстрингом, описать входные и выходные значения. 
    """
    x1, x2 = None, None
    discriminant = discr(a, b, c, accuracy=accuracy)
    if discriminant >= 0:
        d = math.sqrt(discriminant)
        x1=(-b+d)/2*a
        x2=(-b-d)/2*a
        x1=float(round(x1, calc_accuracy(accuracy)))
        x2=float(round(x2, calc_accuracy(accuracy)))
    else:
        # d = math.sqrt(-discriminant)
        # x1= complex((-b/(2*a)),d/(2*a))
        # x2= complex((-b/(2*a)),-d/(2*a))
        pass

    return (x1, x2)

print(solve_eq(1,-2,-3))
assert solve_eq(1,2,3) == (None, None),  "Значение по умолчанию для заглушки функции"

 # 1 test case = тестовый случай 
discr(1)  # 0 

 # 2 
discr(1, c=1/4) # -1.0 

 # 3
discr(1,b=2,c=1/4) # 3.0 

 # 4
discr(1,b=2,c=3) # -8.0

 # 5
discr()  # 0.0

 # 5
discr()  # 0.0

 # 6
discr()

 # 7 
res7 = discr(a=0.0005, b=1.0000043, c=5.00000003339992)

if __name__ == '__main__':

    def test1():
        print('test1 is running')
        try:
            assert discr(1) == 0 , "Ошибка при определении дискриминанта"
        except AssertionError as e:
             print(f"ошибка была такая: {e}")

    def test2():
        print('test2 is running')
        try:
            assert discr(1, c=1/4) == -1.0 , "Ошибка при определении дискриминанта"
        except AssertionError as e:
             print(f"ошибка была такая: {e}")

    def test3():
        print('test3 is running')
        try:
            assert discr(1,b=2,c=1/4) == 3.0 , "Ошибка при определении дискриминанта"
        except AssertionError as e:
             print(f"ошибка была такая: {e}")

    def test4():
        print('test4 is running')
        try:
            assert discr(1,b=2,c=3) == -8.0 , "Ошибка при определении дискриминанта"
        except AssertionError as e:
             print(f"ошибка была такая: {e}")

    def test5():
        print('test5 is running')
        try:
            assert discr() == 0.0 , "Ошибка при определении дискриминанта"
        except AssertionError as e:
             print(f"ошибка была такая: {e}")

    def test6(*inpvals):
        print('test6 is running')
        try:
            assert res7 == 0.99 , "Ошибка при определении точности вычислений"
        except AssertionError as e:
             print(f"ошибка была такая: {e} при таких-то значениях {inpvals[0]}")

    def test7():
        print('test7 is running')
        try:
            assert res7 == 0.9900085999516904 , "Ошибка при определении точности вычислений"
        except AssertionError as e:
             print(f"ошибка была такая: {e}")


    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
