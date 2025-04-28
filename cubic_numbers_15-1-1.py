import matplotlib.pyplot as plt

x_numbers = [1, 2, 3, 4, 5]
y_numbers = [x**3 for x in x_numbers]
figure, graph = plt.subplots()


plt.plot(x_numbers, y_numbers, linewidth=3, color='blue')
graph.set_title('Cubic Numbers', fontsize=24)
graph.set_xlabel('Number', fontsize=14)
graph.set_ylabel('Cube', fontsize=14)
plt.show()