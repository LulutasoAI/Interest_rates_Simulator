from matplotlib import pyplot as plt
class Interest_Simulator:
    def __init__(self) -> None:
        self.is_init = False
        self.wallet = 0
        self.wallet_history = []
        self.debt_history = []

    def setup(self, capital, borrow, interest_rate,months, income = 0):
        if not self.is_init:
            self.capital = capital 
            self.borrow = borrow 
            self.interest_rate = interest_rate
            self.monthly_interest_rate = self.interest_rate / 12
            self.months = months 
            self.wallet = 0
            self.pay_back_per_iter = self.borrow //self.months
            self.is_init = True 
            self.income = income
            self.monthly_income = self.income // 12
            print("done")
        else:
            print("denied")

    def show_setting(self):
        print("原資 : ", self.capital)
        print("借入金 : ", self.borrow )
        print("利率 : ",self.interest_rate)
        print("残り返済回数 : ",self.months)
        print("毎月返済額 : ", self.pay_back_per_iter)
        print("手元資金 : ", self.wallet)
        print("毎月収入 : ", self.monthly_income)
        print("年間売り上げ : ", self.income)

    def iteration(self):
        if self.months == 0:
            print("Simulation done")
            return False
        self.borrow *= (1+self.monthly_interest_rate)
        payment = self.borrow // self.months
        self.borrow -= payment
        self.wallet -= payment
        self.wallet += self.monthly_income
        self.months -= 1 
        self.wallet_history.append(self.wallet)
        self.debt_history.append(self.borrow)
        if self.months % 12 == 0:
            self.report_status()
        return True 
    
    def visualize_history(self):
        plt.plot(self.wallet_history, label = "wallet")
        plt.plot(self.debt_history, label = "debt")
        plt.legend()
        plt.show()
        return True 
    
    def report_status(self):
        print("手元資金 : ", self.wallet)
        print("借入金 : ", self.borrow )
        return True
    def simulate(self):
        while self.iteration():
            pass
        print("Simulation done")
        print("手元資金 : ", self.wallet)
        print("借入金 : ", self.borrow )
        self.visualize_history()
        return True

        

if __name__ == "__main__":
    Simulator = Interest_Simulator()
    Simulator.setup(500000, 75000000, 0.04, 240, 5710000)
    Simulator.show_setting()
    Simulator.simulate()