"""
This is the solution to the problem of using sets to count the number
of individuals in the Internet Movie Database.  Each line of input is
split and stripped to get the name and this name is added to the set. 

One important note. In opening the file we need to specify the
encoding of the text. The default encoding used by open() is platform
dependent, so if you're on Windows with a Western Europe/North America,
you will be given the 8-bit Windows-1252 character set but this
only handles English characters well. Setting encoding to "utf-8"
overrides this. For the IMDB file, we need to
open with a more language-independent, international standard.  This
is a 'UTF-8' encoding of Unicode.

As we will use the time.time() function to measure how long our
computation takes.  This function tells the seconds since the "epoch",
which is 1/1/1970 on Unix-based systems (including Macs and Linux
machines) and 1/1/1601 on Windows machines.  By recording in the
software the time before the calculations start, the time when the
calculations end, and subtracting we get the elapsed time.
"""


import time

imdb_file = input("Enter the name of the IMDB file ==> ").strip()

start_time = time.time()

names = set()
for line in open(imdb_file, encoding="utf-8"):
    words = line.strip().split('|')
    name = words[0].strip()
    names.add(name)

end_time = time.time()

print("Solution took {:.2f} seconds".format(end_time-start_time))

print("Number of unique names in the IMDB:", len(names))

#######
##  The rest of this code was written to test the code and then
##  commented out.
#######
"""
ordered_names = sorted(names)
for i in range(min(len(ordered_names), 100)):
    print("{}: {}".format(i, ordered_names[i]))
"""

"""
for n in names:
    print('\t{}'.format(n))
"""
