from tkinter import *
from tkinter import ttk

import asyncio as asio

import config
from Tracker import Shipment

StdEncoding = config.StdEncoding



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
    SendersList = config.SendersList
    TracksList = config.TracksList

    def __init__(self, Creator: str, TracksDict: dict = None):
        if not TracksDict:
            #self.TracksDict = DoTrackList(self.SendersList, self.TracksList)
            self.TracksDict = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        else:
            self.TracksDict = TracksDict
        self.SendersList = config.SendersList
        self.TracksList = config.TracksList
        screen = [str(int(self.tk.winfo_screenwidth() / 2)), str(int(self.tk.winfo_screenheight() / 2))]
        self.tk.geometry(screen[0] + 'x' + screen[1])
        self.tk.title('Aliexpress Shipments Tracking by ' + Creator)
        self.tk.withdraw()
        self.wait = True
    async def MainLoop(self):
        self.tk.mainloop()
    def CreateDictComponents(self):
        Tracks  = self.DirtyTracks.get('1.0','end').strip().split(',')
        Senders = self.DirtySenders.get('1.0','end').strip().split(',')
        for x in range(len(Tracks)):
            Tracks[x] = Tracks[x].strip()
        for x in range(len(Tracks)):
            Senders[x] = Senders[x].strip()
        return [Senders, Tracks]
    def SpecialDoTrackList(self):
        self.wait = False
        DictComponents = self.CreateDictComponents()
        SendersL = DictComponents[0]
        TracksL = DictComponents[1]
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
        if TracksDict:
            self.TracksDict = TracksDict
        else:
            self.TracksDict = 'No Track Codes'
    def GetDictFromConfig(self):
        self.TracksDict = config.TracksDict
    def PutDictInConfig(self):
        config.TracksDict = self.TracksDict
    def ConstructTracksDict(self, IsNewWindow: bool = True):
        if IsNewWindow:
            Window = Tk()
            Window.title('Dictionary controller')
            Window.geometry('300x300')
        else:
            Window = self.tk
            Window.deiconify()

        Label(master=Window, text='Tracks numbers (splitting symbol is \',\')').place(y=0)
        self.DirtyTracks = Text(master=Window)
        self.DirtyTracks.place(x=0, y=25, height=50, width=250)
        Label(master=Window, text='Senders name (splitting symbol is \',\')').place(y=80)
        self.DirtySenders = Text(master=Window)
        self.DirtySenders.place(y=105, height=50, width=250)

        ButtonFrame = Frame(Window)
        lb = Button(master=ButtonFrame, text='  Load from config.py ', command=self.GetDictFromConfig(), )
        lb.place(y=175)
        lb.pack(side=LEFT)
        db = Button(master=ButtonFrame, text='Dump dict in config.py', command=self.PutDictInConfig(),)
        db.place(y=175)
        db.pack(side=RIGHT)
        sb = Button(master=ButtonFrame, text='Create Track Dict', command=self.SpecialDoTrackList)
        sb.place(y=215, x=0)
        sb.pack(side=TOP)
        ButtonFrame.pack(side=BOTTOM)
        Window.mainloop()

    def ConstructText(self, TracksDict=None):
        self.tk.deiconify()
        if not TracksDict:
            TracksDict = self.TracksDict
        if not TracksDict:
            Button(self.tk, text='Create track dictionary', command=lambda: self.ConstructTracksDict(True)).place(x=0, y=0)

            TracksDict = self.TracksDict

        TrackCodes = []
        Tabs = []
        tab_control = ttk.Notebook(self.tk)



        #mainloop = threading.Thread(target=self.MainLoop())

        #while self.wait:pass    #it's trap Johny!

        c = 0
        for x in TracksDict:
            c += 1
            Tabs.append(ttk.Frame(tab_control))
            tab_control.add(Tabs[c-1],text=x)

        tab_control.pack(expand=0, fill='both')
        self.tk.mainloop()



i = Interface(Creator='/dev/null',)
i.ConstructTracksDict()

