import Dicts
import Banner
import colorama


class statistic(object):
    def __init__(self, record):
        self.permanent_record = record['permanent']
        self.up_record = record['up']

        self.num_permanent_gold = 0
        self.num_permanent_pull = len(self.permanent_record)

        self.num_up_gold = 0
        self.num_up_up_gold = 0
        self.num_up_pull = len(self.up_record)

        self.up_gold_prob = 0
        self.permanent_gold_prob = 0
        self.deviation_rate = 0

        self.up_avarage_pull = 0
        self.permanent_avarage_pull = 0

        # start point
        self.up_process()
        self.permanent_process()

    def up_process(self):
        for i in range(self.num_up_pull):
            temp = self.up_record[i][0]
            if temp in Dicts.items['character_ssr']:
                self.num_up_gold += 1
                for i in range(2):
                    if temp in Dicts.upcharacters[i]:
                        self.num_up_up_gold += 1
                        break
        if self.num_up_gold:
            self.deviation_rate = self.num_up_up_gold / self.num_up_gold
            self.up_gold_prob = self.num_up_gold / self.num_up_pull
            self.up_avarage_pull = self.num_up_pull / self.num_up_gold
        else:
            self.deviation_rate = 0
            self.up_gold_prob = 0
            self.up_avarage_pull = 0

    def display_gacha_history(self):
        self.display_pool('permanent')
        self.display_pool('up')
        print('常驻池出金概率: {}%，平均{}抽一个金'.format(100 * self.permanent_gold_prob, self.permanent_avarage_pull))
        print('up池出金概率: {}%，平均{}抽一个金'.format(100 * self.up_gold_prob, self.up_avarage_pull))
        print('小保底不歪概率: {}%'.format(100 * self.deviation_rate))

    def display_pool(self, mode):
        if mode == 'permanent':
            print('-----------------------常驻池的抽卡记录')
            for i in range(len(self.permanent_record)):
                flag = '\n'
                if self.permanent_record[i][0] in Dicts.items['character_ssr'] or self.permanent_record[i][0] in \
                        Dicts.items['weapon_ssr']:
                    print(colorama.Fore.YELLOW + '第{}抽：  {}'.format(self.permanent_record[i][1],
                                                                      self.permanent_record[i][0]), end=flag)
                elif self.permanent_record[i][0] in Dicts.items['character_sr'] or self.permanent_record[i][0] in \
                        Dicts.items['weapon_sr']:
                    print(colorama.Fore.MAGENTA + '第{}抽：  {}'.format(self.permanent_record[i][1],
                                                                       self.permanent_record[i][0]), end=flag)
                else:
                    print('第{}抽：  {}'.format(self.permanent_record[i][1], self.permanent_record[i][0]), end=flag)
            print('-------------------------')
        elif mode == 'up':
            print('-----------------------UP池的抽卡记录')
            for i in range(len(self.up_record)):
                # flag='\n' if i&1 else '1'
                flag = '\n'
                if self.up_record[i][0] in Dicts.items['character_ssr'] or self.up_record[i][0] in \
                        Dicts.items['weapon_ssr']:
                    print(colorama.Fore.YELLOW + '第{}抽：  {}'.format(self.up_record[i][1],
                                                                      self.up_record[i][0]), end=flag)
                elif self.up_record[i][0] in Dicts.items['character_sr'] or self.up_record[i][0] in \
                        Dicts.items['weapon_sr']:
                    print(colorama.Fore.MAGENTA + '第{}抽：  {}'.format(self.up_record[i][1],
                                                                       self.up_record[i][0]), end=flag)
                else:
                    print('第{}抽：  {}'.format(self.up_record[i][1], self.up_record[i][0]), end=flag)
            print('-------------------------')

    def permanent_process(self):
        for i in range(self.num_permanent_pull):
            temp = self.permanent_record[i][0]
            if temp in Dicts.items['character_ssr'] or temp in Dicts.items['weapon_ssr']:
                self.num_permanent_gold += 1
        if self.num_permanent_gold:
            self.permanent_gold_prob = self.num_permanent_gold / self.num_permanent_pull
            self.permanent_avarage_pull = self.num_permanent_pull / self.num_permanent_gold
