import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
from sklearn.preprocessing import MinMaxScaler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from keras.layers import Dense, LSTM
from keras.models import Sequential


def stockGraph(window, x):
    plt.style.use('fivethirtyeight')

    df = web.DataReader(x, data_source= 'yahoo', start = '2012-01-01', end= '2019-12-17')
    
    data = df.filter(['Close'])
    dataset = data.values
    trainingDataLen = math.ceil( len(dataset) * .8)

    scaler = MinMaxScaler(feature_range=(0,1))
    scaledData = scaler.fit_transform(dataset)

    trainData = scaledData[0:trainingDataLen, : ]

    xTrain = []
    yTrain = []

    for i in range(60,len(trainData)):
        xTrain.append(trainData[i-60:i,0])
        yTrain.append(trainData[i,0])
        
    xTrain,yTrain = np.array(xTrain), np.array(yTrain)
    #Reshape the data into the shape accepted by the LSTM
    xTrain = np.reshape(xTrain, (xTrain.shape[0], xTrain.shape[1], 1))
   
    #Build the LSTM network model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape= (xTrain.shape[1],1)))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=25))
    model.add(Dense(units=1))
    
    #Compiles Model
    model.compile(optimizer='adam', loss='mean_squared_error')

    #Train the model
    model.fit(xTrain, yTrain, batch_size=1, epochs=1)

    #Test data set
    testData = scaledData[trainingDataLen - 60: , : ]

    #Create the x_test and y_test data sets
    xTest = []
    yTest =  dataset[trainingDataLen : , : ] #Get all of the rows from index 1603 to the rest and all of the columns (in this case it's only column 'Close'), so 2003 - 1603 = 400 rows of data
    for i in range(60,len(testData)):
        xTest.append(testData[i-60:i,0])

    #Convert x_test to a numpy array 
    xTest = np.array(xTest)

    #Reshape the data into the shape accepted by the LSTM
    xTest = np.reshape(xTest, (xTest.shape[0],xTest.shape[1],1))

    #Getting the models predicted price values
    predictions = model.predict(xTest) 
    predictions = scaler.inverse_transform(predictions)#Undo scaling

    #Calculate/Get the value of RMSE
    rmse=np.sqrt(np.mean(((predictions- yTest)**2)))
    rmse

    #Plot/Create the data for the graph
    train = data[:trainingDataLen]
    valid = data[trainingDataLen:]
    valid['Predictions'] = predictions

    #Visualize the data
    figure1 = plt.figure(figsize=(8,4))
    plt.xlabel('Date', fontsize=10)
    plt.ylabel('Close Price '+x, fontsize=10)
    plt.plot(train['Close'])
    plt.plot(valid[['Close', 'Predictions']])
    plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
    line2 = FigureCanvasTkAgg(figure1, window)
    line2.get_tk_widget().pack()

def createReport(x):
    df = web.DataReader(x, data_source= 'yahoo', start = '2012-01-01', end= '2019-12-17')
    
    data = df.filter(['Close'])
    dataset = data.values
    trainingDataLen = math.ceil( len(dataset) * .8)

    scaler = MinMaxScaler(feature_range=(0,1))
    scaledData = scaler.fit_transform(dataset)

    trainData = scaledData[0:trainingDataLen, : ]

    xTrain = []
    yTrain = []

    for i in range(60,len(trainData)):
        xTrain.append(trainData[i-60:i,0])
        yTrain.append(trainData[i,0])
        
    xTrain,yTrain = np.array(xTrain), np.array(yTrain)
    #Reshape the data into the shape accepted by the LSTM
    xTrain = np.reshape(xTrain, (xTrain.shape[0], xTrain.shape[1], 1))
   
    #Build the LSTM network model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape= (xTrain.shape[1],1)))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=25))
    model.add(Dense(units=1))
    
    #Compiles Model
    model.compile(optimizer='adam', loss='mean_squared_error')

    #Train the model
    model.fit(xTrain, yTrain, batch_size=1, epochs=1)

    #Test data set
    testData = scaledData[trainingDataLen - 60: , : ]

    #Create the x_test and y_test data sets
    xTest = []
    yTest =  dataset[trainingDataLen : , : ] #Get all of the rows from index 1603 to the rest and all of the columns (in this case it's only column 'Close'), so 2003 - 1603 = 400 rows of data
    for i in range(60,len(testData)):
        xTest.append(testData[i-60:i,0])

    #Convert x_test to a numpy array 
    xTest = np.array(xTest)

    #Reshape the data into the shape accepted by the LSTM
    xTest = np.reshape(xTest, (xTest.shape[0],xTest.shape[1],1))

    #Getting the models predicted price values
    predictions = model.predict(xTest) 
    predictions = scaler.inverse_transform(predictions)#Undo scaling


    #Plot/Create the data for the graph
    train = data[:trainingDataLen]
    valid = data[trainingDataLen:]
    valid['Predictions'] = predictions
    userQuote = web.DataReader(x, data_source='yahoo',start='2012-01-01', end='2019-12-17')
    newDf = userQuote.filter(['Close'])

    last60Days = newDf[-60:].values
    last60DaysScaled = scaler.transform(last60Days)

    XTest = []
    XTest.append(last60DaysScaled)
    XTest = np.array(XTest)
    XTest = np.reshape(XTest, (XTest.shape[0], XTest.shape[1], 1))

    predictedPrice = model.predict(XTest)

    predictedPrice = scaler.inverse_transform(predictedPrice)
    with open("SearchResults.txt", 'a') as f:
        f.write(
            valid.to_string(header = True, index = True)
        )
    