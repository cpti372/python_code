#파이썬 기초 문제 풀기 

#01
#문자열 포매팅 : 소수점 표현하기 
print("%0.2f"%3.141592)
#013 문자열 슬라이싱
mystring="hello world"
print(len(mystring))
#014 문자열 슬라이싱
license_plate="24가 2210"
print(license_plate[4:])

#015 문자열 분리
resolution2 = '1920x1080'
print('width:',resolution2[0:4])
print('height:',resolution2[5:])

#016 거꾸로 출력하기
#리스트만 reverse함수 사용 가능
outstr=" "
input = "PYTHON"
cont=len(input)
for i in range(0,cont):
    outstr=outstr+input[-(i+1)]
print(outstr)

#017 문자열 바인딩
s = "hello"
t = "python"
print(s+" "+t)

#021 리스트 연습
companies = ['NAVER', 'KAKAO', 'SK', 'SAMSUNG']
nstring=';'.join(companies)
print(nstring)
  
    

#022 문자열 나누기 
companies='000660;060310;0133340;095570;068400;006840'
com2=list(companies.split(';'))
print(com2)

#023 문자열 잘라내기- 양쪽 공백지우기 

code='         000660\n'
strip_code=code.strip()
print(strip_code)

#025파이썬 문자열 변경
lang = 'python'
print(lang.replace('p','P'))

#030문자열 자르기 
file=input("파일을입력하시")
print(file.split('.')[1:])

#031 문자열 갯수세기 
introduce = "python is widely used high-level language. python was conceived in the late 1980s"
print(introduce.count('python'))