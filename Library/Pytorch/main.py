import torch


class TwoLayerNet(torch.nn.Module):
    def __init__(self,D_in,H,D_out):
        super(TwoLayerNet,self).__init__()
        self.linear1=torch.nn.Linear(D_in,H)
        self.linear2=torch.nn.Linear(H,D_out)
    
    def forward(self,x):
        hiden_layer_result=self.linear1(x).clamp(min=0)
        return self.linear2(hiden_layer_result)

N,D_in,H,D_out=64,1000,100,10

x = torch.randn(N, D_in)
y = torch.randn(N, D_out)

model=TwoLayerNet(D_in,H,D_out)
criterion=torch.nn.MSELoss(reduction='sum')
optimizer=torch.optim.SGD(model.parameters(),lr=1e-4)

loss_his=[]
for t in range(10000):
    y_pre=model(x)
    loss=criterion(y_pre,y)
    if t%100==0:
        loss_his.append(loss)
        print(loss)
    #Zero gradient, perform backward pass and update parameter
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


from matplotlib import pyplot as plt 
import numpy as np
plt.plot(np.arange(10000,step=100),loss_his)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.savefig('loss.png')
