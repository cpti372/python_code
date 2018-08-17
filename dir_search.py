#하위 디렉터리 검색하기
import os
def search(dirname):
   filenames=os.listdir(dirname)#해당 디렉터리에 있는 파일들의 리스트 
   for filename in filenames:
    full_filename=os.path.join(dirname,filename)#디렉터리랑 파일명 둘다 함께 조인해줌
    print(full_filename)

search("/desktop")

