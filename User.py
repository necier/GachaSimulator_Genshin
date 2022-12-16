import Banner
import Dicts
from numpy import random


class User(object):

    def __init__(self):
        self.dist = 0
        self.permanentbanner = Banner.PermanentBanner()
        self.upbanner = Banner.UpBanner()
        self.gacha_history = {
            'permanent': [],
            'up': []
        }

    # def clear_gacha_history(self):
    #     self.gacha_history['permanent'] = []
    #     self.gacha_history['up'] = []

    def get_up_gacha_history(self):
        return self.gacha_history['up']

    def get_permanent_history(self):
        return self.gacha_history['permanent']

    def one_is_character_else_weapon(self) -> bool:
        temp = random.choice([0, 1])
        return temp == 1

    def one_is_up_else_normal(self) -> bool:
        temp = random.choice([0, 1])
        return temp == 1

    def get_new_dist(self):
        self.dist = random.rand()

    def onepull(self, mode):
        self.get_new_dist()
        mode = int(mode)
        if mode == 1:
            self.permanentpull()
        elif mode == 2 or mode == 3:
            self.uppull(mode - 2)
        else:
            pass

    def permanentpull(self):
        rank = self.return_rank(self.permanentbanner.gold_prob, self.permanentbanner.purple_prob)
        if rank == 'b' and self.permanentbanner.not_purple_cnt >= 9:
            rank = 'p'
        certain_item = self.get_new_permanent_item(rank)
        self.gacha_history['permanent'].append([certain_item, self.permanentbanner.pity_cnt + 1])
        self.change_permanent_stats(rank)

    def change_permanent_stats(self, current_rank):
        if current_rank == 'g':
            self.permanentbanner.pity_cnt = 0
            self.permanentbanner.not_purple_cnt += 1
        elif current_rank == 'p':
            self.permanentbanner.pity_cnt += 1
            self.permanentbanner.not_purple_cnt = 0
        else:
            self.permanentbanner.pity_cnt += 1
            self.permanentbanner.not_purple_cnt += 1
        self.permanentbanner.update_prob()

    def get_new_permanent_item(self, rank):
        if rank == 'b':
            return str(random.choice(Dicts.permanent_pool_items['R']))
        else:
            flag = self.one_is_character_else_weapon()
            if rank == 'g':
                if flag:
                    return str(random.choice(Dicts.permanent_pool_items['CSSR']))
                else:
                    return str(random.choice(Dicts.permanent_pool_items['WSSR']))
            else:
                if flag:
                    return str(random.choice(Dicts.permanent_pool_items['CSR']))
                else:
                    return str(random.choice(Dicts.permanent_pool_items['WSR']))

    def return_rank(self, gold_prob, purple_prob):
        if self.dist <= gold_prob:
            return 'g'
        elif self.dist <= purple_prob + gold_prob:
            return 'p'
        else:
            return 'b'

    def change_upbanner_stats(self, current_rank, isUp: bool):
        if current_rank == 'g':
            self.upbanner.pity_cnt = 0
            self.upbanner.guarantee = False if isUp else True
            self.upbanner.not_purple_cnt += 1
        elif current_rank == 'p':
            self.upbanner.pity_cnt += 1
            self.upbanner.not_purple_cnt = 0
        else:
            self.upbanner.pity_cnt += 1
            self.upbanner.not_purple_cnt += 1
        self.upbanner.update_prob()

    def get_new_up_item(self, rank, index):
        if rank == 'g':
            flag = self.one_is_up_else_normal()
            if self.upbanner.guarantee:
                flag = True
            if flag:
                return Dicts.upcharacters[0][index]
            else:
                return str(random.choice(Dicts.permanent_pool_items['CSSR']))
        elif rank == 'p':
            flag = self.one_is_up_else_normal()
            if flag:
                return str(random.choice(Dicts.upcharacters[1]))
            else:
                return str(random.choice(Dicts.permanent_pool_items['WSR'] + Dicts.permanent_pool_items['CSR']))
        else:
            return str(random.choice(Dicts.permanent_pool_items['R']))

    def uppull(self, index):
        rank = self.return_rank(self.upbanner.gold_prob, self.upbanner.purple_prob)
        if rank == 'b' and self.upbanner.not_purple_cnt >= 9:
            rank = 'p'
        certain_item = self.get_new_up_item(rank, index)
        self.gacha_history['up'].append([certain_item, self.upbanner.pity_cnt + 1])
        self.change_upbanner_stats(rank, certain_item == Dicts.upcharacters[0][index])

    def tenpull(self, mode):
        for i in range(10):
            self.onepull(mode)
