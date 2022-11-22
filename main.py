from tkinter import *

import config
from Tracker import Shipment

StdEncoding = config.StdEncoding
SendersList = config.SendersList
TracksList = config.TracksList


def DoTrackList(SendersL, TracksL):
    TracksDict = {}
    c = False
    for Sender in SendersL:
        for Track in TracksL:
            try:
                sh = Shipment(Track, Sender)
                sh.SetMonthDict()
                sh.GetTrack(1)
                c = True
            except:
                c = False
            finally:
                if c:
                    TracksDict[Track] = Sender
    del c
    return TracksDict


class Interface:
    tk = Tk()

    def __init__(self, Creator: str, TracksDict: dict = None):
        if not TracksDict:
            self.TracksDict = DoTrackList(SendersList, TracksList)
        else:
            self.TracksDict = TracksDict
        screen = [str(int(self.tk.winfo_screenwidth() / 2)), str(int(self.tk.winfo_screenheight() / 2))]
        self.tk.geometry(screen[0] + 'x' + screen[1])
        self.tk.title('Aliexpress Shipments Tracking by ' + Creator)

    def ConstructText(self, TracksDict):
        TrackCodes = []
        c = 0
        for x in TracksDict:
            c += 1
            TrackCodes.append(Label(self.tk, text=x).grid(column=1, row=c))
        self.tk.mainloop()


i = Interface('/dev/null')
i.ConstructText([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
