import getpass
from netmiko import ConnectHandler
import smtplib
from email.mime.text import MIMEText

uname = raw_input("Enter your username: ")
pswd = getpass.getpass(prompt="Enter your Password: ")
result = []
test

def sendemail(mes):
    fromaddr = "TCAMStatus@abc.com"
    toaddr = ['Network@abc.com']
    message = MIMEText(mes)
    message['From'] = fromaddr
    message['To'] = ','.join(toaddr)
    message['Subject'] = "TCAM Status RTRs"
    server = smtplib.SMTP('appmail.data.ie.abc.net:25')
    server.ehlo()
    server.sendmail(fromaddr,toaddr,message.as_string())
    server.quit()

def tcam_status():
    iae_device_list = ['router1', 'router2']

    for k in iae_device_list:
        connection = ConnectHandler(ip=k, device_type='cisco_ios', username=uname, password=pswd)
        output = connection.send_command('sh pl re')
        output = output.split('State')
        output.pop(0)
        output.pop(0)
        o = ''.join(output)
        o = o.split()
        o.pop(0)
        tc = o[36]
        tc = tc.split("(")
        tc = tc[1]
        tcam = tc.split(")")
        tcam = tcam[0]
        tcam_result = 'TCAM for ' + str(k) + ' = ' + str(tcam)
        # print(tcam_result)
        result.append(tcam_result)

tcam_status()
message = '\n'.join(result)
sendemail(message)