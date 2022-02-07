#!/usr/bin/env python
# coding: utf-8

# In[107]:


#0 lamda and list comp methods for filtering even numbers in a list 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lambda_even_numbers = list(filter(lambda x: x%2 == 0, a))
list_comp_even = [x for x in a if x%2 == 0]
list_comp_even
lambda_even_numbers


# In[113]:


#1 lambda solution to under 5 and function using list comprehension 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
under_five = list(filter(lambda x: x<5, a))
def less_than_five(lst, n):
    new_list = [x for x in lst if x<n]
    return new_list
less_than_five(a, 5)
under_five


# In[129]:


#2 Quicksort vs Bubble sort vs Selection sort
arry = [1,3,2,5,6,4,5,5,7, 8]
#selection sort keeps looking for the smallest element from the elements that
#remain unsorted
def selectionsort(array):
   
    for step in range(10):
        min_index = step

        for i in range(step + 1, 10):
         
            if array[i] < array[min_index]:
                min_idx = i
        (array[step], array[min_index]) = (array[min_index], array[step])
    return array
#helper function for quick sort 
#partition works by putting alll smaller elements to the left of the pivot
#and all the larger elements to the right of the pivot 
#this partition takes the first element as the pivot 
def partition(array,start,end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low<= high and array[high] >= pivot:
            high -= 1
        while low<= high and array[low]<= pivot:
            low += 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start] = array[high]
    array[high] = array[start]
    return high 
#Quick sort picks an element as a pivot and partitions the array around the pivot point
#runs partition through the whole array
def quicksort(arr, low, high):
    #low is the starting index 
    #high is the ending index
    if high>= low:

        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)

#Bubble sort works by going element by element and ordering the array through a nested for loop
#most intuitive
def bubblesort(arr):
    n = len(arr)
    for i in range(len(arr)):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
quicksort(arry, 0, 9)
print(arry)         


# In[138]:


#3 (Search) Sequential search has worst case run time of O(n) while Binary search
#has worst case run time of O(logn)
arry = [1,3,4,5,6,3,4,5,5,7]
def binary_search(arr,l,r, ele):
    sorte = bubblesort(arr)
    mid = l + (r-l) // 2
    if sorte[mid] == ele:
        return mid
    elif sorte[mid] > ele:
        return binary_search(arr, l, mid-1, ele)
    elif arr[mid] < ele:
        return binary_search(arr,mid+1 , r, ele)
    else:
        return -1
binary_search(arry,0,9,1)

#sequential search is much more intuitive to code but takes the computer much longer than binary search
# returns all positions where the value is found in the array
def sequentialsearch(listy, value):
    pos = 0
    positions = []
    while pos < 10:
        if listy[pos] == value:
            positions.append(pos)
            pos+=1
        else:
            pos = pos+1

    return positions

sequentialsearch(arry, 7)


# In[4]:


#4 iterating through txt file
def txt_counter(file):
    number_lines = 0
    number_words = 0
    number_chars = 0 
    with open(file, 'r') as f:
        for line in f:
            number_lines+=1
            word = 'Yes'
            for letter in line:
                if(letter!= ' ' and word =='Yes'):
                    number_words += 1
                    word = 'No'
                elif (letter == ' '):
                    word = 'Yes'
                for char in letter:
                    # \n means newline
                    if(char !=" " and char != '\n'):
                        number_chars += 1
    print(number_lines)
    print(number_words)
    print(number_chars)
txt_counter('/Users/strippperton/desktop/scratchpad.txt')


# In[9]:


#5 copy image to another file
#copies image in file 1 to file 2
def copier(file1, file2):
    file_2 = open('file2', 'wb')
    with open('file1', 'rb') as file_1:
        while True:
            byte = file_1.read(1)
            if not byte:
                break
            file_2.write(byte[0])


# In[311]:


#6 display all strings in txt file
def displayer(file):
    with open(file, 'r') as open_file:
        for line in open_file:
            for word in line:
                print(word)
(displayer('/Users/strippperton/desktop/scratchpad.txt'))


# In[310]:


#7 create employee class
#searialized?
class Employee:
    def _init_(self, ID, name, email):
        self.ID = ID
        self.name = name
        self.email = email
        


