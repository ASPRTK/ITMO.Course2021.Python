"""
Here is an alternative list based solution - not covered in lecture -
where each name is added to the list without any checking for
duplicates. The list is then sorted and the number of distinct
individual is counted by scanning through the list and looking for
adjacent pairs of names that are different.

You will see that this solution is almost as fast as the set-based
solution, but the set-based solution is simpler and more natural to
write.

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

# Add all the names to the list
name_list = []
for line in open(imdb_file, encoding="utf-8"):
    words = line.strip().split('|')
    name = words[0].strip()
    name_list.append(name)

# Sort the names.  After this all repeated names will be next to each
# other in the list.
name_list.sort()

# Count the distinct names by counting the number of adjacent pairs of
# names that are different.
count = 1
for i in range(1,len(name_list)):
    if name_list[i-1] != name_list[i]:
        count += 1

end_time = time.time()
print('Total time required {:2f} seconds'.format(end_time-start_time))
print("Number of unique names in the IMDB:", count)
