import pandas as pd
import numpy as np
import random
import time
import math
import matplotlib.pyplot as plt


#greedy , 2-way opt, prims mst, near neighbour
lst = [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38],[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38],[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38],[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38],[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]]
lst1 = [[0.0, 0.0005662441253662109, 0.0, 0.0, 0.0005888938903808594, 0.0010118484497070312, 0.0011105537414550781, 0.0019071102142333984, 0.0020856857299804688, 0.0020666122436523438, 0.003995418548583984, 0.0029954910278320312, 0.003998756408691406, 0.003119945526123047, 0.00400543212890625, 0.004015207290649414, 0.005932331085205078, 0.007999420166015625, 0.008000612258911133, 0.009000539779663086, 0.009999752044677734, 0.01100015640258789, 0.014997243881225586, 0.014150142669677734, 0.023489952087402344, 0.032592058181762695, 0.027999401092529297, 0.022064208984375, 0.027019023895263672, 0.03878474235534668, 0.03152179718017578, 0.03603219985961914, 0.046514272689819336, 0.0520167350769043, 0.045800209045410156, 0.052658796310424805, 0.05219411849975586],[0.0013880729675292969, 0.0015325546264648438, 0.00421452522277832, 0.0020093917846679688, 0.0036284923553466797, 0.0020029544830322266, 0.004571199417114258, 0.0019979476928710938, 0.003009796142578125, 0.006090879440307617, 0.003000497817993164, 0.002000093460083008, 0.0019996166229248047, 0.003998517990112305, 0.003075122833251953, 0.004002809524536133, 0.003013134002685547, 0.003996610641479492, 0.003996610641479492, 0.004998445510864258, 0.005000114440917969, 0.005006313323974609, 0.036173343658447266, 0.012880563735961914, 0.008317232131958008, 0.010055780410766602, 0.0110015869140625, 0.01196908950805664, 0.011507034301757812, 0.013061285018920898, 0.011070489883422852, 0.011590957641601562, 0.01754283905029297, 0.024512052536010742, 0.03454995155334473, 0.015067338943481445, 0.017069578170776367],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0004467964172363281, 0.0, 0.0, 0.0009744167327880859, 0.0, 0.0009992122650146484, 0.001051187515258789, 0.0020017623901367188, 0.0009982585906982422, 0.0009984970092773438, 0.0019996166229248047, 0.0020706653594970703, 0.0029299259185791016, 0.0025904178619384766, 0.002997159957885742, 0.003001689910888672, 0.003929853439331055, 0.004070281982421875, 0.004000663757324219, 0.005930900573730469, 0.007002353668212891, 0.006932973861694336, 0.007040977478027344, 0.0071659088134765625, 0.008920907974243164, 0.01106572151184082, 0.01100301742553711, 0.011085748672485352, 0.010987997055053711, 0.011907577514648438, 0.013995885848999023]]

count = 0
algos = ['Greedy', 'Christofide', 'Nearest neighbour',]
axes = ()*len(algos)
fig,axes  = plt.subplots(1,len(algos))
fig.suptitle('Computational Time')

fig.set_figwidth(15)
count=0
for ax in axes:
    ax.plot(lst[count],lst1[count], label=algos[count])
    ax.legend(loc="upper right")
    ax.set_xlabel('Num of Nodes')
    ax.set_ylabel('Time (Sec)')
    count +=1

#plot for Greedy algorithm
lst = [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]]
lst1 = [[0.00099945068359375, 0.0013146400451660156, 0.0010249614715576172, 0.0005068778991699219, 0.0010128021240234375, 0.01044154167175293, 0.047928810119628906, 0.43081045150756836, 4.891796350479126, 64.00399112701416],  [0.0,0.0,0.0, 0.0, 1.23, 1.23, 1.38, 2.00, 2.023, 3.295553207397461, 3.715196132659912, 3.920621871948242, 4.659349679946899, 4.911469221115112, 5.3063764572143555, 6.01401948928833, 7.299309253692627, 7.339043140411377, 7.945147752761841, 7.9108827114105225, 9.000431537628174, 8.482158184051514, 9.013855934143066, 9.553544759750366, 10.06937837600708, 11.217925786972046, 10.497568607330322, 10.652863502502441, 11.401632070541382, 11.388334274291992, 12.808216094970703, 12.640511751174927, 12.923846006393433, 13.902282953262329, 14.207194805145264, 14.141585350036621, 14.62455701828003], [0.0, 0.0005030632019042969, 0.0010132789611816406, 0.0004961490631103516, 0.0010001659393310547, 0.0009999275207519531, 0.0009996891021728516, 0.0020008087158203125, 0.0019989013671875, 0.0030324459075927734, 0.003038167953491211, 0.0039784908294677734, 0.004035472869873047, 0.005992889404296875, 0.007997274398803711, 0.007982254028320312, 0.009081840515136719, 0.009595155715942383, 0.010099411010742188, 0.01109933853149414, 0.01699995994567871, 0.01499629020690918, 0.017002105712890625, 0.01991868019104004, 0.02399897575378418, 0.026201725006103516, 0.026601791381835938, 0.032541751861572266, 0.07087850570678711, 0.04710865020751953, 0.040419816970825195, 0.06782078742980957, 0.06198859214782715, 0.04928898811340332, 0.05451679229736328, 0.061684370040893555, 0.07445883750915527]]
count = 0
algos = ['Brute','Genetic', 'MST with Prims']
axes = ()*len(algos)
fig,axes  = plt.subplots(1,len(algos))
fig.suptitle('Computational Time')
#fig.legend('Naive')
fig.set_figwidth(15)
count=0
for ax in axes:
    ax.plot(lst[count],lst1[count], label=algos[count])
    ax.legend(loc="upper right")
    ax.set_xlabel('Num of Nodes')
    ax.set_ylabel('Time (Sec)')
    count +=1

    
