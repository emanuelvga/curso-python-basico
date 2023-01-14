# Escreva um programa que leia um valor em metros e o exiba convertido em  quilômetro, hectômetro, decâmetro, metro, decímetro, centímetro.
n1 = float(input("uma distancia em metros: "))
print(f"a medida de {n1} metros corresponde a: ")
km = n1 * 0.001
hm = n1 * 0.01
dan = n1 * 0.1
dec = n1 * 10
cent = n1 * 100
mili = n1 * 1000
print(
    f"{km} Quilômetros\n {hm} Hectômetros\n {dan:.2f} Decâmetros:\n {dec} Decímetros\n {cent} Centímetros\n {mili} Milímetros:"
)