# In[17]:


#8 write lambda function to return the square of input
squared = (lambda x:x**2)
squared(2)


# In[25]:


#9 filter even numbers 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
is_even_function = (lambda x: x%2==0)
list(filter(is_even_function, a))


# In[30]:


#10 square each value in a list
enter_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
square_the_list = print(list(map((lambda x: x**2), enter_list)))


# In[35]:


#11 multiply numbers of two given list using lambda 
multiplied_lists = [a[i] * enter_list[i] for i in range(len(a))]
multiplied_lists


# In[140]:


#12 multiply elements of a list together with lambda and reduce func
import functools
lambda_multiplied = print(functools.reduce(lambda a,b: a*b,arry))


# In[141]:


#13 calculate factorial through a function decorator
def factorial_decorator(val):
    value = 0
    for i in range(1, val-1):
        value += (i * i+1)
    return value
factorial_decorator(6)


# In[57]:


#14 finding common elements in two list
a_list = [1,2,4,5,3,4]
b_list = [1,5,7,8,3,4]
def in_common(list1, list2):
    common = []
    for i in list1:
        if i in list2:
            common.append(i)
    return common
in_common(a_list, b_list)


# In[59]:


#15 add elements of one list to another list through list comp
#doesn't work if they are varrying lengths
summed = [a_list[i] + b_list[i] for i in range(len(a_list))]
summed


# In[69]:


#16 looking for 3 char strings starting with m
import re
Input= 'man sun mat run something'
def mem(long_string):
    splitted = long_string.split()
    worthy = []
    for i in splitted:
        if len(i) == 3 and re.findall('^m', i):
            worthy.append(i)
    return worthy 

mem(Input)


# In[87]:


#17 splitting strings with nonalpha numerics 
#this also splits on spaces which is a nonaplha numeric
Input = 'This is the: “core” python\s assignment'
def splitty(string):
    return re.split('\W', string)
splitty(Input)
    


# In[94]:


#18 return only words starting with a 
Input = 'an apple a day keeps the doctor Away'
def aye(string):
    splitted = re.split(' ', string)
    ayes = []
    for i in splitted:
        if re.findall('^a', i) or re.findall('^A', i):
            ayes.append(i)
    return ayes
aye(Input)


# In[97]:


#19 returns words with start of numbers
Input= 'the meeting will be conducted on 1st and 21st of every month'
def num(string):
    splitted = re.split(' ', string)
    num_starters = []
    for i in splitted:
        if re.findall('^[1-9]', i):
            num_starters.append(i)
    return num_starters
num('the meeting will be conducted on 1st and 21st of every month')


# In[102]:


#20 return words with 5 chars
Input= 'one two three four five six seven 8 9 10'
def fiver(string):
    splitted = re.split(' ', string)
    fivers = []
    for i in splitted:
        if re.findall('^\w{5}$', i):
            fivers.append(i)
    return fivers
fiver(Input)


# In[104]:


#21 Looking for dates
Input= 'Vijay 20 1-5-201, Rohit 21 22-10-1990, Sita 22 15-09-2000'
def dater(string):
    splitted = re.split(' ', string )
    daters = []
    for i in splitted:
        if re.findall('\d{2}-\d{2}-\d{4}', i):
            daters.append(i)
    return daters
dater(Input)


# In[217]:


#22Looking for email IDS from a text file 
def email_in_txt(file):
    emails = []
    with open(file, 'r') as open_file:
        for line in open_file:
            if re.findall("([a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z0-9]+)", line):
                emails.append(line)
    return emails
email_in_txt('/Users/strippperton/desktop/email.txt')


# In[214]:


#23 retrieve information from HTML file
def html_info(html):
    info = []
    splitted = html.split('>')
    for i in splitted:
        if re.match('^[A-Z,5-9]',i):
            i = i.replace('</td', '')
            info.append(i)
        
    return info
html_info('''<html> 

             <table border=2> 

            <tr align=’center’><td>1</td> <td>Roti</td> <td>50</td></tr> 

            <tr align=’center’><td>2</td> <td>Dosa</td> <td>55.75</td></tr> 

            </table> 

        </html>''')        


# In[171]:


