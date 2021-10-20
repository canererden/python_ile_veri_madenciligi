# coding: utf-8
get_ipython().magic('save sin_cos_grafigi 115 # 115. çalıştırılan hücredeki kodları kaydetmek için')
plt.plot(x, np.sin(x))  
plt.plot(x, np.cos(x))  
plt.plot(x, x**2) 
plt.legend(['sinüs', 'cosinüs', 'kare'], loc = 'upper left')
