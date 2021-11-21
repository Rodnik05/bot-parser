def replace(a):
    a = list(a)
    for i in range(len(a)):
        try:
            a.insert(a.index('\n'), ' ')
            a.remove('\n')
        except:
            break
    l = []
    i = 0
    while i < len(a):
        j = i + 1
        if a[i] != ' ':
            while a[j] != ' ':
                j = j + 1
            l.append(''.join(a[i:j]))
        i = j           
    a = l
    l = []
    i = 0
    j = -1
    while i < len(a):
        if a[i] == a[i].lower():
                l[j] = l[j] + ' ' + a[i]
                i = i + 1
        else:
            j = j + 1
            l.append(a[i])
            i = i + 1

    l2 = []
    for i in l:
        j = False
        for x in range(10):
            if str(x) in i:
                j = True
                break
        if j:
            l2.append(i)
    return l2

def parser(string):
    for i in range(len(string)):
        for j in range(10):
            if str(j) == string[i]:
                return string[:i], string[i:]
    
def make_dict(a):
    dict = {}
    for i in a:
        dict[parser(i)[0]] = parser(i)[1]
    return dict

def turn_into_date(string : str):
    if '...' in string:
        return(string.split('...'))
    else:
        return [string]
