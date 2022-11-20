from audioop import ratecv


def computepay(hours, rate):
    print("In computepay", hours, rate)
    if hours > 40 :
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        xp = reg + otp
    else:
        pay = hours * rate
    print("Returning",pay)
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
# print(fh, fr)
computepay(fh,fr)

print("Pay:",xp)
