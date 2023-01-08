# Question 1

import math

class SquareRoot:
    c = 50
    h = 30
    # d = int()
    
    def __init__(self, D) -> None:
        self.d = D
    
    def square_root(self):
        result = []
        for i in self.d:
            Q = round(math.sqrt(2 * 50 * int(i) / 30))
            result.append(Q)
        
        return result

if __name__ == "__main__":
    numbers = input("Provide D: ")
    d = numbers.split(',')
    
    obj = SquareRoot(d)
    
    Q = obj.square_root()
    
    print(Q)



    