import random
import time


def create_player():
    player = {'Жизни': 50}
    player['имя'] = input('Имя игрока')
    return player

def attack(damager, defender):
    damager['урон'] = random.randint
    defender['жизни'] -= damager['урон']
    print(damager['имя'] + 'нанес ' + str(damager['урон']) + 'урона')

def player_info(player):
    print('y' + player['имя'] + 'осталось')


def player_death(player1)

player1 = create_player()
player2 = create_player()


while player1['жизни'] > 0 and player2['жизни'] > 0:  # проверка, живы ли бойцы
    time.sleep(2)


    attack(player1, player2)
    attack(player2, player1)

    player_info(player1)
    player_info(player2)


if player1['жизни'] <= 0 and player2['жизни'] <= 0:  # проверка на ничью
    print('Оба игрока погибли. Ничья.')
elif player1['жизни'] <= 0:  # проверка на поражение игрока 1
    print(player1['имя'] + ' погиб. ' + player2['имя'] + ' победил!')
elif player2['жизни'] <= 0:  # проверка на поражение игрока 2
    print(player2['имя'] + ' погиб. ' + player1['имя'] + ' победил!')

print(player_death(player1, player2))