#GMAILMARKREAD.py
#Author: Aishwarya Rameshkumar 
#Script to mark desired emails (in a given range of dates) as read so user does 
#not have to manually go through and mark each email as read
#CAUTION: Once the script is run and emails are marked as read, this change cannot 
#automatically be undone. If desired, the user must manually mark chosen
#emails as unread. 

#TODO: Will add more comments/imrpove style in next update(s)...

import imaplib, pprint

print "Hello I'm running"

#if not using gmail, change to appropriate host/port
M = imaplib.IMAP4_SSL("imap.gmail.com", port = 993)

#correct username and password must be substituted prior to running script
M.login("username", "password")
M.list()

#search only inbox by default
M.select("inbox") 

#Search command - specify desired email range here
typ, data = M.search(None, '(SENTBEFORE 01-Jun-2016)') 

print "Size of data is", len(data)
for num in data[0].split():
   M.store(num, '+FLAGS', '\\Seen')
M.close()
M.logout()
