#! /usr/bin/env python

import wx

class HeightConverter(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, wx.ID_ANY, "Height Converter")

        self.panel = wx.Panel(self)

        self.prompt = wx.StaticText(self.panel, label="Enter your height:", pos=(10, 10))
        
        self.unitFeet = wx.StaticText(self.panel, label="ft", pos=(235, 10))

        self.unitInch = wx.StaticText(self.panel, label="in.", pos=(350, 10))
        
        self.response = wx.StaticText(self.panel, pos=(10, 55))

        self.feetBox = wx.TextCtrl(self.panel, pos=(130, 10))

        self.inchBox = wx.TextCtrl(self.panel, pos=(250, 10))

        self.btnSubmit = wx.Button(self.panel, label="Submit", pos=(255, 50))
        
	self.btnSubmit.Bind(wx.EVT_BUTTON, self.OnSubmit)

	self.Show()

    def OnSubmit(self, e):
        
        feet = self.feetBox.GetValue()
        
        feet = float(feet)
        
        inch = self.inchBox.GetValue()
        
        inch = float(inch)
        
        centimeter = float((12 * feet + inch) * 2.54)
        
        centimeter = round(centimeter, 2)
        
        self.response.SetLabel("Your height is {}cm".format(centimeter))
                    
app = wx.App(False)

frame = HeightConverter(None)

app.MainLoop()
