message = ['Uptime:  8 days', 'Load:    0.09 0.06', 'Temp:    29 celcius', 'Space:   0.9T/7.2T', 'Cur playing: 1', 'KevinMidboe:Angie Tribeca']

print(message)
message.reverse()
print(message)

for i in range(len(message)):
	print(message.pop())