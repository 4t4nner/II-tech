import pandas
data = pandas.read_csv('.\\dataset\\forestfires.csv', delimiter=',')
print(data[['X', 'Y']].min())
# X,Y,month,day,FFMC,DMC,DC,ISI,temp,RH,wind,rain,area
