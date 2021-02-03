# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:28:51 2021
Implementation of linked list in python

@author: Bilgin
"""

class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        
class linked_list:
    def __init__(self):
        self.head=node()
        
    def append(self,data):
        new_node = node(data)
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next  # this brings the curse ti the last element in cur 
        cur_node.next = new_node
    def length(self):
        cur_node = self.head
        total =0
        while cur_node.next!=None:
            total+=1
            cur_node = cur_node.next
        return total
    
    def display(self):
        elems =[]
        cur_node =self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)
        
    def get(self,index):
        if index>= self.length():
            print("ERROR: 'index' out of range")
            return None
        cur_idx=0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx ==index:
                return cur_node.data
            cur_idx+=1
            
    def erase(self,index):
        if index>= self.length():
            print("ERROR: 'index' out of range")
            return None
        cur_idx=0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx ==index:
                last_node.next = cur_node.next
                return
            cur_idx+=1
        
        
            
        

my_list = linked_list()

my_list.append('a')
my_list.append('b')
my_list.append('c')
my_list.append(1)

my_list.display()

print(f'3rd Element in list is {my_list.get(3)}')

my_list.erase(1)

my_list.display()


