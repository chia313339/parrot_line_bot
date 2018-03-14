from Entity.Entity import *


class PictureDate(db.Model):
    __tablename__ = 'PictureDate'

    def __init__(self
                 , Uuid
                 , Title
                 , Description
                 ):
        self.Uuid = Uuid
        self.Title = Title
        self.Description = Description


class LEARN_WORD(db.Model):
    __tablename__ = 'LEARN_WORD'

    def __init__(self, KEYWORD, MESSAGE):
        self.KEYWORD = KEYWORD
        self.MESSAGE = MESSAGE
