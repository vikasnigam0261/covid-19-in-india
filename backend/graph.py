import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib

ld = []
lh = []
lr = []
kerla = []
telangana = []
delhi = []
rajasthan = []
haryana = []
up = []
mp = []
andhra = []
arunachal = []
ladakh = []
jnk = []
punjab = []
mh = []
kt = []
od = []
wb = []
pd = []
ch = []
cg = []
tn = []
gj = []
ani = []
hp = []
bh = []
jh = []
ut = []
goa = []
asm = []
mgh = []
miz = []
mnp = []
tp = []
male = []
female = []


def itrs(l1, l2):
    l3 = [value for value in l1 if value in l2]
    return l3


with open('covid_d1.json', 'r') as myfile:
    dt = json.load(myfile)
    ds = dt['state']
    dr = dt['reportedOn']
    dp = dt['status']
    dg = dt['gender']
    for i in dp:
        if dp[i] == "Deceased":
            ld.append(i)
        elif dp[i] == "Hospitalized":
            lh.append(i)
        elif dp[i] == "Recovered":
            lr.append(i)
    for j in ds:
        if ds[j] == "Kerala":
            kerla.append(j)
        elif ds[j] == "Telangana":
            telangana.append(j)
        elif ds[j] == "Delhi":
            delhi.append(j)
        elif ds[j] == "Rajasthan":
            rajasthan.append(j)
        elif ds[j] == "Haryana":
            haryana.append(j)
        elif ds[j] == "Uttar Pradesh":
            up.append(j)
        elif ds[j] == "Madhya Pradesh":
            mp.append(j)
        elif ds[j] == "Arunachal Pradesh":
            arunachal.append(j)
        elif ds[j] == "Andhra Pradesh":
            andhra.append(j)
        elif ds[j] == "Ladakh":
            ladakh.append(j)
        elif ds[j] == "Jammu and Kashmir":
            jnk.append(j)
        elif ds[j] == "Punjab":
            punjab.append(j)
        elif ds[j] == "Maharashtra":
            mh.append(j)
        elif ds[j] == "Karnataka":
            kt.append(j)
        elif ds[j] == "Odisha":
            od.append(j)
        elif ds[j] == "West Bengal":
            wb.append(j)
        elif ds[j] == "Puducherry":
            pd.append(j)
        elif ds[j] == "Chhattisgarh":
            ch.append(j)
        elif ds[j] == "Chandigarh":
            cd.append(j)
        elif ds[j] == "Tamil Nadu":
            tn.append(j)
        elif ds[j] == "Gujarat":
            gj.append(j)
        elif ds[j] == "Himachal Pradesh":
            hp.append(j)
        elif ds[j] == "Andaman and Nicobar Islands":
            ani.append(j)
        elif ds[j] == "Bihar":
            bh.append(j)
        elif ds[j] == "Uttarakhand":
            ut.append(j)
        elif ds[j] == "Jharkhand":
            jh.append(j)
        elif ds[j] == "Manipur":
            mnp.append(j)
        elif ds[j] == "Mizoram":
            miz.append(j)
        elif ds[j] == "Goa":
            goa.append(j)
        elif ds[j] == "Assam":
            asm.append(j)
        elif ds[j] == "Tripura":
            tp.append(j)
        elif ds[j] == "Meghalaya":
            mgh.append(j)
    for k in dg:
        if dg[k] == "male":
            male.append(k)
        elif dg[k] == "female":
            female.append(k)

x1 = input("criterion 1")
x2 = input("criterion 2")
xy = itrs(x1,x2)
print(xy)
xx = []
for q in xy:
    xx.append(dr[q])

xx2 = []
for u in xx:
    if u not in xx2:
        xx2.append(u)

def countX(lst, x):
     count = 0
     for ele in lst:
        if (ele == x):
            count = count + 1
     return count

yb = []
for t in xx2:
    yb.append(count(xx, t))

path_to_pdf = input()

with PdfPages(path_to_pdf) as export_pdf:
    plt.plot(yb, xx2)
    export_pdf.savefig()
    plt.close()

destination = input()

password_path = input()

def send_email_pdf_figs(path_to_pdf, subject, message, destination, password_path):
    ## credits: http://linuxcursor.com/python-programming/06-how-to-send-pdf-ppt-attachment-with-html-body-in-python-script
    from socket import gethostname
    #import email
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    import json

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    with open(password_path) as f:
        config = json.load(f)
        server.login('me@gmail.com', config['password'])
        # Craft message (obj)
        msg = MIMEMultipart()

        message = f'{message}\nSend from Hostname: {gethostname()}'
        msg['Subject'] = subject
        msg['From'] = 'me@gmail.com'
        msg['To'] = destination
        # Insert the text to the msg going by e-mail
        msg.attach(MIMEText(message, "plain"))
        # Attach the pdf to the msg going by e-mail
        with open(path_to_pdf, "rb") as f:
            #attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
            attach = MIMEApplication(f.read(),_subtype="pdf")
        attach.add_header('Content-Disposition','attachment',filename=str(path_to_pdf))
        msg.attach(attach)
        # send msg
        server.send_message(msg)