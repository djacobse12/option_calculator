"""
Option price calculator
calculating gain from option price per share, current stock price per share... etc

Derek Jacobsen
4/30/20
"""

import numpy as np
import tkinter as tk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def main():
    """ put stuff here to run in the background and keep window alive (?)"""
    #print('hello world')

    window = main_window_gui()

    # is this necessary?  try updating the window instead of distroying and using this to
    # recreate it.

class main_window_gui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # setup title and define window
        self.title(' Option price calculator ')
        tk.Frame(self.geometry('800x600'))

        # place subject headers
        tk.Label(self, text = ' option strategy ', font = 'bold, 20').place(relx = 0.1,
                                                                              rely = 0.1)
        tk.Label(self, text = 'Buy / Sell').place(relx = 0.1, rely = 0.2)
        tk.Label(self, text = 'Call / Put').place(relx = 0.2, rely = 0.2)
        tk.Label(self, text = 'strike price').place(relx = 0.3, rely = 0.2)
        tk.Label(self, text = 'option price per share').place(relx = 0.4, rely = 0.2)
        tk.Label(self, text = ' current underlying stock price ').place(relx = 0.6, rely = 0.2)
        tk.Label(self, text = '#').place(relx = 0.045, rely = 0.2)

        # place call / put buttons

        #nrows = 3
        row1 = self.rowTags()
        row2 = self.rowTags()
        row3 = self.rowTags()

        # row 1
        call1Button = tk.Checkbutton(self, text = 'call', indicatoron = 0, command = row1.setFN,
                                     variable = row1.callTag)
        call1Button.place(relx = 0.2, rely = 0.3)

        put1Button = tk.Checkbutton(self, text = 'put', indicatoron = 0, command = row1.setFN,
                                    variable = row1.putTag)
        put1Button.place(relx = 0.25, rely = 0.3)

        # row 2
        call2Button = tk.Checkbutton(self, text='call', indicatoron=0, command=row2.setFN,
                                     variable=row2.callTag)
        call2Button.place(relx=0.2, rely=0.4)

        put2Button = tk.Checkbutton(self, text='put', indicatoron=0, command=row2.setFN,
                                    variable=row2.putTag)
        put2Button.place(relx=0.25, rely=0.4)

        # row 3
        call3Button = tk.Checkbutton(self, text='call', indicatoron=0, command=row3.setFN,
                                     variable=row3.callTag)
        call3Button.place(relx=0.2, rely=0.5)

        put3Button = tk.Checkbutton(self, text='put', indicatoron=0, command=row3.setFN,
                                    variable=row3.putTag)
        put3Button.place(relx=0.25, rely=0.5)

        # place buy/sell buttons

        # row 1
        buy1Button = tk.Checkbutton(self, text = 'buy', indicatoron = 0, command = row1.setFN,
                                    variable = row1.buyTag)
        buy1Button.place(relx = 0.1, rely = 0.3)

        sell1Button = tk.Checkbutton(self, text = 'sell', indicatoron = 0, command = row1.setFN,
                                     variable = row1.sellTag)
        sell1Button.place(relx = 0.15, rely = 0.3)

        # row 2
        buy2Button = tk.Checkbutton(self, text='buy', indicatoron=0, command=row2.setFN,
                                    variable=row2.buyTag)
        buy2Button.place(relx=0.1, rely=0.4)

        sell2Button = tk.Checkbutton(self, text='sell', indicatoron=0, command=row2.setFN,
                                     variable=row2.sellTag)
        sell2Button.place(relx=0.15, rely=0.4)

        # row 3
        buy3Button = tk.Checkbutton(self, text='buy', indicatoron=0, command=row3.setFN,
                                    variable=row3.buyTag)
        buy3Button.place(relx=0.1, rely=0.5)

        sell3Button = tk.Checkbutton(self, text='sell', indicatoron=0, command=row3.setFN,
                                     variable=row3.sellTag)
        sell3Button.place(relx=0.15, rely=0.5)

        # place price entries

        # row 1
        strikeP1Entry = tk.Entry(self, width = 7)
        strikeP1Entry.insert(0,'0.00')
        strikeP1Entry.place(relx = 0.3, rely = 0.3)
        row1.strikePrice = strikeP1Entry

        optionP1Entry = tk.Entry(self, width = 10)
        optionP1Entry.insert(0,'0.00')
        optionP1Entry.place(relx = 0.425, rely = 0.3)
        row1.optionPrice = optionP1Entry

        currentP1Entry = tk.Entry(self, width = 10)
        currentP1Entry.insert(0,'0.00')
        currentP1Entry.place(relx = 0.65, rely = 0.3)
        row1.currentPrice = currentP1Entry

        # row 2
        strikeP2Entry = tk.Entry(self, width=7)
        strikeP2Entry.insert(0,'0.00')
        strikeP2Entry.place(relx=0.3, rely=0.4)
        row2.strikePrice = strikeP2Entry

        optionP2Entry = tk.Entry(self, width=10)
        optionP2Entry.insert(0,'0.00')
        optionP2Entry.place(relx=0.425, rely=0.4)
        row2.optionPrice = optionP2Entry

        currentP2Entry = tk.Entry(self, width=10)
        currentP2Entry.insert(0,'0.00')
        currentP2Entry.place(relx=0.65, rely=0.4)
        row2.currentPrice = currentP2Entry

        # row 3
        strikeP3Entry = tk.Entry(self, width=7)
        strikeP3Entry.insert(0,'0.00')
        strikeP3Entry.place(relx=0.3, rely=0.5)
        row3.strikePrice = strikeP3Entry

        optionP3Entry = tk.Entry(self, width=10)
        optionP3Entry.insert(0,'0.00')
        optionP3Entry.place(relx=0.425, rely=0.5)
        row3.optionPrice = optionP3Entry

        currentP3Entry = tk.Entry(self, width=10)
        currentP3Entry.insert(0,'0.00')
        currentP3Entry.place(relx=0.65, rely=0.5)
        row3.currentPrice = currentP3Entry

        # place quantity entries
        # remember to int(entry.get()) so the string '1' isn't a string.  I don't think it will
        # be but honestly, who knows and I can see that being a problem later.
        # row 1
        quant1Entry = tk.Entry(self, width = 3)
        quant1Entry.insert(0,'0')
        quant1Entry.place(relx = 0.045, rely = 0.3)
        row1.quantity = quant1Entry

        # row 2
        quant2Entry = tk.Entry(self, width=3)
        quant2Entry.insert(0, '0')
        quant2Entry.place(relx=0.045, rely=0.4)
        row2.quantity = quant2Entry

        # row 3
        quant3Entry = tk.Entry(self, width=3)
        quant3Entry.insert(0, '0')
        quant3Entry.place(relx=0.045, rely=0.5)
        row3.quantity = quant3Entry


        # run button
        self.runHistory = 0
        self.r1 = row1
        self.r2 = row2
        self.r3 = row3
        runButton = tk.Button(self, text=' run ', fg='green', command = self.calcFN)
        runButton.place(relx=0.75, rely=0.1)

        # keep the party going
        self.mainloop()


    class rowTags():
        def __init__(self):
            self.callTag = tk.IntVar()
            self.putTag = tk.IntVar()
            self.buyTag = tk.IntVar()
            self.sellTag = tk.IntVar()
            self.currentPrice = 0
            self.optionPrice = 0
            self.quantity = 0
            self.buttonHistory = []
            self.m = 100
            self.strikePrice = 0

        def setFN(self):
            call = self.callTag.get()
            put = self.putTag.get()
            buy = self.buyTag.get()
            sell = self.sellTag.get()

            if call == 1 and put == 1:
                call = 1 - self.buttonHistory[-1][0]
                put = 1 - self.buttonHistory[-1][1]
                self.callTag.set(call)
                self.putTag.set(put)

            if buy == 1 and sell == 1:
                buy = 1 - self.buttonHistory[-1][2]
                sell = 1 - self.buttonHistory[-1][3]
                self.buyTag.set(buy)
                self.sellTag.set(sell)

            self.buttonHistory.append([call, put, buy, sell])

            #print(str(call) + ', ' + str(put) + ', ' + str(buy) + ', ' + str(sell))





    def calcFN(self):
        #print('hello again')
        #print(str(self.r1.optionPrice.get()))

        # get variables back
        row1 = self.r1
        row2 = self.r2
        row3 = self.r3

        trows = [row1, row2, row3]
        gains = []
        cpsDif = []
        m = 100
        bec = []
        bep = []
        breakEven = 0

        # calculate gain per share
        # PUTS: gain = (strike) - (current price) - (option price) + (opSale - strikeSale)
        # CALLS: gain = (current price) - (strike) - (option price) + (opSale - strikeSale)
        # sell calls at a higher strike than strike bought ???
        # sell puts at a lower strike than strike bought ???
        # see notes working out each condition

        for row, i in zip(trows, range(len(trows))):
            cpsDif.append(float(row.strikePrice.get()) - float(row.currentPrice.get()))

            if row.putTag.get() == 1:
                bep.append(float(row.strikePrice.get()) - float(row.optionPrice.get()))
                bec.append(0)
            elif row.callTag.get() == 1:
                cpsDif[i] = cpsDif[i] * -1
                bec.append(float(row.strikePrice.get()) + float(row.optionPrice.get()))
                bep.append(0)

            if row.putTag.get() == 1 and float(row.currentPrice.get()) > float(
                    row.strikePrice.get()):
                cpsDif[i] = 0
            elif row.callTag.get() == 1 and float(row.currentPrice.get()) < float(
                    row.strikePrice.get()):
                cpsDif[i] = 0

            gains.append(cpsDif[i] - float(row.optionPrice.get()))

            if row.sellTag.get() == 1:
                gains[i] = -1 * gains[i]

            gains[i] = gains[i] * float(row.quantity.get())

            if row.buyTag.get() == 1 and row.putTag.get() == 1 and float(row.quantity.get()) != 0:
                breakEven = breakEven + float(row.strikePrice.get()) - float(row.optionPrice.get())
            elif row.sellTag.get() == 1 and row.putTag.get() == 1 and float(row.quantity.get()) != 0:
                breakEven = breakEven + float(row.optionPrice.get())
            elif row.buyTag.get() == 1 and row.callTag.get() == 1 and float(row.quantity.get()) != 0:
                breakEven = breakEven + float(row.strikePrice.get()) + float(row.optionPrice.get())
            elif row.sellTag.get() == 1 and row.callTag.get() == 1 and float(row.quantity.get()) != 0:
                breakEven = breakEven - float(row.optionPrice.get())

        for row in trows:
            if row.buyTag.get() == 1 and row.putTag.get() == 1 and breakEven > \
                    float(row.strikePrice.get()):
                breakEven = float(row.strikePrice.get())

            elif row.buyTag.get() == 1 and row.callTag.get() == 1 and breakEven < \
                    float(row.strikePrice.get()):
                breakEven = float(row.strikePrice.get())



        gainPShare = sum(gains)


        # contract worth
        # worth = (gain) * (quantity) * (m)

        worthTotal = gainPShare * m

        # break even price
        # PUTS: (break even) = (strike) - (option price)
        # CALLS: (break even) = (strike) + (option price)


        # print('gain per share: ' + str(gainPShare))
        # print('contract worth: ' + str(worthTotal))
        # print('break even price: ' + str(breakEven))

        second_win = output_window(gainPShare, worthTotal, breakEven, trows)
        # if self.runHistory == 0:
        #     self.runHistory += 1
        # else:
        #     second_win.dfn()
        #     second_win = output_window(gainPShare, worthTotal, breakEven, trows)
        #     self.runHistory += 1
        # print(str(self.runHistory))


