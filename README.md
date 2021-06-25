<a source="https://user-images.githubusercontent.com/35099243/123341302-6bf42c00-d556-11eb-8d2e-67dcb030361b.png" href=""></a>

PDF GENERATOR
CLI app that reads the contents of a simple SQLite school database and convert the whole database to a single PDF document. Prompt the user for an email address to send the PDF to. The email should be a proper one with the header, body, designation and PDF attachment.


Process:
1)	Should have a database.
2)	Should incorporate an email.
Database conversion:
1)	Have a database
2)	Connect database SQLITE using python
3)	Read data from a database
4)	Select table to print
5)	Convert database to pdf.
6)	Have a menu to send email



Email part :
1)	Set up the SMTP server and log into your account
2)	Create MIME
3)	Add sender, receiver address into the MIME
4)	Add the mail title into the MIME
5)	Attach the body into the MIME
6)	Open the file as binary mode, which is going to be attached with the email
7)	Read the byte stream and encode the attachment using base64 encoding scheme.
8)	Add header for the attachments.
9)	Start the SMTP session with valid port number with proper security features
10)	Login to the system
11)	Send mail and exit
# Boot_Camp_Project



ALGORITHM:
  1) Create a database
  2) connect database
  3) read the database
  4) Display menu: to select convert 1) all 
  5)                                 2) specific
  6) convert to pdf
  7) ask user if wants to send
  8) Prompt user to input email, header, body, designation and PDF attachment






