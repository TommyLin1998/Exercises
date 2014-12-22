#! /usr/bin/env python

import wx

class HeightConverter(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, wx.ID_ANY, "Height Converter")

        self.panel = wx.Panel(self)

        self.prompt = wx.StaticText(self.panel, label="Enter your height:", pos=(10, 10))
        
        self.unitFeet = wx.StaticText(self.panel, label="ft", pos=(235, 10))

        self.unitInch = wx.StaticText(self.panel, label="in.", pos=(350, 10))
        
        self.response = wx.StaticText(self.panel, pos=(10, 40))

        self.feetBox = wx.TextCtrl(self.panel, pos=(130, 10))

        self.inchBox = wx.TextCtrl(self.panel, pos=(250, 10))

        self.btnSubmit = wx.Button(self.panel, label="Submit", pos=(255, 50))
        
	self.btnSubmit.Bind(wx.EVT_BUTTON, self.OnSubmit)

	self.cbRound = wx.CheckBox(self.panel, label="Round the answer", pos=(50, 100))

	self.cbRound.Bind(wx.EVT_CHECKBOX, self.OnToggleRound)

        self.cbRound.SetValue(False)

        self.cbMeter = wx.CheckBox(self.panel, label="Convert to meters", pos=(50, 70))

        self.cbMeter.Bind(wx.EVT_CHECKBOX, self.OnToggleMeter)

        self.cbRound.SetValue(False)

        self.cbRound.Show(False)

        self.cbMeter.Show(False)
        
	self.Show()

    def OnSubmit(self, e):

        feet = self.feetBox.GetValue()

        feet = float(feet)

        inch = self.inchBox.GetValue()

        inch = float(inch)

        centimeter = float((12 * feet + inch) * 2.54)

        self.response.SetLabel("Your height is {}cm".format(centimeter))

        self.cbMeter.Show(True)

    def OnToggleRound(self, e):

        isChecked = self.cbRound.GetValue()

        feet = self.feetBox.GetValue()

        feet = float(feet)

        inch = self.inchBox.GetValue()

        inch = float(inch)

        centimeter = float((12 * feet + inch) * 2.54)

        meter = float(centimeter / 100)

        if isChecked:
        
            meter = round(meter, 1)

            self.response.SetLabel("Your height is {}m".format(meter))

        else:

            self.response.SetLabel("Your height is {}m".format(meter))

    def OnToggleMeter(self, e):

        isChecked = self.cbMeter.GetValue()

        feet = self.feetBox.GetValue()

        feet = float(feet)

        inch = self.inchBox.GetValue()

        inch = float(inch)

        centimeter = float((12 * feet + inch) * 2.54)

        meter = float(centimeter / 100.0)

        if isChecked:

            self.response.SetLabel("Your height is {}m".format(meter))

            self.cbRound.Show(True)

        else:

            self.response.SetLabel("Your height is {}cm".format(centimeter))

            self.cbRound.Show(False)

app = wx.App(False)

frame = HeightConverter(None)

app.MainLoop()
