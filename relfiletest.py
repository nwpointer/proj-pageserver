import os
dir = os.path.dirname(__file__)

#p = dir + "/index.html"
#p = p[1:]

f= open(os.path.join(os.path.dirname(__file__), 'index.html'));

print(f.read());

