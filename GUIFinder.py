import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib.ticker import NullFormatter
from matplotlib.patches import Rectangle
from tkinter import *
from tkinter import ttk

number = [] #player id's
first = [] #player first name
last = [] #player last name
pitcher_atbats = [] 
i = int(0) #counter
a = int(0) #counter
k = []
count= 0
x = [] #pitch x value
y = [] #pitch y value
pitch= [] #pitch type
sz_bot = float(0) #used to configure strike zone bottom
sz_top = float(0) #used to configure strike zone top
bot = float(0) #bottom hiegh of strike zone
top = float(0) #top height of strike zone
first_last = []
name = []
z = int(0) #counter
dtdy = []
j = []
pitcher_ID =[]
checker = int(0)
d = int(0)
pitcher_first = []
pitcher_last = []
j = []
junk = int(0)
rem = int(0)
v = []
situation = []
s = []
ball = []

master = Tk()                                       #starts tkinter gui


with open('player_names.csv','r') as csvfile:       #open csv files to get player ids and numbers
    plots = csv.reader(csvfile, delimiter=',')
    next (plots)                                    
    for row in plots:
        number.append((row[0]))                     #append player number to list
        first.append(row[1])                        #append player first name to list
        last.append(row[2])                         #append player last name to list
                                                    #we have to have the names and ids all in the same index so we can find the player later on in the program, we switch between 3 CSV files here

with open('atbats.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')      #this will only get the pitcher IDs so we don't have a postion player in our drop downlist
    next (plots)

    for row in plots:
        #if a > k :
        checker = (row[8])
        if checker in pitcher_ID:
            checker = checker
            #move along
        else:
            pitcher_ID.append(row[8])
            junk +=1

    with open('player_names.csv','r') as csvfile: #this takes the pticher ID's and finds the pitcher's first and last name
        plots = csv.reader(csvfile, delimiter=',')
        next (plots)
        for row in plots:
            if d != junk:
                if pitcher_ID[d] == row[0]:
                    pitcher_first.append(row[1])
                    pitcher_last.append(row[2])
                    d += 1


for x in pitcher_first:
    dtdy.append(pitcher_first[i] + ' ' + pitcher_last[i])   
    i += 1
#print(dtdy[200])
k =(list(zip(pitcher_first, pitcher_last))) #takes pticher_first and pitcher_last and makes it one list
k.sort()                                    #orders the names alaphabetically
#print(k)

w = ttk.Combobox(master, values = k, text = "pitcher") #first drop down using our list 'k'
w.pack()
j = ['--Select Pitch Type--','ALL']         #initializes the pitch type list, allows us to sort by ALL pitches
                                                
def pltcolor(lst):                          #defines the function 'pltcolor' so the pitchers can be color coded
    cols=[]
    for l in lst:
        if l=='FF':
            cols.append('red')
        elif l =='FT':
            cols.append('black')
        elif l=='CH':
            cols.append('blue')
        elif l=='CU':
            cols.append('yellow')
        elif l=='FC':
            cols.append('orange')
        elif l=='SL':
            cols.append('purple')
        elif l=='SI':
            cols.append('lightgray')
        else:
            cols.append('green')
    return cols

def graph(x,y, pitch):                      #defines the function for graphing, makes code more efficent
    cols=pltcolor(pitch)

    nullfmt = NullFormatter()               # no labels

    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]

    # start with a rectangular Figure
    plt.figure(1, figsize=(8, 8))

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)

    # no labels
    axHistx.xaxis.set_major_formatter(nullfmt)
    axHisty.yaxis.set_major_formatter(nullfmt)

    # the scatter plot:
    axScatter.scatter(x, y, c = cols)

    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    axScatter.set_xlim((-lim, lim))
    axScatter.set_ylim((-1, lim))

    bins = np.arange(-lim, lim + binwidth, binwidth)
    axHistx.hist(x, bins=bins)
    axHisty.hist(y, bins=bins, orientation='horizontal')

    axHistx.set_xlim(axScatter.get_xlim())
    axHisty.set_ylim(axScatter.get_ylim())

    someX = 0
    someY = 3.4632659
    axScatter.add_patch(Rectangle((someX - .7083 , someY - 1.8832 ), 1.467, 1.8832, fill=None, alpha=1))
    plt.show()

