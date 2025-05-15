a = int(input('Digite um ano: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('\033[32mAno bissexto!\033[m')
else:
    print('\033[032mAno \033[31mnão\033[032m bissexto!')