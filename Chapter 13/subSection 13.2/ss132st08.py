# Звездный треугольник
#
# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
#     fill – символ заполнитель;
#     base – величина основания равнобедренного треугольника;
#
# а затем выводит его.
#
# Примечание. Гарантируется, что основание треугольника – нечетное число.

# put your python code here
def draw_triangle(fill, base):
    for i in range(base + 1):
        if (base // 2) + 1 >= i:
            print(fill * i)
        else:
            print(fill * (base - i + 1))

        # считываем данные


fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)