def select ():                      # once pitcher drop down is selcetd, user will hit the "Select" button to be able to sort by ptich type, strike and ball count 
    global b
    global rem
    global v
    global s
    global ball
    a = w.get()
    z = int(0)
    index = int(0)
    for x in dtdy:
        if a == dtdy[z]:
            #print(number[z])
            #print(z)
            index = z
            ID = number[z]
            z += 1
        else:
            z += 1
    print(ID, index)
    with open('atbats.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next (plots)

        for row in plots:
            if  number[index] == row[8]:
                pitcher_atbats.append(row[0])

    with open('pitches.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next (plots)
        for row in plots:
            if row[0] in pitcher_atbats:
                pitches = row[19]
                if pitches in j:
                    pitches = pitches                                               #we only want a pitch which isn't already in the list
                else:
                    if pitches == '' or pitches == 'PO' or pitches == 'IN':         #we don't want to list these in pitch types, they aren't important
                        pitches = pitches
                    else:
                        j.append(row[19])
                        print (j)
    v = ttk.Combobox(master, values = j, text = "pitch type")                               #create pitch type drop down
    v.current(0)
    v.pack()

    ball=ttk.Combobox(master, values = ['--select balls--','any',0,1,2,3], text = "balls")  #create balls drop down
    ball.current(0)
    ball.pack()
    
    s = ttk.Combobox(master, values = ['--select strikes--','any',0,1,2], text = "strikes") #create strike drop down
    s.current(0)
    s.pack()

    

    button = Button(master, text="OK", command=ok)                  #calls the function ok when "OK" is clicked, this will graph everything
    button.pack()

button = Button(master, text="Select", command= select)             #defines the button will run the 'select' function
button.pack()



def ok ():
    global v
    global s
    global ball
    z = int(0)
    global a
    global b
    global dtdy
    a = w.get()
    b = v.get()
    c = s.get()
    other = ball.get()
    print(a)
    print ("Pitcher is:" + w.get())
    print ("Pitches: " + b)
    for x in dtdy:
        if b != 'ALL' and c != 'any' and other != 'any':
            if a == dtdy[z]:
                print(number[z])
                print(z)
                ID = number[z]
                with open('atbats.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)

                    for row in plots:
                        if  number[z] == row[8]:
                            pitcher_atbats.append(row[0])


                with open('pitches.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)
                    x = []
                    y = []
                    pitch= []
                    h = int(0)
                    for row in plots:
                        if h == 300000000:
                            break
                        else:
                            if row[0] in pitcher_atbats and row [19] == b and row[5] == other and row[22] == c:
                                    x.append(float(row[20]))
                                    y.append(float(row[21]))
                                    pitch.append(row[19])
                                    #sz_bot = (float(row[26]))
                                    #sz_top = (float(row[27]))
                                    #print(sz_bot)
                                    #bot = bot + sz_bot
                                    #top = top + sz_top
                                    #print(bot)
                                    #if pitcher_atbats[a] == row[0]:
                                    h +=1
                graph(x,y, pitch)
            else:
                z += 1
        elif b == 'ALL' and c != 'any' and other != 'any':
            if a == dtdy[z]:
                #print(number[z])
                ID = number[z]
                with open('atbats.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)

                    for row in plots:
                        #if a > k :
                        if  number[z] == row[8]:
                            pitcher_atbats.append(row[0])


                with open('pitches.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)
                    x = []
                    y = []
                    pitch= []
                    h = int(0)
                    for row in plots:
                        if h == 3000:
                            break
                        else:
                            if row[0] in pitcher_atbats and row[4] == other and row[22] == c:

                                    x.append(float(row[20]))
                                    y.append(float(row[21]))
                                    pitch.append(row[19])
                                    #sz_bot = (float(row[26]))
                                    #sz_top = (float(row[27]))
                                    #print(sz_bot)
                                    #bot = bot + sz_bot
                                    #top = top + sz_top
                                    #print(bot)
                                    #if pitcher_atbats[a] == row[0]:
                                    h +=1
                graph(x,y, pitch)
            else:
                z += 1
                
        elif b == 'ALL' and c == 'any' and other == 'any':
            if a == dtdy[z]:
                #print(number[z])
                ID = number[z]
                with open('atbats.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)

                    for row in plots:
                        #if a > k :
                        if  number[z] == row[8]:
                            pitcher_atbats.append(row[0])


                with open('pitches.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)
                    x = []
                    y = []
                    pitch= []
                    h = int(0)
                    for row in plots:
                        if h == 3000:
                            break
                        else:
                            if row[0] in pitcher_atbats:# and row[4] == other and row[22] == c:

                                    x.append(float(row[20]))
                                    y.append(float(row[21]))
                                    pitch.append(row[19])
                                    #sz_bot = (float(row[26]))
                                    #sz_top = (float(row[27]))
                                    #print(sz_bot)
                                    #bot = bot + sz_bot
                                    #top = top + sz_top
                                    #print(bot)
                                    #if pitcher_atbats[a] == row[0]:
                                    h +=1
                graph(x,y, pitch)
            else:
                z += 1
        elif b == 'ALL' and s == 'any' and other == 'any':
            if a == dtdy[z]:
                #print(number[z])
                ID = number[z]
                with open('atbats.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)

                    for row in plots:
                        #if a > k :
                        if  number[z] == row[8]:
                            pitcher_atbats.append(row[0])


                with open('pitches.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)
                    x = []
                    y = []
                    pitch= []
                    h = int(0)
                    for row in plots:
                        if h == 3000:
                            break
                        else:
                            if row[0] in pitcher_atbats: # and row [19] == b  and row[4] == other and row[22] == c:

                                    x.append(float(row[20]))
                                    y.append(float(row[21]))
                                    pitch.append(row[19])
                                    #sz_bot = (float(row[26]))
                                    #sz_top = (float(row[27]))
                                    #print(sz_bot)
                                    #bot = bot + sz_bot
                                    #top = top + sz_top
                                    #print(bot)
                                    #if pitcher_atbats[a] == row[0]:
                                    h +=1
                graph(x,y, pitch)
            else:
                z += 1
        elif b != 'ALL' and c == 'any' and other == 'any':
            if a == dtdy[z]:
                print(number[z])
                print(z)
                ID = number[z]
                with open('atbats.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)

                    for row in plots:
                        if  number[z] == row[8]:
                            pitcher_atbats.append(row[0])


                with open('pitches.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)
                    x = []
                    y = []
                    pitch= []
                    h = int(0)
                    for row in plots:
                        if h == 300000000:
                            break
                        else:
                            if row[0] in pitcher_atbats and row [19] == b:
                                    x.append(float(row[20]))
                                    y.append(float(row[21]))
                                    pitch.append(row[19])
                                    #sz_bot = (float(row[26]))
                                    #sz_top = (float(row[27]))
                                    #print(sz_bot)
                                    #bot = bot + sz_bot
                                    #top = top + sz_top
                                    #print(bot)
                                    #if pitcher_atbats[a] == row[0]:
                                    h +=1
                graph(x,y, pitch)
            else:
                z += 1
        elif b != 'ALL' and c == 'any' and other != 'any':
            if a == dtdy[z]:
                print(number[z])
                print(z)
                ID = number[z]
                with open('atbats.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)

                    for row in plots:
                        if  number[z] == row[8]:
                            pitcher_atbats.append(row[0])


                with open('pitches.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)
                    x = []
                    y = []
                    pitch= []
                    h = int(0)
                    for row in plots:
                        if h == 300000000:
                            break
                        else:
                            if row[0] in pitcher_atbats and row [19] == b and row[5] == other:
                                    x.append(float(row[20]))
                                    y.append(float(row[21]))
                                    pitch.append(row[19])
                                    #sz_bot = (float(row[26]))
                                    #sz_top = (float(row[27]))
                                    #print(sz_bot)
                                    #bot = bot + sz_bot
                                    #top = top + sz_top
                                    #print(bot)
                                    #if pitcher_atbats[a] == row[0]:
                                    h +=1
                graph(x,y, pitch)
            else:
                z += 1    
        elif b != 'ALL' and c != 'any' and other == 'any':
            if a == dtdy[z]:
                print(number[z])
                print(z)
                ID = number[z]
                with open('atbats.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)

                    for row in plots:
                        if  number[z] == row[8]:
                            pitcher_atbats.append(row[0])


                with open('pitches.csv','r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    next (plots)
                    x = []
                    y = []
                    pitch= []
                    h = int(0)
                    for row in plots:
                        if h == 300000000:
                            break
                        else:
                            if row[0] in pitcher_atbats and row [19] == b and row[5] == other and row[22] == c:
                                    x.append(float(row[20]))
                                    y.append(float(row[21]))
                                    pitch.append(row[19])
                                    #sz_bot = (float(row[26]))
                                    #sz_top = (float(row[27]))
                                    #print(sz_bot)
                                    #bot = bot + sz_bot
                                    #top = top + sz_top
                                    #print(bot)
                                    #if pitcher_atbats[a] == row[0]:
                                    h +=1
                graph(x,y, pitch)
            else:
                z += 1
mainloop()

