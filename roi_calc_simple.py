# This ROI Calculator works and is fully functional but is still kind of simple 


class RentalInfo():
    def __init__(self):
        self.totalmonthincome = ""
        self.totalmonthexpense = ""
        self.totalmonthcash = ""
        self.totalannualcash = ""
        self.totalinvestment = ""
        self.returnOnInvestment = ""

    def income(self, rent, laundry, storage, miscincome):

        # income = ROICalculator(rent, laundry, storage, miscincome)
        # self.totalmonthincome.append(income)
        print("Step 1 of the ROI Calculator is totaling your MONTHLY INCOME")
        print("Your total monthly income is: ")
        income = int(self.rent + self.laundry + self.storage +  self.miscincome)
        self.totalmonthincome.append(income)
        print(self.totalmonthincome)

    def expenses(self, taxes, insurance, utilities, miscexpense, mortgage):
        print("Step 2 is totaling your monthly expenses")
        self.totalmonthexpense = int(self.taxes + self.insurance + self.utilities +  self.miscexpense + self.mortgage)
        print(self.totalmonthexpense)
        # expenses_total = ROICalculator(taxes, insurance, utilities, miscexpense, mortgage)
        # self.totalmonthexpense.append(expenses_total)
        
    def cash_flow(self):
        print("Step 3 is calculating your cash flow")
        print("Your cash flow is equal to your income minus your monthly expenses.")
        # self.totalmonthcash = (int(self.totalmonthincome) - int(self.totalmonthexpense))
        print(f"So yours is: {self.totalmonthincome} minus {self.totalmonthexpense} equals {int(self.totalmonthincome) - int(self.totalmonthexpense)}")
        print(f"Your annual cash flow is: {(self.totalmonthincome - self.totalmonthexpense) * 12}")
    
    def investment(self):
        print("Step 3 is calculating your total investment in the house.")
        self.totalinvestment = self.downpay + self.closing + self.rehab + self.miscinv
        print(f"Your total investment on the property is: {self.totalinvestment}")

    def roi(self):
        print("Your total Return on investment (ROI) is calculated by dividing your Annual Cash Flow by your Total Investment")
        print(f"So in your case, we divide {self.totalannualcash} by {self.totalinvestment}")
        self.returnOnInvestment = self.totalannualcash / self.totalinvestment
        print(f"So your ROI is: {self.returnOnInvestment}")

    
class ROICalculator:
    def __init__(self):
        self.owner = RentalInfo()

    def run(self):
        # STEP 1:
        print("Step 1 of the ROI Calculator is totaling your monthly income...")
        
        self.rent = int(input("What is your rental income?: "))
        self.laundry = int(input("What is your laundry income?: "))
        self.storage = int(input("What is your storage income?: "))
        self.miscincome = int(input("Enter any other forms of misc income: "))

        if self.rent >= 0:
            print(f"Your monthly rent is {self.rent}")
        elif self.rent < 0:
            print("Please enter a number value!")

        if self.laundry >= 0:
            print(f"Your monthly laundry income is {self.laundry} ")
        elif self.laundry < 0:
            print("Please enter a number value!")

        if self.storage >= 0:
            print(f" Your monthly storage income is {self.storage}")
        elif self.storage < 0:
            print("Please enter a number value!")

        if self.miscincome >= 0:
            print(f"Your monthly misc income is {self.miscincome}")
        elif self.miscincome < 0:
            print("Please enter a number value!")
        # self.owner.income()
        print("Your total monthly income is: ")
        self.totalmonthincome = int(self.rent + self.laundry + self.storage +  self.miscincome)
        print(self.totalmonthincome)

        # STEP 2:
        print("Step 2 is totaling your monthly expenses...")
        self.taxes = int(input("What are your monthly taxes?: "))
        self.insurance = int(input("What is your monthly insurance?: "))
        self.utilities = int(input("What are your monthly utility expenses?: "))
        self.miscexpense = int(input("Enter any other monthly expenses such as HOA, repairs, & property management: "))
        self.mortgage = int(input("What is your monthly mortgage payment?: "))

        if self.taxes >= 0:
            print(f"Your monthly taxes are: {self.taxes}")
        elif self.taxes < 0:
            print("Please enter a number value!")

        if self.insurance >= 0:
            print(f"Your monthly insurance expenses are: {self.insurance} ")
        elif self.insurance < 0:
            print("Please enter a number value!")

        if self.utilities >= 0:
            print(f" Your monthly utilities expenses are: {self.utilities}")
        elif self.utilities < 0:
            print("Please enter a number value!")

        if self.miscexpense >= 0:
            print(f"Your monthly misc expenses are: {self.miscexpense}")
        elif self.miscexpense < 0:
            print("Please enter a number value!")

        if self.mortgage >= 0:
            print(f"Your monthly mortgage payment is: {self.mortgage}")
        elif self.mortgage < 0:
            print("Please enter a number value!")

        print(f"Your total monthly expenses are: ")
        self.totalmonthexpense = int(self.taxes + self.insurance + self.utilities +  self.miscexpense + self.mortgage)
        print(self.totalmonthexpense)

        #STEP 3
        # self.owner.cash_flow()
        print("Step 3 is calculating your cash flow...")
        print("Your cash flow is equal to your income minus your monthly expenses.")
        self.totalmonthcash = (int(self.totalmonthincome) - int(self.totalmonthexpense))
        print(f"So yours is: {self.totalmonthincome} minus {self.totalmonthexpense} equals {self.totalmonthcash}")
        self.totalannualcash = self.totalmonthcash * 12
        print(f"Your annual cash flow is: {self.totalannualcash}")

        # STEP 4
        # self.owner.investment()
        self.downpay = int(input("What was your total down payment on the house?: "))
        self.closing = int(input("What were your total closing costs?: "))
        self.rehab = int(input("What was your total rehab cost?: "))
        self.miscinv = int(input("Enter any other final costs: "))

        self.totalinvestment = self.downpay + self.closing + self.rehab + self.miscinv
        print(f"Your total investment on the property is: {self.totalinvestment}")

        # STEP 5:
        print("Your total Return on investment (ROI) is calculated by dividing your Annual Cash Flow by your Total Investment")
        print(f"So in your case, we divide {self.totalannualcash} by {self.totalinvestment} and multiply 100 for a %")
        self.returnOnInvestment = (self.totalannualcash / self.totalinvestment)*100
        print(f"So your ROI is: {self.returnOnInvestment}%")



roi = ROICalculator()
roi.run()
