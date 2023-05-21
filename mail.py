import smtplib

server=smtplib.SMTP('smtp@gmail.com',587)
server.starttls()

server.login ('brindhagopenath@gmail.com','ReshuBindhu01*')
server.sendmail('brindhagopenath@gmail.com','reshmigopenath@gmail.com','mail sent from py')

print('Mail sent')
