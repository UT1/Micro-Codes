import smtplib

sender = 'username@domain.com'
receivers = ['username@domain.com']

message = """Subject:Write the subject Here"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Mail sent successfully"
   
except SMTPException:
   print "Error! unable to send email"
