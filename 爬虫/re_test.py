import re
pattern = re.compile(ur'";window.gtk = ('.*?');"')
str = u''
print(pattern.search(str))