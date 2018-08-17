#단순한 메모 입력 후 메모장 생성
#그 후에 탭을 공백으로 바꾸
import sys
src=sys.argv[1]
dst=sys.argv[2]
f=open(src)
tab_content=f.read()
f.close()
space_content=tab_content.replace("\t",""*4)
f=open(dst,"w")
f.write(space_content)
f.close()