import socket
import smtplib
from smtplib import *
import sys
import optparse

def connect(IP,Port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, Port))
        socket.setdefaulttimeout(3)
        ans = s.recv(1024)
        if ("220" in ans):
            print "\n[+]Port" + " " + str(Port) + " " + "open on the target system\n"
        else:
            print "\n[+]Port" + " " + str(Port) + " " + "open on the target system\n"
            sys.exit(0)
    except Exception as e:
        print e

def check_open_relay_attack(IP,Port):


        attacker_mail=raw_input("***Enter the Attacker Mail address ********\n")
        victim_mail = raw_input("***Enter the Victim Mail address ********\n")
        try:
            smtpserver = smtplib.SMTP(IP, Port)

            r = smtpserver.docmd("Mail From:", attacker_mail)
            a = str(r)
            if ("250" in a):
                r = smtpserver.docmd("RCPT TO:", victim_mail)
                a = str(r)
                if ("250" in a):
                    smtpserver.sendmail(attacker_mail,victim_mail,"This is a open Relay test message" )
                    print "[+]The target system seems vulenarble to Open relay attack\n"

                else:
                    print "[-]The target system is not vulnerable to Open relay attack "

                helo_res = smtpserver.helo(IP)
                print "::::::::::::::::HELO RESULT:::::::::::::::"
                for i in helo_res:
                    print i
                print "::::::::::::::::HELO END:::::::::::::::"

            else:
                print "[-]Port is closed/Filtered"
        except Exception as e:
            print e

def main():
    try:
        parser = optparse.OptionParser("usage %prog -H <target host IP address> -p <target port>")
        parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
        parser.add_option('-p', dest='tgtPort', type='string', help='specify target port ')
        (options, args) = parser.parse_args()
        tgtHost = options.tgtHost
        tgtPorts = options.tgtPort
        print tgtHost
        print tgtPorts
        if (tgtHost == '') | (tgtPorts[0] == ''):
            print '[-] You must specify a target host and port.'

        connect(tgtHost,int(tgtPorts))
        check_open_relay_attack(tgtHost,int(tgtPorts))
    except Exception as e:
        print '[-] You must specify a  -H <target host IP address> -p <target port>.'


if __name__ == '__main__':
    main()
