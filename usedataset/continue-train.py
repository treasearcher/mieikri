from train_test import train, test, set_record_file
from train_test import Justreducelr_0 as Net
import torch

# time.sleep(3600*16)


print('start')
net_name = '0-justreducelr'
model_path = net_name + '.pt'
set_record_file('record' + net_name + '.txt')
net = Net()
net.load_state_dict(torch.load(model_path))
net.eval()
net = train(net=net, model_path=model_path)
test(net, net_name)


