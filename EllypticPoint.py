import math

class EllypticPoint:
    def __init__(self,x,y,a,b,p,inf = False):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.p = p
        self.inf = inf

    def printPoint(self):
        print("(%d:%d)"%(self.x,self.y))

    def __add__(self,obj):
        if isinstance(obj,EllypticPoint):
            if(self.inf):
                return obj
            if(obj.inf):
                return self
            if(self.x == obj.x and self.y == obj.y):
                k = EllypticPoint.divisionInFiniteField(((3*self.x*self.x+self.a)% self.p),(2*self.y) %self.p,self.p);
            else:
                k = EllypticPoint.divisionInFiniteField((obj.y - self.y)% self.p,(obj.x - self.x)% self.p,self.p)
            if(k == "Infinity"):
                return EllypticPoint(0,0,self.a,self.b,self.p,True)
            else:
                result_x = (k*k - self.x - obj.x) % self.p
                result_y = (k*(self.x - result_x)-self.y) % self.p
                return EllypticPoint(result_x,result_y,self.a,self.b,self.p)
        else:
            return self    
    
    def divisionInFiniteField(a,b,module):
        if b == 0:
            return "Infinity"
        if math.floor(a/b)*b == a:
            return a/b
        res = -1
        for i in range(1,b):
            if b*i % module == 1:
                res = i
                break
        return a*res % module


    def kPoint(self,number):
        result = EllypticPoint(0,0,self.a,self.b,self.p,True)
        for i in range(1,number+1):
            result = result + self
        return result