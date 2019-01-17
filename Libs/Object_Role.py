from UI.Role import Ui_Role
import sqlite3
from Config.Config import Config

conn = sqlite3.connect(Config.DATABASE_PATH/Config.BASE_ATTRIBUTE_DB)
c=conn.cursor()

class Role(Ui_Role):

    def __init__(self, character, profession):
        super(Role, self).__init__()
        self.character = character
        self.profession = profession

    def start(self):
        self.initBaseAttribute()
        self.initSkillTree()

    def reset(self):
        pass

    def initBaseAttribute(self):
        pass

    def initSkillTree(self):
        pass

    def update(self):
        pass
