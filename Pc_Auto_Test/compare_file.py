# -*- coding: utf-8 -*-
# __author__ = yangyd 
# File: compare_file.py
# Create time: 2020/4/27 0027 09:22


import sys
import difflib
import os


class CompareFile:

    def __init__(self, file_dir1, file_dir2):
        self.file_dir1 = file_dir1
        self.file_dir2 = file_dir2
        
    @staticmethod
    def get_file_name(file_dir):
        """获取文件夹下的所有文件"""
        name_list = []
        for name in os.listdir(file_dir):
            if name.endswith('DAT') or name.endswith('dat'):  # 判断文件后缀名
                name_list.append(name)
        return name_list

    def get_same_name_file(self):
        """获取相同名称的文件"""
        text_list1 = self.get_file_name(self.file_dir1)
        text_list2 = self.get_file_name(self.file_dir2)
        same_name_list = []
        for file_name1 in text_list1:
            for file_name2 in text_list2:
                if file_name1 == file_name2:
                    same_name_list.append(file_name1)
        return same_name_list

    @staticmethod
    def read_file(file_name):
        """读取文件"""
        try:
            with open(file_name, 'r') as file_desc:
                # 读取后按行分割
                text = file_desc.read().splitlines()
            return text
        except IOError as error:
            print('Read input file Error: {0}'.format(error))

    def compare_file(self):
        """比较两个文件并把结果生成一份html文本"""
        name_list = self.get_same_name_file()
        for file_name in name_list:
            text1_lines = self.read_file(os.path.join(self.file_dir1, file_name))
            text2_lines = self.read_file(os.path.join(self.file_dir2, file_name))

            diff = difflib.HtmlDiff()  # 创建HtmlDiff 对象
            result = diff.make_file(text1_lines, text2_lines)  # 通过make_file 方法输出 html 格式的对比结果

            current_path = os.path.dirname(os.path.abspath(__file__))
            report_path = os.path.join(current_path, 'resultreport')
            report_file_path = os.path.join(report_path, f'result_({file_name}).html')
            # 将结果写入到result_.html文件中
            try:
                with open(report_file_path, 'w') as result_file:
                    result_file.write(result)
                    print(f"{file_name} Successfully Finished")
            except IOError as error:
                print('写入html文件错误：{0}'.format(error))


if __name__ == '__main__':
    comf = CompareFile(r'C:/Users/Administrator/ABLATION/68ea32/弹道模板-只读/output/heatflux',
                       r'E:\热烧蚀\FASHEAT_20181026_完全版\output\heatflux')
    comf.compare_file()

