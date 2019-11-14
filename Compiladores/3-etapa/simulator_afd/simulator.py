import pandas as pd
import numpy as np

tabela = pd.DataFrame(columns = ['ES','0','1','2','3','4','5','6','7','8','9',
                                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','W''Y','Z',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z','(',')','[',']',
                                '/','*',';','.','"',"'",'+','-','<','>','='],
                      index = np.arange(91))

buffer = []
with open('input.txt','r') as file:
    input = file
    for line in file:
        buffer.append(line)
        print(line)

print(buffer)
print(tabela.tail())