class Interest_Simulator:
    def __init__(self) -> None:
        self.is_init = False 
        self.wallet = 0

    def setup(self, capital, borrow, interest_rate,times):
        if not self.is_init:
            self.capital = capital 
            self.borrow = borrow 
            self.interest_rate = interest_rate
            self.times = times 
            self.wallet = self.capital + self.borrow
            self.pay_back_per_iter = self.borrow //self.times
            self.is_init = True 
            print("done")
        else:
            print("denied")

    def show_setting(self):
        print("原資 : ", self.capital)
        print("借入金 : ", self.borrow )
        print("利率 : ",self.interest_rate)
        print("残り返済回数 : ",self.times)
        print("毎月返済額 : ", self.pay_back_per_iter)
        print("手元資金 : ", self.wallet)

    def iteration(self):
        if self.times == 0:
            print("Simulation done")
            return False
        self.borrow *= (1+self.interest_rate)
        self.borrow -= self.pay_back_per_iter
        self.wallet -= self.pay_back_per_iter
        self.times -= 1 
        return 1
        

        

if __name__ == "__main__":
    Simulator = Interest_Simulator()
    Simulator.setup(1500000, 15000000,0.03,60)
    Simulator.show_setting()