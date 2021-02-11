
link = input('Paste your link: ')
n = int(input('How  many links?:'))
firspart = link[:56]
lastpart = link[62:]


def changer():
    if len(link) > 0:
        try:
            code = int(link[57:63])
        except ValueError:
            code = int(link[56:62])

        newcode = code + 1
        newlink = firspart + str(newcode) + lastpart
        return newlink
    else:
        print('fckit, try again')

for i in range(n):      
    link = changer()
    print(link)

input("Press 'ENTER' to exit")