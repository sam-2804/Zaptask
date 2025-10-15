import time
import os

websites_to_block = ["instagram.com","facebook.com"]                # List of websites to block

# Function that blocks the websites
def website_block():                                                            

    with open("C:/Windows/System32/drivers/etc/hosts","a+") as file:   # open the "hosts" file as file by using the "with open()"
        for websites in websites_to_block:                             # iterates through the websites_to_block list
            file.writelines("\n" + "127.0.0.1" + "    www." + websites )    # writes the ip adress and the website in file to block it
    
    print("website blocked")    #debug statement


def website_unblock():
    
    with open("C:/Windows/System32/drivers/etc/hosts","a+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(website in line for website in websites_to_block):
                file.write(line)
        file.truncate()
    print("website unblocked")  #debug statement

FO_mode = False

def check():
    if FO_mode:
        website_block()
    elif FO_mode == False:
        website_unblock()

def main(mins):
    global FO_mode

    s = mins*60
    website_block()

    while s!=0:
        print(s)
        s = s-1
        time.sleep(1)

    website_unblock()

if __name__ == "__main__":
    print("you executed Focus_mode.py")
else:
    print("you imported this file from somewhere else")