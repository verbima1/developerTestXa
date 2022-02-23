import tkinter as tk

class describeProductInfo:
    def __init__(self, VATType = None, SalesPrExclVAT = None, PurchCostExclVAT = None):
        self.VATType = VATType # variable describes type of VAT
        self.SalesPrExclVAT = SalesPrExclVAT # variable describes Sales Price Excluding VAT
        self.PurchCostExclVAT = PurchCostExclVAT # variable describes Purchase Cost Excluding VAT

        # VATType: VATTypes - Tady se píše jaký typ daně se použije na počítání zdanění.
        # SalesPrExclVAT: Dec - Tady je číslo (dec je číslo v desítkové soustavě), které popisuje Prodejní cenu bez DPH.
        # PurchCostExclVAT: Dec - Tady je číslo (dec je číslo v desítkové soustavě), které popisuje Nákupní cenu bez DPH.

        self.SalesPrInclVAT = None # variable describes Sales Price Including VAT
        self.PurchCostInclVAT = None # variable describes Purchase Cost Including VAT
        self.profitAmmountExclVAT = None # variable describes Profit Excluding VAT
        self.profitAmmountInclVAT = None # variable describes Profit Including VAT

        self.window = tk.Tk(className=" Product Info ") # creating window app
        self.window.geometry("600x400") # setting width and height


        # ----------------------------------------------------------------------
        VATFrame = tk.Frame() # VAT Frame

        VATLabel = tk.Label(master=VATFrame, text="VAT Type") # VAT Label
        VATLabel.pack()

        VATOptions = [ # options
            'Base',
            'Reduced1',
            'Reduced2',
            'NoVAT'
        ]

        self.VATTypeOptions = tk.StringVar(master=VATFrame)
        self.VATTypeOptions.set(VATOptions[0])  # default value
        self.VATTypeGUI = tk.OptionMenu(VATFrame, self.VATTypeOptions, *VATOptions)
        self.VATTypeGUI.pack()

        VATFrame.pack()
        VATFrame.place(relx=.05, rely=.1)


        # ----------------------------------------------------------------------
        SalesPrExclVATFrame = tk.Frame()  # SalesPrExclVAT Frame

        SalesPrExclVATLabel = tk.Label(master=SalesPrExclVATFrame, text="Sales Price Excluding VAT")
        SalesPrExclVATLabel.pack()

        self.SalesPrExclVATGUI = tk.Entry(master=SalesPrExclVATFrame)
        self.SalesPrExclVATGUI.pack()

        SalesPrExclVATFrame.pack()
        SalesPrExclVATFrame.place(relx=.25, rely=.1)


        # ----------------------------------------------------------------------
        PurchCostExclVATFrame = tk.Frame()  # PurchCostExclVAT Frame

        PurchCostExclVATLabel = tk.Label(master=PurchCostExclVATFrame, text="Purchase Cost Excluding VAT")
        PurchCostExclVATLabel.pack()

        self.PurchCostExclVATGUI = tk.Entry(master=PurchCostExclVATFrame)
        self.PurchCostExclVATGUI.pack()

        PurchCostExclVATFrame.pack()
        PurchCostExclVATFrame.place(relx=.50, rely=.1)


        # ----------------------------------------------------------------------
        self.countButtonGUI = tk.Button(master=self.window, text="Count", command=self.callback, width=10, height=2) # Count button
        self.countButtonGUI.pack()
        self.countButtonGUI.place(relx=.85, rely=.85)


        # ----------------------------------------------------------------------
        responseFrame = tk.Frame(width= 100, height=100)
        responseFrame.grid(columnspan=2)

        firstResponse = tk.Label(master=responseFrame, text="Sales Price Incl. VAT is:   ").grid(column=0, row=0, sticky='w', ipady=5)
        self.firstText = tk.Label(master=responseFrame, text="None")
        self.firstText.grid(column=1, row=0)
        secondResponse = tk.Label(master=responseFrame, text="Sales Margin is:").grid(column=0, row=1, sticky='w', ipady=5)
        self.secondText = tk.Label(master=responseFrame, text="None")
        self.secondText.grid(column=1, row=1)
        thirdResponse = tk.Label(master=responseFrame, text="Profit Amount is:").grid(column=0, row=2, sticky='w', ipady=5)
        fourthResponse = tk.Label(master=responseFrame, text="Including VAT - ").grid(column=0, row=3, sticky='w', ipady=5)
        self.thirdText = tk.Label(master=responseFrame, text="None")
        self.thirdText.grid(column=1, row=3)
        fifthResponse = tk.Label(master=responseFrame, text="Excluding VAT - ").grid(column=0, row=4, sticky='w', ipady=5)
        self.fourthText = tk.Label(master=responseFrame, text="None")
        self.fourthText.grid(column=1, row=4)
        sixthResponse = tk.Label(master=responseFrame, text="Surcharge is:").grid(column=0, row=5, sticky='w', ipady=5)
        self.fifthText = tk.Label(master=responseFrame, text="None")
        self.fifthText.grid(column=1, row=5)

        responseFrame.pack()
        responseFrame.pack(expand=True)
        responseFrame.place(relx=.05, rely=.4)


        # ----------------------------------------------------------------------
        errorFrame = tk.Frame(width=50, height=20)
        errorFrame.grid(columnspan=2)

        errorType = tk.Label(master=errorFrame, text="Error:").grid(column=0, row=0, sticky='w', ipady=5)
        self.error = tk.Label(master=errorFrame, text="None", fg="red")
        self.error.grid(column=1, row=0)

        errorFrame.pack()
        errorFrame.pack(expand=True)
        errorFrame.place(relx=.4, rely=.85)

        self.window.mainloop()

    def callback(self):
            self.VATType = self.VATTypeOptions.get()

            if self.SalesPrExclVATGUI.get() == '' or self.PurchCostExclVATGUI.get() == '':
                self.error.config(text="No Input!")
                return

            containLettersSales = self.SalesPrExclVATGUI.get().lower().islower()
            containLettersPurch = self.PurchCostExclVATGUI.get().lower().islower()

            if not containLettersSales:
                self.SalesPrExclVAT = float(self.SalesPrExclVATGUI.get())
            else:
                self.error.config(text="The Sales Price Exclude VAT contains letters!")
                raise Exception("The Sales Price Exclude VAT contains letters!")

            if not containLettersPurch:
                self.PurchCostExclVAT = float(self.PurchCostExclVATGUI.get())
            else:
                self.error.config(text="The Sales Price Exclude VAT contains letters!")
                raise Exception("The Sales Price Exclude VAT contains letters!")


            if type(self.SalesPrExclVAT) == int:
                pass
            elif type(self.SalesPrExclVAT) == float:
                pass
            else:
                self.error.config(text="The Sales Price Exclude VAT is not Int or Float!")
                raise Exception("The SalesPrExclVAT is not Int or Float!")

            if type(self.PurchCostExclVAT) == int:
                pass
            elif type(self.PurchCostExclVAT) == float:
                pass
            else:
                self.error.config(text="The Purchase Cost Exclude VAT is not Int or FLoat!")
                raise Exception("The PurchCostExclVAT is not Int or FLoat!")

            self.error.config(text="None")
            self.printProductInfo()

    def useVAT(self):
        if self.VATType == 'Base': # VAT type
            SalesPrInclVAT = self.SalesPrExclVAT * 1.21
            self.SalesPrInclVAT = SalesPrInclVAT

            PurchCostInclVAT = self.PurchCostExclVAT * 1.21
            self.PurchCostInclVAT = PurchCostInclVAT

        elif self.VATType == 'Reduced1': # VAT type
            SalesPrInclVAT = self.SalesPrExclVAT * 1.15
            self.SalesPrInclVAT = SalesPrInclVAT

            PurchCostInclVAT = self.PurchCostExclVAT * 1.15
            self.PurchCostInclVAT = PurchCostInclVAT

        elif self.VATType == 'Reduced2': # VAT type
            SalesPrInclVAT = self.SalesPrExclVAT * 1.10
            self.SalesPrInclVAT = SalesPrInclVAT

            PurchCostInclVAT = self.PurchCostExclVAT * 1.10
            self.PurchCostInclVAT = PurchCostInclVAT

        elif self.VATType == 'NoVAT': # VAT type
            self.SalesPrInclVAT = self.SalesPrExclVAT
            self.PurchCostInclVAT = self.PurchCostExclVAT

    def calculateSalesMargin(self):
        # Print Sales Margin (Marže)
        # Napíše prodejní marži.
        # Rozdíl mezi prodejní a pořizovací cenou zboží, vyjádřeno korunově nebo procentuálně. Kdy za základ 100% bereme prodejní cenu.

        salesMargin = round((((self.SalesPrExclVAT - self.PurchCostExclVAT) / self.SalesPrExclVAT) * 100), 2)
        return salesMargin

    def calculateProfitAmount(self):
        # Print Profit Amount (Zisk) including & excluding VAT
        # Napíše zisk včetně & bez daně (vybrané).

        profitAmmountExclVAT = self.SalesPrExclVAT - self.PurchCostExclVAT
        self.profitAmmountExclVAT = profitAmmountExclVAT

        profitAmmountInclVAT = self.SalesPrInclVAT - self.PurchCostInclVAT
        self.profitAmmountInclVAT = profitAmmountInclVAT

    def calculateSurcharge(self):
        # Print Surcharge (Přirážka)
        # Napíše přirážku.
        # Vyjádření toho co jsme si k nákupní ceně přirazili. Základ (100%) pro výpočet je nákupní cena.

        surcharge = round((((self.SalesPrExclVAT - self.PurchCostExclVAT) / self.PurchCostExclVAT) * 100), 2)
        return surcharge

    def printProductInfo(self):
        self.useVAT()

        firstText = str(round((self.SalesPrInclVAT), 2)) + " Kč"
        self.firstText.config(text=firstText)

        secondText = str(self.calculateSalesMargin()) + "%"
        self.secondText.config(text=secondText)

        self.calculateProfitAmount()

        thirdText = str(round(self.profitAmmountInclVAT, 2)) + " Kč"
        self.thirdText.config(text=thirdText)

        fourthText = str(round(self.profitAmmountExclVAT, 2)) + " Kč"
        self.fourthText.config(text=fourthText)

        fifthText = str(self.calculateSurcharge()) + "%"
        self.fifthText.config(text=fifthText)



if __name__ == '__main__':
    start = describeProductInfo()
