class SkillDamage:
    def __init__(self, value, phy=True, percentage=True, trend=0):
        """
        :param value: Damage Value
        :param phy:  is phy damage
        :param percentage: is percentage damage
        :param trend: {0: 'none', 1: 'fire', 2:'ice',3:'light',4:'dark'}
        """
        self.value = value
        self.phy = phy
        self.percentage = percentage
        self.trend = trend


class Skill:
    maxLv = 99
    minLv = 0
    learnLv = 0
    learnInterval = 1
    spCost = 0
    tpCost = 0
    damage = {}

    def __init__(self, ID, level=0):
        """
        :param ID: skill ID
        :param level: skill level
        """
        self.ID = ID
        self.lv = level

    def addDamage(self):
        pass
    def loadSkil(self):
        pass

    def levelUP(self):
        pass

    def levelDown(self):
        pass


class SkillTree:
    def __init__(self, character, profession):
        pass

    def add_skill(self,skill,position):
        """
        :type skill: Skill
        :type position (int,int)
        :return:
        """
        pass
