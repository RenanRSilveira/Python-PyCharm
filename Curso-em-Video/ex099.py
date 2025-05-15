from time import sleep
def maior(* num):
    if not num:
        print('Sem valoes definidos!')
        return
    print('[ ', end='')
    for valor in num:
        print(f'{valor} ', end='')
    print('] ', end='')

    ordem = sorted(num)
    print(f'Foram informados {len(ordem)} valores e o maior é {ordem[-1]}')


maior(3, 5, 6, 4, 7, 9)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()