#24 find IP address of a website
import socket 
def get_ip(website):
    return socket.gethostbyname(website)
get_ip('www.google.co.in')


# In[313]:


#25 write program to read webpage source code
from urllib.request import urlopen
def source_code(html):
    opened = urlopen(html)
    source_coder = opened.read()
    #too long to show the whole thing
    return source_coder[:100]
source_code('https://docs.google.com/document/d/1eDLw7dw4Wcc-DvsBxAdwQY7YFX-NQhCVRzc_UI8uCZo/edit')


# In[294]:


#26 download a web page from the internet
def downloader(webpage):
    url = 'http://google.com/'
    r = requests.get(url, 'html.parser')
    with open(webpage,'w') as webpage:
        webpage.write(r.text)
        webpage.close()
        return webpage
downloader('/Users/strippperton/desktop/email.txt')


# In[ ]:


#27 create a TCP/IP server that sends messages to client
# take the server name and port name
#keeps timing out 
#TCP/IP stands for Transmission Control Protocol/Internet Protocal it is used 
#to interconnect devices
#Needed help from external sources for this question
host = 'local host'
port = 132
# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM) 
# bind the socket with server
# and port number
s.bind(('', port))
# allow maximum 1 connection to
# the socket
s.listen(1)
#
# display client address
print("connection from:", str(addr))
# send message to the client after
# encoding into binary string
c.send(b"testing message function")
msg = "gg"
c.send(msg.encode())
# disconnect the server
c.close()


# In[300]:


#28 write program that recives a file name and sneds the contents to the file
#
s = socket.socket()
port = 4999
s.bind(('', port))
s.listen(10)


# In[243]:


#29 Student class
class Student_details:
    def __init__(self, roll, name, address, email):
        self.roll = roll
        self.name = name
        self.address = address
        self.email = email
    def get_roll(self):
        print(self.name + ' roll is ' + self.roll)
    def get_name(self):
        print('''Student's name is ''' + self.name)
    def get_address(self):
        print(self.name + ' adress is ' + self.address)
    def get_email(self):
        print(self.name + ' email is ' + self.email)
steve = Student_details('32', 'steve', '4323 steve st', 'steve@gmail.com')
steve.get_email()
steve.get_roll()
steve.get_name()
steve.get_address()


# In[303]:


#30 employee class
#variables must be private using __
#accessor and mutator
#auto generated ID
class Employee:
    __id = 1
    
    def __init__(self):
        self.__id = Employee.__id
        self.name = None
        self.department = None
        self.age = None
        self.email = None
        Employee.__id += 1
    def setEmployee(self, name, department, age, email):
        self.__name = ('Employee name:' + name)
        self.__department = (name + ' department is ' + department)
        self.__age = (name + ' age is: ' + age)
        self.__email = (name + ' email is: ' + email)
    def get_name(self):
        print(self.__name)
    def get_id(self):
        print(self.__id)
    def get_department(self):
        print(self.__department)
    def get_email(self):
        print(self.__email)
    def get_age(self):
        print(self.__age)
    def set_id(self, __id):
        self.__id = __id
jhon = Employee() 
jhon.setEmployee('jhon', 'ERS', '55', 'jhon@yahoo.com')
rick = Employee()
rick.setEmployee('rick', 'aws', '44', 'rick@gmail.com')
jhon.get_email()
jhon.get_id()
rick.get_email()
jhon.get_id()


# In[273]:


#31 Circle Class 
#radius and color as private instance variables
#two overloaded constructors 
#two public methods getRadius() and getArea()
#TestCircle.java
from math import pi
class Circle:
    def __init__(self, radius, color):
        #privite variables
        self.__radius = radius
        self.__color = color
    def getRadius(self):
        print(self.__radius)
    def getArea(self):
        print(pi * (self.__radius **2))
circle_1 = Circle(3, 'black')
circle_1.getArea()
circle_1.getRadius()


# In[286]:


#32 stack it
#pop and push
class MyIntStack:
    def __init__(self):
        self.items = []
    def pop(self):
        self.items = self.items[:-1]
    def push(self, item):
        self.items.append(item)
stack = MyIntStack()
stack.push(1)
stack.push(4)
stack.push(3)
stack.pop()
print(stack.items)


# In[ ]:




