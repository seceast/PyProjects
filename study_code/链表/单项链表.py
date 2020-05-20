"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 单项链表.py
@time: 2019/10/21 0021 10:16
"""


class Node:
    def __init__(self, elem):
        self.elem = elem  # elem指数据元素
        self.next = None  # next是下一节点的标识


class SingleLinkList:

    def __init__(self, node=None):
        if node is not None:
            head_node = Node(node)
            self.__head = head_node
        else:
            self.__head = node

    def add(self, item):
        """在头部添加元素"""
        pass

    def append(self, item):
        """尾部添加"""
        pass

    def insert(self, pos, item):
        """在指定位置添加"""
        pass

    def remove(self, item):
        """删除节点"""
        pass

    def search(self, item):
        """查找节点是否存在"""
        pass

    def is_empty(self):
        """是否为空"""
        return self.__head is None

    def link_length(self):
        """链表长度"""
        count = 0
        cur_node = self.__head
        while cur_node is not None:
            cur_node = cur_node.next
            count += 1
        return count

    def link_travel(self):
        """遍历链表"""
        cur_node = self.__head
        while cur_node is not None:
            pass




if __name__ == '__main__':
    # 初始化元素值为20的单项链表,也可以不传参数，创建空链表
    sing_list = SingleLinkList()

    print(sing_list.is_empty())
    print(sing_list.link_length())
