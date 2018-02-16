import smtplib

sender = 'aakash.sinha@st.niituniversity.in'
receivers = ['utkarsh.srivastava@st.niituniversity.in']

message = """Subject: Ping
Hi! How are you!
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Mail delivered successfully"
   
except SMTPException:
   print "Error! unable to send email"
