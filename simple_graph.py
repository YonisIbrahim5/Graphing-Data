import matplotlib.pyplot as plt

ind_var = range(1, 10_001)
dep_var = [x * x for x in ind_var]
plt.style.use('dark_background')
print(dep_var)
figure, graph = plt.subplots()
graph.scatter(ind_var, dep_var, s=10, c=dep_var, cmap=plt.cm.Greys)
#graph.plot(ind_var, dep_var, linewidth=3, color='blue')
graph.set_title('Square Numbers', fontsize=24)
graph.set_xlabel('Value', fontsize=14)
graph.set_ylabel('Square Values', fontsize=14)
graph.tick_params(labelsize=14)
graph.axis([1,10000, 1,100_000_000])
graph.ticklabel_format(axis='y', style='plain')
#plt.save()
plt.savefig('simple_squares_graph.png', bbox_inches='tight', pad_inches=0.5 )