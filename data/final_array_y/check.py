import numpy as np
y_train_1=np.load('y_train_numu_500_event_1.npy')
y_train_2=np.load('y_train_nue_500_event_1.npy')
y_train_3=np.load('y_train_numu_500_event_0.npy')
y_train_4=np.load('y_train_nue_500_event_0.npy')
y_train=np.concatenate((y_train_1, y_train_2))
y_train_22=np.concatenate((y_train_22, y_train_3))
y_train_23=np.concatenate((y_train_22, y_train_4))
counter_a=0
counter_b=0
counter_c=0
for i in range(len(y_train_23)):
    if y_train[i]==0:
        counter_a=counter_a+1
    elif y_train[i]==1:
        counter_b=counter_b+1
    elif y_train[i]==2:
        counter_c=counter_c+1

print(counter_a)
print(counter_b)
print(counter_c)
