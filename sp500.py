#Written by Sam Trippy
#Data from Kaggle: https://www.kaggle.com/camnugent/sandp500/data
#A functional program to play around with S&P 500 stock data (1 year dataset)

###########################
#   Importing modules     #
###########################
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplt
import matplotlib.ticker as tckr
import matplotlib.dates as dts

###########################
#   Reading the data      #
###########################
def getData():
    stocks = pd.read_csv('stocks_1yr.csv') #read the file
    return stocks

###########################
#      Exploring data     #
###########################
def tickers():
    """ returns the tickers of the stocks within the dataset"""
    stocks = getData()
    tickers = np.sort(stocks.Name.unique(),kind='quicksort') #find unique & quicksort
    print(tickers)

def AnnualReview():
    """ return preliminary data about a stock's annual performance"""
    stocks = getData() #get the data

    pick = input("Enter the ticker for the stock you want to analyze: ")
    #placeholder for cross-referencing another data set or calling an API to get the actual stock name
    print("You have chosen " + pick)
    pickdata = stocks[stocks['Name'] == pick]
    highs = pickdata['High']
    printhighs = input("Would you like to plot the highs? (y/n) : ")
    if(printhighs == 'y'):
        autoPlot(pick, 'High')
    lows = pickdata['Low']
    printlows = input("Would you like to plot the lows? (y/n) : ")
    if(printlows == 'y'):
        autoPlot(pick, 'Low')
    print("Any plots have been saved as a .png image file titled " + pick + "[High or Low].png")
    
def autoPlot(pick, category):
    """ return a plot data about a stock's annual highs"""
    stocks = getData()
    pickdata = stocks[stocks['Name'] == pick]
    
    x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in pickdata['Date']]
    y = pickdata[category]

    pyplt.gca().xaxis.set_major_formatter(dts.DateFormatter('%m/%d/%Y'))
    pyplt.gca().xaxis.set_major_locator(dts.DayLocator(interval=60))
    pyplt.gca().yaxis.set_major_locator(tckr.MultipleLocator(100))

    pyplt.plot(x,y) #plot x and y
    pyplt.grid(True) #turn on grid
    pyplt.ylim(0) #sets the y axis min
    pyplt.xticks(rotation=90,fontsize = 10) # rotates x axis ticks
    pyplt.title(pick) #print title 
    pyplt.ylabel('Stock Price For '+ category) #label y axis
    pyplt.xlabel('Date') #label x axis

    pyplt.savefig(pick+category+'.png')
    print("Your plot has been saved as a .png image file titled " + pick + category + '.png')

def Plot():
    """ return a plot data about a stock's annual highs"""
    stocks = getData()
    pick = input("Enter the ticker for the stock you want to analyze: ")
    #placeholder for cross-referencing another data set or calling an API to get the actual stock name
    print("You have chosen " + pick + ", or [NAME]")
    pickdata = stocks[stocks['Name'] == pick]
    category = input("Would you like to print 'High' or 'Low' data?: ")
    if (category == 'high'):
        category = 'High'
        print("You have chosen " + category)
    elif (category == 'low'):
        category = 'Low'
        print("You have chosen " + category)
    elif (category != 'High' or category!= 'Low'):
        print("Sorry, please enter High or Low")
    else:
        print("You have chosen " + category)
    
    x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in pickdata['Date']]
    y = pickdata[category]

    pyplt.gca().xaxis.set_major_formatter(dts.DateFormatter('%m/%d/%Y'))
    pyplt.gca().xaxis.set_major_locator(dts.DayLocator(interval=60))
    pyplt.gca().yaxis.set_major_locator(tckr.MultipleLocator(100))

    pyplt.plot(x,y) #plot x and y
    pyplt.grid(True) #turn on grid
    pyplt.ylim(0) #sets the y axis min
    pyplt.xticks(rotation=90,fontsize = 10) # rotates x axis ticks
    pyplt.title(pick) #print title 
    pyplt.ylabel('Stock Price For '+ category) #label y axis
    pyplt.xlabel('Date') #label x axis

    pyplt.savefig(pick+category+'.png')
    print("Your plot has been saved as a .png image file titled " + pick + category + '.png')
