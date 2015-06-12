class socialNetwork:
	accountCount=0
	def __init__(self,username,dob,mobileNo):
		socialNetwork.accountCount+=1
		self.username=username
		self.dob=dob
		self.mobileNo=mobileNo
	def howMany():
		print("Total Account",socialNetwork.accountCount)
	def profile(self):
		print("username :"+self.username)
		print("Date of Birth :"+self.dob)
		print("MObile NUmber :"+self.mobileNo)


anil=socialNetwork("Anil","18/02/94","1234567")

anil.profile()
