# For Tester

```
class describeProductInfo: # Třída, která popisuje 
    def __init__(self, VATType = None, SalesPrExclVAT = None, PurchCostExclVAT = None):
        # VATType: VATTypes - Tady se píše jaký typ daně se použije na počítání zdanění.
        # SalesPrExclVAT: Dec - Tady je číslo (dec je číslo v desítkové soustavě), které popisuje Prodejní cenu bez DPH.
        # PurchCostExclVAT: Dec - Tady je číslo (dec je číslo v desítkové soustavě), které popisuje Nákupní cenu bez DPH.

        # Další proměnné

        # Vytvoření okna - uživatelského rozhraní


        # ----------------------------------------------------------------------
        # Frame, který zahrnuje v sobě výběr různých typů daní 


        # ----------------------------------------------------------------------
         # Frame, který zahrnuje v sobě INPUT, kam se udává částka (Prodejní cenu bez DPH)


        # ----------------------------------------------------------------------
        # Frame, který zahrnuje v sobě INPUT, kam se udává částka (Nákupní cenu bez DPH)


        # ----------------------------------------------------------------------
        # Vytvoření tlačítka, které po kliknutí spustí metodu


        # ----------------------------------------------------------------------
        # Frame, který zahrnuje v sobě všechny výpočty a vlastně OUTPUT programu


        # ----------------------------------------------------------------------
        # Frame, který má na staorsti hlášení různých chyb

    def callback(self):
          # Metoda, která je vyzvána tlačítkem
          # Stará se o správný vstup a vyzývá finální metodu

    def useVAT(self):
        # Metoda, která vytváří/vypočítává proměnné, které budou pužity do budoucna

    def calculateSalesMargin(self):
        # Napíše prodejní marži.
        # Rozdíl mezi prodejní a pořizovací cenou zboží, vyjádřeno korunově nebo procentuálně. Kdy za základ 100% bereme prodejní cenu.

    def calculateProfitAmount(self):
        # Napíše zisk včetně & bez daně (vybrané).

    def calculateSurcharge(self):
        # Napíše přirážku.
        # Vyjádření toho co jsme si k nákupní ceně přirazili. Základ (100%) pro výpočet je nákupní cena.

    def printProductInfo(self):
        # Finální metoda, která vyzýva nejdříve jednu metodu (pro vytvoření proměnných)
        # Potom vypíše pár výstupů
        # Vyzýva druhou metodu
        # Vypíše ostatní výstupy



if __name__ == '__main__':
    # vytvoření nové instance START třídy describeProductInfo
```
