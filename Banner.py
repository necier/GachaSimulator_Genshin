import Dicts


class Banner(object):
    def __init__(self):
        self.pity_cnt = 0
        self.not_purple_cnt = 0
        self.gold_prob = 0.006
        self.purple_prob = 0.0255
        self.list_gold_cha = Dicts.permanent_pool_items['CSSR']
        self.list_gold_wep = []
        self.list_purple_cha = Dicts.permanent_pool_items['CSR']
        self.list_purple_wep = Dicts.permanent_pool_items['WSR']


class PermanentBanner(Banner):
    def __init__(self):
        super().__init__()

    def update_prob(self):
        if self.pity_cnt >= 73:
            self.gold_prob += 0.06
        else:
            self.gold_prob = 0.006


class UpBanner(Banner):
    def __init__(self):
        super().__init__()
        self.guarantee = False

    def update_prob(self):
        if self.pity_cnt >= 73:
            self.gold_prob += 0.06
        else:
            self.gold_prob = 0.006


class WeaponBanner(Banner):
    def __init__(self, gold_up: list):
        super().__init__()
