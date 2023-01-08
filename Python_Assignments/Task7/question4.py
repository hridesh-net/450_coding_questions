class Time:
    hours = 1
    minutes = 10
    
    def addTime(self, hrs, mins):
        self.hours = self.hours + hrs
        self.minutes = self.minutes + mins
        
        if (self.minutes >= 60):
            self.hours += 1
            self.minutes = self.minutes - 60
        
    def displayTime(self):
        print(str(self.hours) + "hrs and " + str(self.minutes) + "mins \n")
        
    def displayMinute(self):
        print("Minutes = " + str((self.hours * 60) + self.minutes))
        print("\n\n")
    
if __name__ == "__main__":
    obj = Time()
    
    obj.displayTime()
    obj.displayMinute()
    
    obj.addTime(2, 40)
    
    obj.displayTime()
    obj.displayMinute()