"""
# Задание №1.
#
# Рецепт булочек предусматривает следующие ингридиенты

# 1.5 стакана сахара
# 1 стакан масла
# 2.75 стакана муки

# С таким количеством ингридиентов этот рецепт позволяет приготовить 48 булочек.
# Напишите программу, которая запрашивает у пользователя, сколько булочек он хочет
# приготовить, и затем показывает число стаканов каждого ингридиента, необходимого
# для заданного количества булок
#
# отводится времени 1.5 часа.
"""

print('Ну что начнем ?')
OneSugar = 1.5/48
OneMaslo = 1/48
OneMuka  = 2.75/48

print(f'На приготовление одной булочки уходит: \n', OneSugar, f' стаканов сахара\n', OneMaslo, f' стаканов масла\n',
      OneMuka, f' стаканов муки\n')

print(f'соответственно, \n')
bulok = int(input(f'сколько вы хотите приготовить булочек? '))
print('ok, на такое количество (',bulok, ' шт.) у вас уйдет ингридиентов:')
print('Сахара: ', OneSugar * bulok, ' стакана')
print('Масла: ', OneMaslo * bulok, ' стакана')
print('Муки: ', OneMuka * bulok, ' стакана')
