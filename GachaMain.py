import User
import Dicts
import colorama
import os
import Analyze


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
                aer = Analyze.statistic(user.gacha_history)
            aer.display_gacha_history()
            print('\n\n')
        elif op == 6:
            user = User.User()
            os.system('cls')
        elif op == 7: \
                exit(0)
