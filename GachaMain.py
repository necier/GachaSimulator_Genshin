import User
import Dicts
import colorama
import os
import Analyze


def printTerminal(H: dict):
    for J in H:
        print('-----------------------', end='')
        if J == 'permanent':
            print('常驻池的抽卡记录')
        elif J == 'up':
            print('UP池的抽卡记录')
        L = H[J]
        length = len(L)
        if not length:
            print('无抽卡记录')
        else:
            for i in range(length):
                # flag='\n' if i&1 else '1'
                flag = '\n'
                if L[i][0] in Dicts.items['character_ssr'] or L[i][0] in Dicts.items['weapon_ssr']:
                    print(colorama.Fore.YELLOW + '第{}抽：  {}'.format(L[i][1], L[i][0]), end=flag)
                elif L[i][0] in Dicts.items['character_sr'] or L[i][0] in Dicts.items['weapon_sr']:
                    print(colorama.Fore.MAGENTA + '第{}抽：  {}'.format(L[i][1], L[i][0]), end=flag)
                else:
                    print('第{}抽：  {}'.format(L[i][1], L[i][0]), end=flag)
    print('-------------------------\n\n')
    aer = Analyze.statistic(H)
    print('deviation_rate: {}'.format(aer.deviation_rate))
    print('gold prob: {}'.format(aer.up_gold_prob))


if __name__ == '__main__':
    colorama.init(autoreset=True)
    user = User.User()
    while True:

        print(
            '(1)常驻池 (2)Up1池 (3)Up2池 (4)武器池还没做捏 (5)抽卡统计 (6)清空抽卡记录 (7)退出程序\n现在常驻池抽了{}发，UP池抽了{}发\n'.format(
                len(user.gacha_history['permanent']), len(user.gacha_history['up'])))
        op = int(input(''))
        if op < 5:
            times = int(input('多少抽？\n'))
            os.system('cls')
            for i in range(times):
                user.onepull(op)
        elif op == 5:
            os.system('cls')
            if not len(user.gacha_history['up']) + len(user.gacha_history['permanent']):
                print("there's no gacha history!")
            else:
                # printTerminal(user.gacha_history)
                aer = Analyze.statistic(user.gacha_history)
            aer.display_gacha_history()
            print('\n\n')
        # print(user.gacha_history)
        elif op == 6:
            # user.clear_gacha_history()
            user = User.User()
            os.system('cls')
        elif op == 7: \
                exit(0)
