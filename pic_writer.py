#file that makes the parse-able file
#all files created are converted into a GIF
def numConv(num):
    new = str(num)
    if len(new) == 1:
        return '00' + new
    if len(new) == 2:
        return '0' + new
    if len(new) == 3:
        return new

f = open('pic.txt', 'w')
f.write('line\n500 0 -10000 0 0 -10000\nline\n0 0 -10000 0 250 -10000\nline\n0 250 -10000 0 250 10000\nline\n500 250 -10000 500 250 10000\nline\n500 0 -10000 500 0 10000\n')
a = -10000
while a < 10000:
    f.write('line\n0 250 {} 500 250 {}\nline\n500 250 {} 500 0 {}\n'.format(a,a,a,a))
    a += 100
fNum = 1
tmp = fNum
while fNum < tmp + 25:
    f.write('save\nimage{}.png\n'.format(numConv(fNum)))
    fNum += 1
tmp = fNum
while fNum < tmp + 20:
    f.write('ident\nrotate\nx 1\nrotate\ny -1\napply\nsave\nimage{}.png\n'.format(numConv(fNum)))
    fNum += 1
tmp = fNum
while fNum < tmp + 55:
    f.write('ident\nmove\n-5 -5 0\napply\nsave\nimage{}.png\n'.format(numConv(fNum)))
    fNum += 1
f.write('display\n')
f.close()
