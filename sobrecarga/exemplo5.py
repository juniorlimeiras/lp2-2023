import datetime

class Data:
    def __init__(self, data):
        if isinstance(data, str):
            self._d = datetime.date.fromisoformat(data)
        elif isinstance(data, datetime.date):
            self._d = data
        #print(datetime.date.today())
    def __str__(self):
        return f'{self._d.day:02}/{self._d.month:02}/{self._d.year}'
d1 = Data('2024-01-02')
d2 = Data(datetime.date.today())
print(d1, d2)