from train_test_onehot import train, test
from train_test_onehot import Coon_0_2 as Net

# time.sleep(3600*4)

print('start')
net_name = '2-0+coon-onehot'
model_path = net_name + '.pt'
net = Net()
net = train(net, model_path=model_path)
test(net, net_name)

