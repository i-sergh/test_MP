def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
#https://en.wikipedia.org/wiki/Digital_root
