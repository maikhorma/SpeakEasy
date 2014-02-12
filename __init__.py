import eg

eg.RegisterPlugin(
    name = "SpeakEasy",
    author = "MaikHorma",
    version = "0.0.1",
    kind = "other",
    description = "Uses built in speech recognition of windows 7 to convert words to events.",
    #NEED to get this a LOT smaller
    icon = "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"
)

import speech
import time
from threading import Event, Thread
import wx

DEFAULT_WORDS = 'roger,start,notepad,command,system,close,help,lock,shutdown,reboot,cancel,mute,save'

class SpeakEasy(eg.PluginBase):
    counter = 0
    
    def __init__(self):
        self.AddEvents()
        self.AddAction(Speaker)

    def __start__(self,words):
        self.wordList = words.split(',')
        def followUp(plugin):
            Event().wait(4)
            plugin.counter -= 1
            if plugin.counter <= 0:
                plugin.TriggerEvent("DIE")
                plugin.counter = 0
        
        def callback(phrase, listener):
            self.counter += 1
            self.TriggerEvent("ANY")
            self.TriggerEvent(phrase)
            Thread(target=followUp, args=(self,)).start()
            
        speech.listenfor(self.wordList,callback)
        
    def __stop__(self):
        speech.stoplistening()
        
    def Configure(self,words=DEFAULT_WORDS):
        panel = eg.ConfigPanel()
        labelField = wx.StaticText(panel,-1,'Known words:')
        textCtrl = wx.TextCtrl(panel,-1,words)
        topSizer = wx.FlexGridSizer(2,0,2,15)
        topSizer.AddGrowableCol(0,1)
        topSizer.AddGrowableCol(1,1) 
        topSizer.Add(labelField,0,wx.EXPAND)
        topSizer.Add(textCtrl,0,wx.EXPAND)    
        panel.sizer.Add(topSizer,0,wx.EXPAND)
        while panel.Affirmed():
            panel.SetResult(textCtrl.GetValue())

class Speaker(eg.ActionBase):

    def __call__(self, word):
        speech.say(word)

    def Configure(self, word=""):
        panel = eg.ConfigPanel()
        textControl = wx.TextCtrl(panel, -1, word)
        panel.sizer.Add(textControl, 1, wx.EXPAND)
        while panel.Affirmed():
            panel.SetResult(textControl.GetValue())        