import msvcrt
import time

finish=10
count1=count2=count3=0
print "press enter key to get started"
raw_input()
s_time=time.time()

while(1):
	key1=msvcrt.getch()
	if key1=='d':
		count1=count1+1
		print "-->",
		if count1==finish:
			print "press S key"
			break
	else:
		print "\nYou lose,try again"
		quit()
while(1):
	key2=msvcrt.getch()
	if key2=='s':
		print 40*" "+"|"
		count2=count2+1
		if count2==finish:
			print 40*" "+"press D key"
			print 40*" ",
			break
	else:
		print "\nYou lose,try again"
		quit()
while(1):
	key3=msvcrt.getch()
	if key3=='d':
		count3=count3+1
		print "-->",
		if count3==finish:
			time_elapsed=time.time()-s_time
			print "\nCongrats you have completed the game"
			print "time taken is "+str(time_elapsed)
			break
	else:
		print "\nYou lose,try again"
		quit()

		
'''
1. Mention controls for the game.
'''
