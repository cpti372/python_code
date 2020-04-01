def find_first(filename,key):
    infile=open("input.txt","r")
    outfile=open("result.txt","w")
    text=infile.read()
    pos=text.find(key)
    if pos==-1:
        outfile.write("none")
    else:
        outfile.wrtie
