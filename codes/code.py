sample_space = [1,1,2,2,2,3]
frequency = {1:sample_space.count(1),2:sample_space.count(2),3:sample_space.count(3)}
probability = {1:frequency[1]/6,2:frequency[2]/6,3:frequency[3]/6}
print(f'P(2) = {probability[2]}')
print(f'P(1 or 3) = {probability[1]+probability[3]}')
print(f'P(not 3) = {1 - probability[3]}')
x = [1,2,3]
y = [probability[1],probability[1]+probability[2],probability[1]+probability[2]+probability[3]]
plt.plot(x,y,label = 'CDF')
z = [probability[1],probability[2],probability[3]]
plt.plot(x,z,label = 'PMF')
plt.legend()
plt.show()
