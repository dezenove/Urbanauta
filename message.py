class Message:
	
	def buildMessage(self):
		result = []
		overhead = self.messageCode << 4 | self.direction << 3 | self.responseType
		result.append(overhead)
		
		for item in self.data:
			result.append(item);
			
		return result
		
	def decodeMessage(message):
		result = Message()
		
		overhead = message[0]
		result.messageCode = (240 & overhead) >> 4
		result.direction = (8 & overhead) >> 3
		result.responseType = (7 & overhead)
		
		result.data = []
		for i in range(1, len(message)):
			result.data.append(message[i])
			
		return result
	decodeMessage = staticmethod(decodeMessage)