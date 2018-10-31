import nexfile
import numpy as np
import scipy.sparse as ss




reader = nexfile.Reader()
fileData = reader.ReadNexFile('C:\\Users\\siddh\\PycharmProjects\\\CNN_RodentData\\1065\\1065u065merge-clean.nex')
dictlist=[]
for key, value in dict.items(fileData):
    temp = [value]
    dictlist.append(temp)
temp=str(dictlist[0])
temp1=temp.split('\'End\':')
temp2=temp1[1].split(',')
print("Total Recording time:"+str(temp2[0])+" sec"+"   "+str(int((float(temp2[0])*1000)))+ " msec" )

vars=dictlist[1]
var_str=str(vars).split("]},")
all_val=[]
k=0
for j in range (len(var_str)):
    temp=var_str[j].split('Name\': \'')
    name=temp[1].split('\', \'DataOffset\':')
    if(name[0].__contains__("CA1")):
        ms = np.zeros((int((float(temp2[0]) * 1000))))
        k=k+1
        temp=name[1].split('\'Timestamps\': [')
        values=temp[1].split(', ')
        #print(values)
        P=1000
        val_np=np.asarray(values)

        ms_np=np.zeros((len(val_np)))
        for i in range(0,len(val_np)):
            ms_np[i]=float(val_np[i])*1000
        print(str(k) + " " + name[0]+" "+ str(int(ms_np[len(val_np)-1])) )  # ----------------------------------

        for i in range(0,len(ms_np)):
            ms[int(ms_np[i])]=1
        all_val.append(ms)


print(np.shape(all_val))
data_csr = ss.csr_matrix(np.asarray(all_val))
ss.save_npz('input.npz', data_csr)


print("---------------------------------------------")
all_val=[]
k=0
for j in range (len(var_str)):
    temp=var_str[j].split('Name\': \'')
    name=temp[1].split('\', \'DataOffset\':')
    if(name[0].__contains__("CA3")):
        ms = np.zeros((int((float(temp2[0]) * 1000))))
        k=k+1
        temp=name[1].split('\'Timestamps\': [')
        values=temp[1].split(', ')
        #print(values)
        P=1000
        val_np=np.asarray(values)

        ms_np=np.zeros((len(val_np)))
        for i in range(0,len(val_np)):
            ms_np[i]=float(val_np[i])*1000
        print(str(k) + " " + name[0]+" "+ str(int(ms_np[len(val_np)-1])) )  # ----------------------------------

        for i in range(0,len(ms_np)):
            ms[int(ms_np[i])]=1
        all_val.append(ms)

print(np.shape(np.reshape(np.asarray(all_val[1]),(1,len(all_val[1]))   )))
data_csr = ss.csr_matrix(np.reshape(np.asarray(all_val[1]),(1,len(all_val[1]))   ))
ss.save_npz('output.npz', data_csr)

all_val=[]
