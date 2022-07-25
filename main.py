#CyHelp Starter Code
cybersecBirthYear = 1970

#Greets user
print("\033[1;31;40mHello! I'm CyHelp.")
print ("What is your name?\033[0m")
userName = input("Your name: ")

print ("Nice to meet you " + userName + "!\n")
#Recounts start of Cybersecurity
print ("\033[1;31;40mWhat year is it?\033[0m")
todaysYear = input("The year: ")
timePassed = int(todaysYear) - cybersecBirthYear

print ("\n")

print("Wow! That means it has been " + str(timePassed) + " years since Cybersecurity began!")

print ("\n")

print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")

print ("\n")

input ("\033[1;31;40mPress enter to continue.\n\033[0m")

#Describes Cybersecurity
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from digital threats.")

print("These people can be government, nations, companies, community, organizations and individuals.\n")

#Introduces CIA Triad
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for confidentiality, integrity and avaliablity")


print ("Would you like to learn more about the CIA Triad?")
giveInfo = input("Type \033[1;31;40m'yes'\033[0m or \033[1;31;40m'no'\033[0m\n")


if giveInfo == "no" :
  print ("Ahhh so you're a rebel. Respect. But actually you should really go back and learn about the CIA Triad.")
#Explains pillars of CIA Triad
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n\n \033[1;33;40m(a) confidentiality\033[0m, \033[1;36;40m(b) integrity \033[0m,\033[1;35;40m(c) avaliablity\033[0m, or \033[1;32;40m(d) none\033[0m\n\n")
  
  userclick = input()
  
  if userclick.lower() == "a":
    print ("\033[1;33;40mConfidentiality makes sure data is private.\n\033[0m")
  
  elif userclick.lower() == "b":
    print("\033[1;36;40mIntegrity makes sure data has not been tampered with and can be trusted.\n\033[0m")
  
  elif userclick.lower() == "c":
    print("\033[1;35;40mAvaliability makes sure authorized people can access the data.\n\033[0m")
  
  elif userclick.lower() == "d":
    print("\033[1;32;40mThanks for chatting with me, and I hope you learned something new!\033[0m")
    break
  
  else:
    print ("Sorry, I didn't catch that. Please choose from the options listed.")
  
  print ("\n")
  #Chatbot ends conversation