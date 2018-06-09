import smtplib
from notpublic.logindata import haslo,login
from email.mime.text import MIMEText

odbiorca=login
nadawca=login
haslo=haslo

temat="temat"
tresc="tresc"

mailer=smtplib.SMTP("smtp.gmail.com",587)

mailer.ehlo()
mailer.starttls()
mailer.login(login,haslo)
mailer.sendmail(nadawca,odbiorca,msg=tresc)

print("wyslano")

mailer.close()
