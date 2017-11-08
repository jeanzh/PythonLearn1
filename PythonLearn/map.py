

def format_name(s):
    s1=s[0:1].upper()+s[1:].lower();
    return s1;
def mapname():
    print(list(map(format_name, ['adam', 'LISA', 'barT'])))
