from typing import Any
from collections import deque
from random import random
import pickle
class StackisFull(Exception):
    def __str__(self):
        return 'The Stack is Full'
class StackisEmpty(Exception):
    def __str__(self):
        return 'The Stack is Empty'
class Stack:
    def __init__(self,maxlen:int=256)->None:
        self.capacity=maxlen
        self.__stk=deque([],maxlen)
    def __len__(self)->int:
        return len(self.__stk)
    def is_empty(self)->bool:
        return not self.__stk
    def is_full(self)->bool:
        return len(self.__stk)==self.__stk.maxlen
    def push(self,value:Any)->None:
        try:self.__stk.append(value)
        except:raise StackisFull
    def pop(self)->Any:
        try:return self.__stk.pop()
        except IndexError:raise StackisEmpty
    def peek(self)->Any:
        return self.__stk[-1]
    def clear(self)->None:
        self.__stk.clear()
    def find(self,value:Any)->Any:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1
    def count(self,value:Any)->int:
        return self.__stk.count(value)
    def __contains__(self,value:Any)->bool:
        return self.count(value)
    def dump(self,prin=True,filename='data')->int:
            if prin:
                print(list(self.__stk))
                f=open(f'{filename}.stk','wb')
                pickle.dump(list(self.__stk),f)
            else:
                f=open(f'{filename}.stk','wb')
                pickle.dump(list(self.__stk),f)
            f.close()
    def load(self,fn,prin=True):

        f=open(f'{fn}.stk','rb')

        a=pickle.load(f)

        self.__stk=list(a)
        if prin:print(a)
        else:pass
        f.close()