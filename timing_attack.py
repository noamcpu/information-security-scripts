import time
import sys

"""
 The function check_password(password) is used by a safe with 4-digits passwords,
  and is susceptible to timing attacks. More specifically, it takes it around 0.1 seconds to check one digit –
   so brute-forcing all the possible combinations will take more than an hour.
   This code can to crack its password in less than a minute.
"""

begin = time.time()


def check_password(password):
    real_password = sys.argv[1]
    if len(password) != len(real_password):
        print(" Access denied ")
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1)  # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            end = time.time()
            return False, end - begin
    return True, x


p = "0000"
i = 0


def crack_password():
    chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if i == 0:
        valid, t = check_password(p)
    if not valid:
        if 0.1 < t < 0.2:
            while not valid:
                for k in chars:
                    valid, t = check_password(k.zfill(4))
                    ++i
                    crack_password()
        if 0.2 < t < 0.3:
            while not valid:
                for k in chars:
                    valid, t = check_password(k.zfill(4))
                    ++i
                    crack_password()
        if 0.3 < t < 0.4:
            while not valid:
                for k in chars:
                    valid, t = check_password(k.zfill(4))
                    ++i
                    crack_password()
        if t > 0.4:
            while not valid:
                for k in chars:
                    valid, t = check_password(k.zfill(4))
                    ++i
                    crack_password()
    if valid:
        return print(t)


# return cracked password


crack_password()
