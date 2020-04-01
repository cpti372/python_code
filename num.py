#문자열인지 판별
def isinteger(s):
    return s.isdigit() or s[0] == '-' and s[1:].isdigit()


#윤년인지 확인하는 함수
def istheyear(year):
    if year < 20:
        year += 2000
    else:
        year += 1900
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def isRRN(s):
    (front,mid,back)=s.partition("-")
    return front_ok(front) and mid =="-" and back_ok(s)

def front_ok(front):# 주민번호 앞 
    year,month,day=int(front[0:2]),int(front[2:4]),int(front[4:])
    if month='01' and '03' and 05 and 07 and 08 and 10 and 12:
        if day>0 and day<32:
            return True
    elif month==04 and 06 and 09 and 10 and 11:
        if day>0 and day<31:
            return True 
    elif istheyear(year)==True:
        if month==02 and 0<day and day<29:
            return True
        else:
            return False

    elif istheyear(year)==False:
        if month==02 and 0<day and day<30:
            return True
        else:
            return False

def back_ok(s):

