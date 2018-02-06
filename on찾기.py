import re
a='Raindrops# on Roses*, and Whiskers! on Kittens.'
r=re.compile(r"\b\w*")
print(r.findall(a))
