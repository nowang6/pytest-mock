class ExchangeRater:
    def get_rate(self) -> int:
        return 6


class Caculator:
    rater = ExchangeRater()

    def dollar2rmb(self, dollar):
        return self.rater.get_rate()*dollar

    def add(self, a, b) -> int:
        return a + b
    
    def subtract(self, a, b) -> int:
        return a - b
    
    def multiply(self, a, b) -> int:
        return a * b
    
    def divide(self, a, b) -> int:
        return a * 1.0 / b