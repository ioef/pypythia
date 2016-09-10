#!/usr/bin/env python 

import random

class PyPythia():
    def __init__(self):
        self.results = []

    def generate(self):
        present = True
        while present:
            mynum = int(random.random()*9007199254740992)
            
            while len(str(mynum)) < 21:
                mynum = int(random.random()*900632457199254740992)
 
            if mynum not in self.results:
                present = False
            self.results.append(mynum)

        return mynum

    def reset(self):
        self.results = []
        
        
p = PyPythia()

for i in range(0,10000):
    print (p.generate())

