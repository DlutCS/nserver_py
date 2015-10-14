from models import Model, store

class Group(Model):

    __table__ = 'tbl_group'

    def __init__(self, id, name, category, news, comment, user, group):
        self.id = id
        self.name = name
        self.category = category
        self.news = news
        self.comment = comment
        self.user = user
        self.group = group

    @classmethod
    def get_auth(cls, group_id, name):
        sql = 'select %s from {} where id=%s'.format(cls.__table__)
        params = (name, group_id)
        print sql % params
        rs = store.execute(sql, params)
        print rs
        return rs[0][name] if rs else None
