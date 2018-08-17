import urllib.request

url="https://movie.naver.com/movie/bi/mi/basic.nhn?code=153687"
text="&page="
review=""
for num in range(1,20):
    full_url=url+text+str(num)
    full_html=urllib.request(full_url)
    full_contents=str(full_html.read().decode("153687"))
    review=re.findall(r"\<br\>.+",full_contents)
for result in review:
    print(result)