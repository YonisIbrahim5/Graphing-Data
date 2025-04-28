import matplotlib.pyplot as plt

ind_var = range(1, 6)
dep_var = [x * x for x in ind_var]

print(dep_var)

figure, graph = plt.subplots()
graph.plot(ind_var, dep_var, linewidth=3, color='blue')
graph.set_title('Square Numbers', fontsize=24)
graph.set_xlabel('Value', fontsize=14)
graph.set_ylabel('Square Values', fontsize=14)
graph.tick_params(labelsize=14)


plt.show()