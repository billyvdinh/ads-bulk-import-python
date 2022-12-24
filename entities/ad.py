
class Ad(object):
    def __init__(self, id, ad_group_id, title, post_id):
        """
        :param id: integer, unique identifier
        :param ad_group_id: integer, reference from ad group id
        :param title: string or null
        :param post_id: string or null
        """
        self.id = id
        self.ad_group_id = ad_group_id
        self.title = title
        self.post_id = post_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if type(id) != int:
            raise Exception("id must be integer")

        self._id = id

    @property
    def ad_group_id(self):
        return self._ad_group_id

    @ad_group_id.setter
    def ad_group_id(self, ad_group_id):
        if type(ad_group_id) != int:
            raise Exception("ad group id must be integer")

        self._ad_group_id = ad_group_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title and type(title) != str:
            raise Exception("title must be string or None")

        self._title = title

    @property
    def post_id(self):
        return self._post_id

    @post_id.setter
    def post_id(self, post_id):
        if post_id and type(post_id) != str:
            raise Exception("post id must be string or None")

        self._post_id = post_id

    def to_dict(self):
        return {
            'id': self.id,
            'ad_group_id': self.ad_group_id,
            'title': self.title,
            'post_id': self.post_id
        }
