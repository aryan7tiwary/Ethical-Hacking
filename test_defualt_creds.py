# This Python script is to detect any default or weak credential in SSH and Telnet using Brute-force

# paramiko is a module for working with SSH
import paramiko
import telnetlib


# function for brute forcing SSH login
def SSHLogin(host,port,username,password):
    try: 
        ssh = paramiko.SSHClient()

        # as we don't have host key we are setting flag to missing
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # trying to connect SSH using username and password
        ssh.connect(host,port=port,username=username,password=password)
        ssh_session = ssh.get_transport().open_session()

        # if there is an active SSH session then we have logged in. Active SSH session can be viewed using ssh_session.active function
        if ssh_session.active:
            print("Login successful on %s:%s with username %s and password %s" % (host,port,username,password))
    except:
            print("Login failed %s %s" % (username,password))
    ssh.close()


# function for brute forcing Telnet login
def TelnetLogin(host,port,username,password):
    h = "http://"+host+":"+port+"/"
    tn = telnetlib.Telnet(h)

    # find login and input "username" in it
    tn.read_until("login: ")
    tn.write(username + "\n")

    # find password field and input "password"
    tn.read_until("Password: ")
    tn.write(password + "\n")

    try: 
        result = tn.expect(["Last login"])

        # if a login was successful there should be at least one entry in result
        if (result[0] >= 0):
            print("Telnet login successful on %s:%s with username %s and password %s" % (host,port,username,password))
        tn.close()
    except EOFError:
        print("Login failed %s %s" % (username,password))

host = "127.0.0.1"
port = 2200
with open("defaults.txt","r") as f:
    for line in f:
        vals = line.split()
        username = vals[0].strip()
        password = vals[1].strip()
        SSHLogin(host,port,username,password)
        TelnetLogin(host,port,username,password)
        