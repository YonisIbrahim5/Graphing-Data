import plotly.express as px
from die import Die

die1 = Die()
die2 = Die()

results = []

for roll_num in range(100):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
min_result_value = 1 + 1
max_result_value = die1.num_sides + die2.num_sides
pos_results = range(min_result_value, max_result_value+1)

for value in pos_results:
    freq = results.count(value)
    frequencies.append(freq)

fig = px.bar(x=pos_results, y=frequencies, 
            title=f'Frequence of rolling two D{die1.num_sides} dice',
            labels={'x':'Possible Values', 'y': 'Frequencey'},
         )
fig.update_layout(xaxis_dtick=1)
fig.show()


