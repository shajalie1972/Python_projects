
# Converting String to Integer
sval = '123'
ival = int(sval)
type(ival)
print(ival +1)

#Asking user to Input information

name = input(' Who are you ? ')
print('Welcome', name)

imp = input('Europe Floor ?')
usf = int(imp) + 1
print('us floor', usf)

# Conditional Statements
x= 21
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finish')

x = 5
print('Before 5')
if x == 5 :
    print(' Is 5')
    print(' Is still 5')
    print(' Third 5')
print(' Afterwards 5')
print(' Before 6')
if x ==6 :
    print(' Is 6')
print(' Afterwards 6')

# Multi-way Puzzle
if x< 2 :
    print('Below 2')
elif x >= 2 :
    print('Two or more')
else :
    print('Something else')

# Sample try / except
rawstr = input(' Enter a Number: ')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0 :
    print(' Nice Work ')
else:
    print(' Not a Number')

# Parameters
def greet (lang):
    if lang == 'es' :
        print(' Hola')
    elif lang == 'fz' :
        print('Bonjour')
    else:
        print('Hello')

print(greet('en'), 'Glean')

print(greet('es'), 'Sally')

print(greet('fz'),'Michael')

# LOOPS (REPEATED STEPS)

n = 10
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff! ')
print(n)

# BREAKING OUT OF A LOOP
#while True:
    #line = input('> ')
   # if line == 'done' :
     #   break
   # print(line)
  #  print('Done! ')

# A Definite Loop with Sring
friends = ['Joseph', 'Glean', ' Sally']
for friend in friends :
    print(' Happy new year ', friend)
print(' done! ')

for i in [5,4,3,2,1 ] :
    print(i)
print('done!')

# FINDING THE LARGEST VALUE
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num > largest_so_far :
        largset_so_far = the_num
    print(largset_so_far, the_num)
print('After', largest_so_far)

# Counting in a Loop

zork = 0
print(' Beforre', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print(' After', zork)

# Summing in a Loop
zork = 0
print(' Beforre', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print(' After', zork)

#FINDING THE AVERAGE IN A LOOP
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)

# Filtering in a Loop
print(' Before')
for value in [ 9, 41, 12, 3, 74, 15] :
    if value > 20 :
        print('large Number', value)
print('After')

# Search using a Boolen Variable
found = False
print(' Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
    print(' Found', value)
print('After', found)

# HOW TO FIND THE SMALLEST VALUE
smallest = None
print(' Before', smallest)
for value in [9, 43, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print(' After', smallest)

# Len Function
fruit = 'banana'
x = len(fruit)
print(' The Length is', x)

# Looping Through String
fruit = 'banana'
for letter in fruit :
    print(letter)

    index = 0
    while index < len(fruit) :
        letter = fruit[index]
        print(letter)
        index = index + 1

# Looping and Counting
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)

# Slicing Strings
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

#String Library

greet = ' Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

# Making everything Upper Case
greet = ' Hello Bob'
nnn = greet.upper()
print(nnn)

www= greet.lower()
print(www)

# Search and Replace
greet = ' Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)
nstr = greet.replace('o','x')
print(nstr)
 # Prefixes

line = 'Please have a nice day'
line.startswith('Please')
line.startswith('P')

# Parsing and Extracting

data = 'From stephen.marquard@uct.as.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print('The @ Sign is Position ', atpos)
sppos = data.find(' ',atpos)
print(atpos)

host = data[atpos+1 : sppos]
print(host)

# What is a Handle
fhand = open('mbox.txt', 'r')
print(fhand)

# The Newline Character
stuff = 'Hello\nWorld!'
print(stuff)

stuff = 'x\ny'
print(stuff)
len(stuff)

#Conunting Lines in a file
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
    print('Line Count:', count)

# Reading the Whole file
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))

# Displaying the first 20 characters of the file
print(inp[:20])

#Searching Through a File
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip() # get rid of extra line
    if line.startswith('From:') :
        print(line)

# Skipping With Continue
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip() # get rid of extra line
    if not line.startswith('From:') :
        continue
        print(line)
#Prompt for File Name
fname = input(' Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('subject: ') :
        count = count +1
print('There were', count, 'Subject lines in ', fname)

#Looking Inside Lists

friends = ['Joseph', 'Glean', 'Sally']
print(friends[1])

#List Can be sliced Using :
t= [9, 41, 12, 3, 74, 15]
print(t[:3])
print(t[:4])

#List Method
x = list()
type(x)
#<type 'list'>
dir(x)
['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#Building a List From scratch
stuff = list()
stuff.append('book')
stuff.append('99')
print(stuff)
stuff.append('cookies')
print(stuff)
stuff.append('Samson')
print(stuff)

#Built_in Functions and Lists
nums = [3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))

#print(sum(nums)/len(nums)))

#numlist= list()
#while True :
    #inp = input(' Enter a Number: ')
   # if inp == ' done' : break
    #value = float(inp)
    #numlist.append(value)
#average = sum(numlist) / len(numlist)
#print('average:', average)

#BEST FRIENDS: STRINGS AND LIST
abc = 'with three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
print(stuff)
for w in stuff :
    print(w)
#opening and deboging mbox-short.txt
han = open('mbox-short.txt')

for line in han:
    line = line.strip()
    wds = line.split()
    #Guardian a lit stronger
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])
#Dictionaries
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
# Many Counters With a Dictionary
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
# The Get Method for Dictionaries
counts = dict()
names = ['csev', 'cwen', 'zgian', 'cwen', 'csev', 'sam']
for name in names :
    counts[name] = counts.get(name, 0) +1
print(counts)

#Counting pattern
counts = dict()
print('Enter a line of text:' )
line = input('')
words = line.split()
print('Words:', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) +1
print('Counts', counts)

#Definite Loops and Dictionaries
counts = {'Chuck':1, 'Fred':42, 'Jan':100}
for key in counts:
    print(key, counts[key])

# Retrieving Lists of keys and Values
jjj = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

#Bonus: Two Iteration Variables!
jjj = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
for aaa,bbb in jjj.items() :
    print(aaa,bbb)

#Counting Words in a File
name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count
print(bigword, bigcount)



