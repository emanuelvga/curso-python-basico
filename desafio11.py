# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m².
lar = float(input("qual a largura da parede? "))
alt = float(input("qual a altura da parede? "))
h = lar * alt
paint = h / 2
print(f"a area foi de {h:.2f} metros² ")
print(f"para pintar essa parede gastará {paint:.2f} litros de tinta")
