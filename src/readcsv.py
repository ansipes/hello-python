import matplotlib.pyplot as plt
import csv

x = []
y = []

with open("./src/static/temperature.csv") as f:
  f.readline()
  reader = csv.reader(f)
  for row in reader:
    y.append(int(row[0]))
    x.append(int(row[1]))

# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('My first graph!')
  
# function to show the plot
plt.show()