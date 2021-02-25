from email_sender import SendEmail as SE

with open('contacts.txt') as contacts:
    # reads the text file below, make sure all names and emails are one line and no new lines(\n).
    contact = contacts.readline()
    l1 = contact.split(',')
    # takes string of contacts/emails and splits on ',' to be separated into two lists
    names = []
    emails = []
    for i in l1:
        if '@' in i:
            emails.append(i)
        else:
            names.append(i)
    
    for n in names:
        i = names.index(n)
        SE(emails[i], names[i])
print("All emails have been sent...")