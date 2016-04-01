y = [x for x in range(8)]
print y

y = [x*x for x in range(8)]
print y

y = [ (x, x*x, x*x*x) for x in range(8) ]
print y

p="myNoobPass1234"
print p

y = [x for x in p]
print y

y = [x for x in "1234"]
print y

UC_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print UC_LETTERS

y = [ x for x in p if x in UC_LETTERS ]
print y

y = [ 1 for x in p if x in UC_LETTERS ]
print y

y = [ 1 if x in UC_LETTERS else 0 for x in p ]
print y

NUMS = "0123456789"
LC_LETTERS = "abcdefghijklmnopqrstuvwxyz"

##print [ 1 if x in UC_LETTERS elif 2 for x in LC_LETTERS else 0 for x in p]

def pass_check(pw):
    return 0 in [0 if x in UC_LETTERS else 1 if x in NUMS else 2 if x in LC_LETTERS for x in pw]

pass = "000000"
print pass_check(pass)