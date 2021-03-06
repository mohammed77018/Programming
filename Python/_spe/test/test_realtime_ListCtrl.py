#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4 on Sun Nov 20 19:04:45 2005

import wx

import sys
from _spe.sm.wxp.realtime import ListCtrl
#from wx import ListCtrl #to compare

TAG     = '#todo:'
TAGLEN  = len(TAG)

class Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Frame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.statusbar = self.CreateStatusBar(1, 0)
        self.listCtrl = ListCtrl(self, -1, style=wx.LC_REPORT)
        self.source = wx.TextCtrl(self, -1, "#todo:red\nblue", style=wx.TE_MULTILINE)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        self.finish()

    def __set_properties(self):
        # begin wxGlade: Frame.__set_properties
        self.SetTitle("Realtime ListCtrl Demo - SPE widget")
        self.SetSize((400, 300))
        self.statusbar.SetStatusWidths([-1])
        # statusbar fields
        statusbar_fields = ["Right click on any item to display its line number in the statusbar."]
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(statusbar_fields[i], i)
        self.source.SetBackgroundColour(wx.Colour(255, 135, 127))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Frame.__do_layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.listCtrl, 1, wx.EXPAND, 0)
        sizer.Add(self.source, 1, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer)
        self.Layout()
        # end wxGlade
        
    def finish(self):
        self.listCtrl.InsertColumn(0,'Line',wx.LIST_FORMAT_LEFT,40)
        self.listCtrl.InsertColumn(1,'!',wx.LIST_FORMAT_LEFT,20)
        self.listCtrl.InsertColumn(2,'Task',wx.LIST_FORMAT_LEFT,500)
        self.Bind(wx.EVT_IDLE,self.onIdle)
        
    def onIdle(self,event):
        source          = [(line,index) for index, line in enumerate(self.source.GetValue().split('\n'))]
        source.sort()
        self.listCtrl.DeleteAllItems()
        for line, index in source:
            if line[:TAGLEN] == TAG:
                item    = self.listCtrl.InsertStringItem(sys.maxint, str(index+1))
                self.listCtrl.SetStringItem(item, 1, str(line.count('!')))
                self.listCtrl.SetStringItem(item, 2, line[TAGLEN:])
                if 'blue' in line:
                    self.listCtrl.SetItemBackgroundColour(item,wx.BLUE)
                elif 'green' in line:
                    self.listCtrl.SetItemBackgroundColour(item,wx.GREEN)
                elif 'red' in line:
                    self.listCtrl.SetItemBackgroundColour(item,wx.RED)
                else:
                    self.listCtrl.SetItemBackgroundColour(item,wx.WHITE)
        self.listCtrl.Update()

# end of class Frame


class App(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame = Frame(None, -1, "")
        self.SetTopWindow(frame)
        frame.Show()
        return 1

# end of class App

if __name__ == "__main__":
    app = App(0)
    app.MainLoop()
