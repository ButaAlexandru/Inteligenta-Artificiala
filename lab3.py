from asyncio import to_thread
from hashlib import new
import smtplib
sender='nu_vreau_spam@coneasorin.ro'
subject='Pretul a scazut la:'
to_addr_list = ['coneasorin@outlook.com']
cc_addr_list = ['']
def sendemail(sender,message, subject,to_addr_list, cc_addr_list=[]):
    try:
        smtpserver='mail.x-it.ro:26'
        header = 'from: %s\n' % sender
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message

        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender, "stiinte216_2022")
        problems = server.sendmail(sender, to_addr_list, message)
        server.quit()
        return True
    except:
            print("Error: unable to send Email")
            return False
            