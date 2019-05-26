import bcrypt


def encrypt(pw):
    return bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()


def check_pw(pw, hashed):
    return bcrypt.checkpw(pw.encode(), hashed.encode())