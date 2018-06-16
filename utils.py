from itertools import combinations  as cchose
import numpy as np

class construce_alpa:
    def __init__(self,d):
        self.d = d
        self.a = np.arange(d)
        self.bet_k = self.construt_bet_k()
        self.constant = self.cal_concat()

    def temp_prod_sum(self,k):
        assert k<self.d,'The value of k must smaller than d. Value wrong'
        temp = list(cchose(self.a,k))
        temp_sum = 0
        for i in temp:
            temp_sum += np.prod(i)
        temp_sum *= (-1)**k
        return temp_sum    
    
    def construt_bet_k(self):
        bet_k = np.zeros(self.d)
        for k in np.arange(self.d):
            #coef = (-1)**(k)
            bet_k[k] = self.temp_prod_sum(k)
        return bet_k
    
    def cal_concat(self):
        temp = 1
        for i in range(1,self.d+1):
            temp = np.multiply(temp,i)
        return temp
    
    @property
    def get_bet_k(self):
        return self.bet_k
    
    @property
    def get_a(self):
        return self.a
    
    @property
    def get_k(self):
        return self.construt_bet_k
