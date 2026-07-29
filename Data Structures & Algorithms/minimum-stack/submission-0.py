class MinStack:
    
    def __init__(self):
        self.s = []
        self.s_min = []

    def push(self, val: int) -> None:  
        self.s.append(val)
        
        if not self.s_min:
            self.s_min.append(val)
        else:
            self.s_min.append(min(self.s_min[-1],val))

    def pop(self) -> None:
        self.s.pop()
        self.s_min.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s_min[-1] 
