#! /usr/bin/env python

import wx

class HeightConverter(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, wx.ID_ANY, "Height Converter")

        self.panel = wx.Panel(self)

        self.prompt = wx.StaticText(self.panel, label="Enter your height:", pos=(10, 10))
        
        self.unit = wx.StaticText(self.panel, label="cm", pos=(235, 10))
        
        self.response = wx.StaticText(self.panel, pos=(10, 40))

        self.nameBox = wx.TextCtrl(self.panel, pos=(130, 10))

        self.btnSubmit = wx.Button(self.panel, label="Submit", pos=(275, 8))
	self.btnSubmit.Bind(wx.EVT_BUTTON, self.OnSubmit)

	self.Show()

    def OnSubmit(self, e):
        name = self.nameBox.GetValue()
        number = int(self.nameBox.GetValue())
        inch = float(number/2.54)
        feet = int(inch/12)
        newInch = float(inch - 12 * feet)
        self.response.SetLabel("Your height is {} ft and {} in.".format(feet, newInch))
                    
app = wx.App(False)

frame = HeightConverter(None)

app.MainLoop()
