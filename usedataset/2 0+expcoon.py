from train_test import train, test, set_record_file
from train_test import Coon_0_2 as Net
from MusicDataset import MusicDataThree, ExpNorm

# time.sleep(3600*4)

print('start')
set_record_file('record-expoon.txt')
net_name = '2-0+expcoon'
model_path = net_name + '.pt'
tsfm = ExpNorm()
train_set = MusicDataThree(transform=tsfm, start=0, total=1)
test_set = MusicDataThree(transform=tsfm, start=0, total=1)
net = Net()
net = train(net, model_path=model_path, dataset=train_set)
test(net, net_name, dataset=test_set)


