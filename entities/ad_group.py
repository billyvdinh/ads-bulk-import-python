from datetime import datetime


class AdGroup(object):
    def __init__(self, id, campaign_id, title, geolocations, start_date, end_date):
        """
        :param id: integer, unique identifier
        :param campaign_id: integer, reference from campaign id
        :param title: string or null
        :param geolocations: comma separated string or null
        :param start_date: date string (m/d/y)
        :param end_date: date string (m/d/y)
        """
        self.id = id
        self.campaign_id = campaign_id
        self.title = title
        self.geolocations = geolocations
        self.start_date = start_date
        self.end_date = end_date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if type(id) != int:
            raise Exception("id must be integer")

        self._id = id

    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        if type(campaign_id) != int:
            raise Exception("campaign id must be integer")

        self._campaign_id = campaign_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title and type(title) != str:
            raise Exception("title must be string or None")

        self._title = title

    @property
    def geolocations(self):
        return self._geolocations

    @geolocations.setter
    def geolocations(self, geolocations):
        if geolocations and type(geolocations) != list:
            raise Exception("geolocations must be list or None")

        self._geolocations = geolocations

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if start_date and type(start_date) != datetime:
            raise Exception("start date must be datetime or None")

        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if end_date and type(end_date) != datetime:
            raise Exception("end date must be datetime or None")

        self._end_date = end_date

    def to_dict(self):
        return {
            'id': self.id,
            'campaign_id': self.campaign_id,
            'title': self.title,
            'geolocations': self.geolocations,
            'start_date': self.start_date.strftime('%m/%d/%y'),
            'end_date': self.end_date.strftime('%m/%d/%y')
        }
