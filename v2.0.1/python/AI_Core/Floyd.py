# -*- coding: utf-8 -*-
import os
from time import sleep

_delay = 10



os.chdir('C:\\Users\\BehnamH\\Desktop\\quick-start-master')
os.system("start cmd /C floyd login --username behnamh721rn --password bam.H@721")
sleep(_delay)
os.system("start cmd /C floyd init test_rl")
sleep(_delay)
os.system("start cmd /K floyd run --gpu --env tensorflow-1.3 'python train_and_eval.py'")