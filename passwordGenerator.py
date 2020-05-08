#author: someoneHackingYourMom
#year: 2020


#some libraryes this program needs to make all the code work per
import os 
import sys
import random
import string

#random variable
n = random.randint(1,1000)


#generate random string function
def randomString(stringLength):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


if os.name == 'nt':
	clear = lambda: os.system('cls')
	clear()
else: 
	clear = lambda: os.system('clear')
	clear()
clear()
print ("Password Generator")
print ("author: SomeoneHackingYourMom")
print ("------------------")
print ("------------------")
print ("[1] generate a normal password with numbers and normal characters")
print ("[2] generate a super complex password")
print ("[3] what is a super complex password in this program?")
print ("[0] exit the program!")
print ("------------------")
print ("------------------")

choice = input("what is your choice[1][2][3]: ")
if (choice == "1"):
	lenght = input("kk, now tell me how long u want the password to be[enter a number]: ")
	lenghted = int(lenght)
	
	randompassword = randomString(lenghted)
	print ("your random password is " + randompassword)
elif (choice == "2"):
	print("Generating the super complex password!!")
	
	lenghted = randomString(n)
	lenghted.replace("a", "lawoidjg")
	lenghted.replace("b", "po2i3rbtnf")
	lenghted.replace("c", "iuaoPJNB")
	lenghted.replace("č", "PIDEG")
	lenghted.replace("d", "OPWEFMJIF")
	lenghted.replace("e", "SPOKNsdf")
	lenghted.replace("f", "G98PJLSN")
	lenghted.replace("g", "89OIQNGAO8FUS89I=iU")
	lenghted.replace("h", "ABFERGHQR")
	lenghted.replace("i", "hefhqer")
	lenghted.replace("j", "HR\"srhgWR")
	lenghted.replace("k", "WEIOUJGI3W")
	lenghted.replace("l", "p9qijregh")
	lenghted.replace("m", "vwp93roigt")
	lenghted.replace("n", "83q49jkh")
	lenghted.replace("o", "gz829'teg ")
	lenghted.replace("p", "zu2803ijpg")
	lenghted.replace("r", "2eogrbj")
	lenghted.replace("s", "031t92rhijo")
	lenghted.replace("š", "93480jiebk")
	lenghted.replace("t", "t398porwmk")
	lenghted.replace("u", "98zgut0jkm")
	lenghted.replace("v", "ut3gemlkf")
	lenghted.replace("z", "iuogb")
	lenghted.replace("ž", "riu8erjinr")
	lenghted.replace("x", "joewfkl ")
	lenghted.replace("y", "uioternk")
	lenghted.replace("1", "78r9uej")
	lenghted.replace("2", "8ru9i'ok")
	lenghted.replace("3", "3gre")
	lenghted.replace("4", "3rijweopmlk,")
	lenghted.replace("5", "wrgfer23rtg")
	lenghted.replace("6", "hetr34zhmzh")
	lenghted.replace("7", "3zthr3zt4zh")
	lenghted.replace("8", "3rht3z4z")
	lenghted.replace("9", "h3zt3trht")
	lenghted.replace("=", "34ztjr4t32")
	print ("your random password is " + lenghted)
elif (choice == "3"):
	print ("A super complex password in this program is a password that will be generated\nwith a lenght between 1 and 1000 characters included with numbers and letters")
	sys.exit()
elif (choice == "0"):
	if os.name == 'nt':
		clear = lambda: os.system('cls')
		clear()
	else:
		clear = lambda: os.system('clear')
		clear()
	sys.exit()
else:
	print ("please reply with only 1 or 2!")
	sys.exit()





