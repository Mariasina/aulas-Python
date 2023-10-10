# -*- coding: utf-8 -*-

import time

def contador(inicio, fim, passo):
    for i in range(inicio, fim+1, passo):
        print(i)
        time.sleep(0.5)
     
        
contador(1,20,1)
    