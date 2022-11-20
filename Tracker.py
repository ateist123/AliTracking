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
        TrackStart = 35

    def GetShipmentState(self, last=1, IsRaw=True, qotes=[]):
        last += 5
        if 5 < last > 9:
            raise RuntimeError('Invalid number')
        if not qotes:
            raise RuntimeError('Empty qotes')

        q = " ".join(qotes[last].text.replace('\n', '')
                     .replace('Aliexpress Standard Shipping', '')
                     .replace('Hong Kong', '')
                     .split())  # clearing result

        for x in self.Month:
            q = q.replace(x, self.Month[x])
        if not IsRaw:
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

    def GetTrack(self, last=1, IsRaw=False):
        url = 'https://gdeposylka.ru/courier/' + self.Sender + '/tracking/' + self.Track
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        qote = soup.findAll('li')
        if IsRaw:
            ReturnDict = {
                'date': '-1:-1',
                'time': '-1:-1',
                'status': self.GetShipmentState(last, True, qote)
            }
        else:
            # 5 - id;  6-9 -- zakaz
            if last == 0:
                ShipmentState = self.GetShipmentState(last, False, qote)
                ReturnDict = {
                    'date': '-1:-1',
                    'time': '-1:-1',
                    'status': ShipmentState[self.pattern.TrackStart:len(ShipmentState)]
                }
            else:
                ShipmentState = self.GetShipmentState(last, False, qote)

                ReturnDict = {
                    'date': ShipmentState[self.pattern.DateStart:self.pattern.DateEnd],
                    'time': ShipmentState[self.pattern.TimeStart:self.pattern.TimeEnd],
                    'status': ShipmentState[self.pattern.StatusStart:len(ShipmentState)]
                }

        return ReturnDict
