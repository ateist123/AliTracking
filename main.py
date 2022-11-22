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


class MakeInterface:
    def __init__(self, tk: Tk(), Creator: str):
        # TracksDict = DoTrackList(SendersList, TracksList)
        self.TracksDict = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.tk = Tk()
        screen = [str(int(self.tk.winfo_screenwidth() / 2)), str(int(tk.winfo_screenheight() / 2))]
        tk.geometry(screen[0] + 'x' + screen[1])
        tk.title('Aliexpress Shipments Tracking by ' + Creator)

    def ConstructText(self, TracksDict: dict):
        TrackCodes = []
        c = 2
        for x in TracksDict:
            c += 1
            TrackCodes.append(Label(self.tk, text=x).grid(column=c % 3, row=c // 3))
        self.tk.mainloop()


MakeInterface()
