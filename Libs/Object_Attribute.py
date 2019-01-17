class Attribute:
    def __init__(self, **kwargs):
        self.attributes = {"attribute_moveSpeed": 0,
                           "attribute_phyCritRate": 0,
                           "attribute_fireStrengthening": 0,
                           "attribute_fireResistance": 0,
                           "attribute_attackSpeed": 0,
                           "attribute_lightStrengthening": 0,
                           "attribute_lightResistance": 0,
                           "attribute_stiff": 0,
                           "attribute_magicDefense": 0,
                           "attribute_mpRecovery": 0,
                           "attribute_iceStrengthening": 0,
                           "attribute_antiEvil": 0,
                           "attribute_hpRecovery": 0,
                           "attribute_singingSpeed": 0,
                           "attribute_hitRate": 0,
                           "attribute_dodgeRage": 0,
                           "attribute_iceResistance": 0,
                            "attribute_magicCritRate": 0,
                           "attribute_stiffness": 0,
                           "attribute_strength": 0,
                           "attribute_intelligence": 0,
                           "attribute_mp": 0,
                           "attribute_spirit": 0,
                           "attribute_phyAttack": 0,
                           "attribute_magicAttack": 0,
                           "attribute_hp": 0,
                           "attribute_phyDefense": 0,
                           "attribute_stamina": 0,
                           "attribute_darkStrengthening": 0}
        for key, val in kwargs.items():
            if self.attributes.get(key) is not None:
                self.attributes[key] = val

    def __add__(self, other):
        """
        :type other: Attribute
        :return: Attribute
        """
        res = Attribute()
        for key in other.attributes:
            if self.attributes.get(key):
                res.attributes[key] = self.attributes[key] + other.attributes[key]
        return res
    def __sub__(self, other):
        res = Attribute()
        for key in other.attributes:
            if self.attributes.get(key):
                res.attributes[key] = self.attributes[key] - other.attributes[key]
        return res

    def getAttribute(self, key):
        return self.attributes.get(key)
