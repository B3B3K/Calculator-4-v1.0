print('{}\n{}\n{}\n{}'.format("1++toplama ", "2--çıkarma", "3**çarpma ", "4//bölme"))
i = int(input(">-1-2-3-4-< sayılarından birini giriniz "))
s = int(input("1. sayıyı giriniz: "))
d = int(input("2. sayıyı giriniz: "))
if i > 4:
    print(">-1-2-3-4-< sayılarından birini giriniz", i)
elif i == 1:
    print("toplama sonuç= ", s+d)
elif i == 2:
    print("çıkarma sonuç= ", s-d)
elif i == 3:
    print("çarpmanın sonucu", s*d)
elif i == 4:
    print("bölmenin sonucu", s/d)
