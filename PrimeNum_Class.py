
class prime:
	
	def __init__(self):
	    pass
	    
	def setNumbers(self,x,y):
	    self.x = x
	    self.y = y
	
	def getPrimes(self):
	    if self.x<2:
	    	self.x=2
	    self.primes=[]
	    for i in range(self.x,self.y+1):
	    	self.primeCountA=0
	    	for j in range(2,i):
	    		if i%j==0:
	    			self.primeCountA+=1
	    	if self.primeCountA==0:
	    		self.primes.append(i)
	    return self.primes
	    
	def lenPrimes(self):
		try:
			return len(self.primes)
		except AttributeError:
			return("ERROR: Numbers Are Not Set [ Set The Numbers Using - object.setNumbers(int,int) ] ")
			
	def setNumber(self,k):
	    self.k=k
	
	def checkPrime(self):
		try:
		    self.countB=0
		    if self.k<2:
		        return f"{self.k} Is Neither A Prime Nor A Composite Number"
		    for l in range(2,self.k):
			    if l==self.k-1:
				    break
			    if self.k%l==0:
				    self.countB+=1
				
		    if self.countB>1:
			    return f"{self.k} Is Not A Prime Number"
				
		    if self.countB==0 and self.k>=2:
			    return f"{self.k} Is A Prime Number"
		except AttributeError:
			return("ERROR: Number Is Not Set [ Set The Number Using - object.setNumber(int) ] ")
								
	def divNums(self):
		try:
		    self.divs=[1]
		    for m in range(2,self.k):
			    if l==self.k-1:
				    self.divs.append(self.k)
				    break
			    if self.k%l==0:
				    self.divs.append(m)
		    return self.divs
		except AttributeError:
			del self.divs
			return("ERROR: Number Is Not Set [ Set The Number Using - object.setNumber(int) ] ")
	
a=prime()
a.setNumbers(0,100)
print(a.getPrimes())
print(a.lenPrimes())

print(a.checkPrime())
print(a.divNums())
