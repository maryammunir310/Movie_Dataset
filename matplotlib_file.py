# import matplotlib.pyplot as plt 
# x=[1,2,3,4,5,]
# y=[6,7,8,8,10]
# plt.plot(x,y,color="Green",marker="o",linestyle="--")
# plt.title("MY first Graph")
# plt.xlabel("X_AXIS")
# plt.ylabel("Y_LABEL")
# plt.show()



# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# temp = [30, 32, 35, 37, 36]
# humidity = [60, 58, 55, 53, 52]

# plt.style.use('ggplot')  # clean look
# plt.plot(x, temp, 'o--', color='red', label='Temperature (°C)')
# plt.plot(x, humidity, 's-', color='blue', label='Humidity (%)')

# plt.title("Weather Report")
# plt.xlabel("Days")
# plt.ylabel("Values")

# plt.xticks([1, 2, 3, 4, 5], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
# plt.legend(loc='upper right')
# plt.grid(True, linestyle='--', alpha=0.6)

# plt.show()




import matplotlib.pyplot as plt

marks = [45, 50, 52, 60, 61, 63, 67, 69, 70, 75, 78, 82, 85, 87, 90, 93]

plt.hist(marks, bins=5, color='skyblue', edgecolor='black')

plt.title("Students' Marks Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")

plt.show()
