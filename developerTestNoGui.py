class describeProductInfo:
    def __init__(self, VATType, SalesPrExclVAT, PurchCostExclVAT):
        self.VATType = VATType  # variable describes type of VAT
        self.SalesPrExclVAT = SalesPrExclVAT  # variable describes Sales Price Excluding VAT
        self.PurchCostExclVAT = PurchCostExclVAT  # variable describes Purchase Cost Excluding VAT

    def useVAT(self):
        if self.VATType == 'Base':  # VAT type
            SalesPrInclVAT = self.SalesPrExclVAT * 1.21
            self.SalesPrInclVAT = SalesPrInclVAT

            PurchCostInclVAT = self.PurchCostExclVAT * 1.21
            self.PurchCostInclVAT = PurchCostInclVAT

        elif self.VATType == 'Reduced1':  # VAT type
            SalesPrInclVAT = self.SalesPrExclVAT * 1.15
            self.SalesPrInclVAT = SalesPrInclVAT

            PurchCostInclVAT = self.PurchCostExclVAT * 1.15
            self.PurchCostInclVAT = PurchCostInclVAT

        elif self.VATType == 'Reduced2':  # VAT type
            SalesPrInclVAT = self.SalesPrExclVAT * 1.10
            self.SalesPrInclVAT = SalesPrInclVAT

            PurchCostInclVAT = self.PurchCostExclVAT * 1.10
            self.PurchCostInclVAT = PurchCostInclVAT

        elif self.VATType == 'NoVAT':  # VAT type
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

        print("Sales Price Incl. VAT is: " + str(round((self.SalesPrInclVAT), 2)) + " Kč", end="\n\n")

        print("Sales Margin is " + str(self.calculateSalesMargin()) + "%", end="\n\n")

        self.calculateProfitAmount()
        print("Profit Amount is:")
        print("   Including VAT - " + str(self.profitAmmountInclVAT) + " Kč")
        print("   Excluding VAT - " + str(self.profitAmmountExclVAT) + " Kč", end="\n\n")

        print("Surcharge is " + str(self.calculateSurcharge()) + "%", end="\n\n")


if __name__ == '__main__':
    VATType = str(input("Write VAT Type (Base, Reduced1, Reduced2, NoVAT).\n"))
    if VATType == 'Base' or VATType == 'Reduced1' or VATType == 'Reduced2' or VATType == 'NoVAT':
        print("OK\n")
    else:
        print("Wrong VAT Type written.")
        exit()
    while True:
        try:
            SalesPrExclVAT = float(input("Sales Price Excluding VAT.\n"))
            PurchCostExclVAT = float(input("Purchase Cost Excluding VAT.\n"))
            break
        except ValueError:
            print("You didn't enter a number.\n")

    print("\n\n")
    start = describeProductInfo(VATType, SalesPrExclVAT, PurchCostExclVAT)
    start.printProductInfo()