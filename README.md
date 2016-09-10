
Need more Pythia? here's one in python https://www.reddit.com/r/ProgrammerHumor/comments/4sv6qr/true_random_number_generator/

# PyPythia

High quality &amp; fast true random number generator

This is a high quality fast true random number generator. This means that PyPythia never ever repeats the same numbers again
regardless of how many tests you do. This also means that it never generates any numbers in a predictable order no matter 
how many times you refresh. PyPythia solves a great problem and is by far the best solution out there.

How to use:
```python
from pythia import PyPythia

pythia = new PyPythia();
```


##Pythia API:

.generate  -  Generate a new random number.
.reset     -  Reset and enable to restart and -probably- regenerate same numbers.


Enjoy!


Note: This is a joke, please do not use

Proof:


./pythia.py > test2.bin 

$ ent test2.bin

Entropy = 3.434982 bits per byte.

Optimum compression would reduce the size
of this 220000 byte file by 57 percent.

Chi square distribution for 220000 samples is 5048157.84, and randomly
would exceed this value 0.01 percent of the times.

Arithmetic mean value of data bytes is 50.5333 (127.5 = random).
Monte Carlo value for Pi is 4.000000000 (error 27.32 percent).
Serial correlation coefficient is -0.033698 (totally uncorrelated = 0.0).

