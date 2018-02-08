import matplotlib.pyplot as plt
import pylab as pl

queries_list,threads_list,threads_running_list = list(),list(),list()
with open("broken_line_graph_data.txt") as f:
    for f_read in f.readlines():
        queries,threads,threads_running = f_read.split(" ")
        queries_list.append(float(queries))
        threads_list.append(float(threads))
        threads_running_list.append(float(threads_running))


def gen_list(lenght):
    temp_list = list()
    for i in range(lenght):
        temp_list.append(i)

    return temp_list

x = gen_list(len(queries_list))
y = queries_list
z = threads_list
pl.plot(x,y)
# pl.plot(z,y)
pl.show()
# print(queries_list)