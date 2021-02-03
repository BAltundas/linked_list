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
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
    def length(self):
        cur = self.head
        total =0
        while cur.neaxt!=None:
            total+=1
            cur = cur.next
        return total
    def display(self):
        elems =[]
        cur_node =self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)

my_list = linked_list()
my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.display()

