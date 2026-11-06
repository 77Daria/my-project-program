import math
import sys

def extract_float(p,s,v):
    print (f"Попытка считывания параметра {p}...")
    try:
        x=float(s)
        v.append(x)
        print("\tУспешно")
        return True
    except ValueError:
        print(f"\tОшибка-не вещественное число,  переходим в режим считывания с клавиатуры")
        return False
def read_float(p):
    while True:
        print(f"Введите параметр {p}: ")
        s=input()
        try:
            x=float(s)
            return x
        except ValueError:
            print("Не вещественное число, повторите ввод")

def add_root(t,lst):
    if t==0:
        lst.append(0)
    elif t>0:
        lst.append(math.sqrt(t))
        lst.append(-math.sqrt(t))
a=0
b=0
c=0
cf=[]
print(sys.argv)
if len(sys.argv)!=4:
    print("программа ожидает три пользовательских аргумента")

elif (extract_float("A", sys.argv[1],cf) and extract_float("B", sys.argv[2],cf) and extract_float("C", sys.argv[3],cf)):
    a = cf[0]
    b = cf[1]
    c = cf[2]
if len(cf)!=3:
    a = read_float("A")
    b = read_float("B")
    c = read_float("C")



print (f"{a}x^4 + {b}x^2 + {c} = 0")
all_roots=[]
if a==0:
    #уравнение становится линейным bx+c=0
    if b==0:
        if c==0:
            print("бесконечное число решений")
        else:
            print("нет решений")
    else:
       # print(f"x = {-c/b}")
        add_root(-c/b, all_roots)
else:
    d=b**2-4*a*c
    if d<0:
        print("Действительных корней нет")
    elif d==0:
       # print(f"x = {-b/(2*a)}")
        add_root(-b/(2*a), all_roots)
    else:
        #print(f"x1 = {(-b+math.sqrt(d))/(2*a)}")
        #print(f"x2 = {(-b - math.sqrt(d)) / (2 * a)}")
        add_root( (-b+math.sqrt(d))/(2*a), all_roots)
        add_root((-b - math.sqrt(d)) / (2 * a) , all_roots)
print(f"Список действительных корней: {all_roots}")

#добавить параметры работы командной строки