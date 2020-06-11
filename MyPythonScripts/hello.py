import re

def mystrip(mystr, char=None):
    if char == None:
        char = ' '
    # stripped = re.sub('{0}' + r'(\S*)' + '{0}'.format(char), r'\1', mystr)
    #stripped = re.sub(r'[{0}]+|[{0}]+$'.format(char), '', mystr)
    stripped = re.sub(r'\.*{0}$'.format(char), '', mystr)
    return stripped

        
        
    




mysong = 'You can call me Al - remaster'
print(mysong)
a = mystrip(mysong, 'er')
print(a)