class output_window(tk.Tk):
    def __init__(self, gainPShare, worthTotal, breakEven, trows):
        tk.Tk.__init__(self)

        # title / window
        self.title(' Option strategy summary ')
        tk.Frame(self.geometry('900x600'))

        # general labels / text
        tk.Label(self, text = ' Strategy ', font = 'bold, 20').place(relx = 0.05, rely = 0.1)
        tk.Label(self, text = 'buy option').place(relx = 0.05, rely = 0.15)
        tk.Label(self, text = 'strike price').place(relx = 0.05, rely = 0.25)
        tk.Label(self, text = 'sold option').place(relx = 0.05, rely = 0.35)

        tk.Label(self, text = 'gain per share').place(relx = 0.05, rely = 0.65)
        tk.Label(self, text = 'contract worth').place(relx = 0.05, rely = 0.75)
        tk.Label(self, text = 'break even price').place(relx = 0.05, rely = 0.85)

        # passed calc labels
        tk.Label(self, text = str(gainPShare)).place(relx = 0.2, rely = 0.7)
        tk.Label(self, text = str(worthTotal)).place(relx = 0.2, rely = 0.8)
        tk.Label(self, text = str(breakEven)).place(relx = 0.2, rely = 0.9)

        # filling in info from trows
        sopt = ' 0 / 0 '
        for row in trows:
            if row.buyTag.get() == 1:
                if row.putTag.get() == 1:
                    buyOpt = 'put'
                elif row.callTag.get() == 1:
                    buyOpt = 'call'

                stpr = row.strikePrice.get()

                cpr = float(row.currentPrice.get())

            elif row.sellTag.get() == 1 and float(row.quantity.get()) != 0:
                if row.putTag.get() == 1:
                    sopt = 'put / ' + row.strikePrice.get()
                elif row.callTag.get() == 1:
                    sopt = 'call / ' + row.strikePrice.get()

        tk.Label(self, text = buyOpt).place(relx = 0.2, rely = 0.2)
        tk.Label(self, text = stpr).place(relx = 0.2, rely = 0.3)
        tk.Label(self, text = sopt).place(relx = 0.2, rely = 0.4)

        cpMin = 0.8 * cpr
        cpMax = 1.2 * cpr

        cpRange = np.linspace(cpMin, cpMax)
        gainRange = []

        for cpi in cpRange:
            gains = []
            cpsDif = []
            bec = []
            bep = []

            for row, i in zip(trows, range(len(trows))):
                cpsDif.append(float(row.strikePrice.get()) - cpi)

                if row.putTag.get() == 1:
                    bep.append(float(row.strikePrice.get()) - float(row.optionPrice.get()))
                    bec.append(0)
                elif row.callTag.get() == 1:
                    cpsDif[i] = cpsDif[i] * -1
                    bec.append(float(row.strikePrice.get()) + float(row.optionPrice.get()))
                    bep.append(0)

                if row.putTag.get() == 1 and cpi > float(
                        row.strikePrice.get()):
                    cpsDif[i] = 0
                elif row.callTag.get() == 1 and cpi < float(
                        row.strikePrice.get()):
                    cpsDif[i] = 0

                gains.append(cpsDif[i] - float(row.optionPrice.get()))

                if row.sellTag.get() == 1:
                    gains[i] = -1 * gains[i]

                gains[i] = gains[i] * float(row.quantity.get())

            gainPShare0 = sum(gains)

            gainRange.append(gainPShare0)

        plt.close('all')
        plt.figure(1)
        plt.plot(cpRange, gainRange)
        plt.plot(cpr, gainPShare, '.r')
        plt.xlabel(' Current stock price ')
        plt.ylabel(' gain per share ')
        #plt.show()

        fig = plt.figure(1)

        canvas = FigureCanvasTkAgg(fig, master = self)
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        canvas.get_tk_widget().place(relx = 0.3, rely = 0.1)
        toolbar.place(relx = 0.5, rely = 0.9)

        # keep the party going
        self.mainloop()

    def dfn(self):
        self.destroy()











main()

