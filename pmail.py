import base64

def setTo():
    return "Mail address"

def setFrom():
    return "Mail address"

def setSubject():
    return "subject"

def setTemp():
    return tempEncode("snap.jpg")

def tempEncode(filename):
    with open(filename,"rb") as f:
        origin = f.read()
        temp = base64.b64encode(origin)
    return temp

def setMail():
    with open("dmail","w") as f:
        f.write("To:"+setTo()+"\n")
        f.write("From:"+setFrom()+"\n")
        f.write("Subject:"+setSubject()+"\n\n")
        f.write(str(setTemp().decode()))