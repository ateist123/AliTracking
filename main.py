from Tracker import Shipment
from tkinter import *
import config


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


def MakeInterface():
    tk = Tk()
    screen = [str(int(tk.winfo_screenwidth()/2)), str(int(tk.winfo_screenheight()/2))]
    tk.geometry(screen[0]+'x'+screen[1])
    tk.title('Aliexpress Shipments Tracking')

    TracksDict = DoTrackList(SendersList, TracksList)
    TrackCodes = []
    c = 1
    for x in TracksDict:
        c += 1
        c = Text(tk, TracksDict[x])

MakeInterface()
