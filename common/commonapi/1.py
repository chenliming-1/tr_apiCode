from module import *
# import urllib
# from skimage import io
import os

if __name__ == '__main__':

    # url = "https://image01.cdn.klxuexi.com/resource/tr/item/20190219f1c3c0b15f4e40e98880d5d328d64af4/4ff02d81b8ace37411bc6b9f187d3c0c.jpg"
    # imagefile = urllib.request.urlopen(url)
    # imagefile = io.imread(url)
    # io.imshow(imagefile)
    # io.show()
    list1 = []
    if list1 is None:
        print("1")
    else:
        print("2")

    # print(os.path.expanduser('~'))

    # url = '//www.jb51.net/images/logo.gif'
    # file = urllib2.urlopen(url)
    # tmpIm = cStringIO.StringIO(file.read())
    # im = Image.open(tmpIm)
    # print (im.format, im.size, im.mode)

    # i=0
    # list = []
    # for i in range(0, 26):
    #     list.append(chr(65+i))
    # print(list)
    # random.shuffle(list)
    # print(list)
    # print('<abbr class=\\"ql-topic-student-answer\\"></abbr>')

    # a = [1, 2]
    # b = [2, 5, 9]
    # a[:] = b
    # print(a)

    a = "/tr/api/tr/paper-textbook/2020051562b2a26dd8b1444c926c3ea4f1d6d6c3"
    b = a.split('/')
    print(a)
    print(b)

    c = b.pop()
    print(b)


