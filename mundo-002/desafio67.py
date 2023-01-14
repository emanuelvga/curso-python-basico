while True:
    n = int(input('taboada de qual valor? '))
    if n < 0:
        break
    for t in range(1, 11):
        print(f'{n} x {t} = {t * n}')
print('Programa de taboada encerrada...')
    
    