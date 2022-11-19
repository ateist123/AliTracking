import requests
from bs4 import BeautifulSoup


class Shipment:
    def __init__(self, track, sender):
        self.Track = track
        self.Sender = sender
        self.Month = []

    class pattern:
        DateStart = 0
        DateEnd = 5
        TimeStart = 6
        TimeEnd = 11
        StatusStart = 12

    def GetSippingState(self, last, qotes):
        last += 6
        if 6 < last > 9:
            raise RuntimeError('Invalid number')

        q = " ".join(qotes[last].text.replace('\n', '').replace('Aliexpress Standard Shipping', '').replace('Hong Kong', ''))
        q = q.split()
        for x in self.Month:
            q = q.replace(x, self.Month[x])
        q = q.replace(' ', ':', 1)
        return q

    def SetMonthDict(self):
        self.Month = {
            'января': '01',
            'февраля': '02',
            'марта': '03',
            'апреля': '04',
            'мая': '05',
            'июня': '06',
            'июля': '07',
            'августа': '08',
            'сентября': '09',
            'октября': '10',
            'ноября': '11',
            'декабря': '12'
        }

    def GetTrack(self, last):
        url = 'https://gdeposylka.ru/courier/'+self.Sender+'/tracking/'+self.Track
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        qote = soup.findAll('li')

        # 5 - id;  6-9 -- zakaz
        self.GetSippingState(last, qote)
        ReturnDict = {
            'date': self.GetSippingState(last, qote)[self.pattern.DateStart:self.pattern.DateEnd],
            'time': self.GetSippingState(last, qote)[self.pattern.TimeStart:self.pattern.TimeEnd],
            'status': self.GetSippingState(last, qote)[self.pattern.StatusStart:len(self.GetSippingState(1, qote))]
        }
        return ReturnDict


Sh = Shipment('LD145472776CN', 'china-ems')
Sh.SetMonthDict()
print(Sh.GetTrack(0)['date'])
