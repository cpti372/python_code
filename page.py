def getTotalPage(m,n):
    if m%n==0:
        pages=m/n
        return pages
    else:
        pages=m/n+1
        return int(pages)


print(getTotalPage(15,10))