

class Campaign(object):
    def __init__(self, id, title, objective):
        """
        :param id: integer, unique identifier
        :param title: string or None
        :param objective: integer or None
        """
        self.id = id
        self.title = title
        self.objective = objective

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if type(id) != int:
            raise Exception("id must be integer")

        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not title and type(title) != str:
            raise Exception("title must be string or None")

        self._title = title

    @property
    def objective(self):
        return self._objective

    @objective.setter
    def objective(self, objective):
        if not objective and type(objective) != str:
            raise Exception("objective must be string or None")

        self._objective = objective

