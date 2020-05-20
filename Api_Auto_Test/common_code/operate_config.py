#!/user/bin/env python
# -*- coding: utf-8 -*-
# __author__ = yangyd 
# Create time: 2019/6/25 0025 17:15


from configparser import ConfigParser


class DoConfig:
    def __init__(self, file_path):
        self.file_path = file_path

    # 读取文件内容，返回字符串类似的数据
    def read_info(self, section, option):
        info = ConfigParser()
        info.read(self.file_path, encoding='utf-8')
        info_value = info.get(section, option)
        return info_value

    # 读取int型数据
    def read_int(self, section, option):
        int_info = ConfigParser()
        int_info.read(self.file_path, encoding='utf-8')
        int_value = int_info.getint(section, option)
        return int_value

    # 读取float类型的数据
    def read_float(self, section, option):
        float_info = ConfigParser()
        float_info.read(self.file_path, encoding='utf-8')
        float_value = float_info.getfloat(section, option)
        return float_value

    # 读取Bool类型的数据
    def read_bool(self, section, option):
        bool_info = ConfigParser()
        bool_info.read(self.file_path, encoding='utf-8')
        boll_value = bool_info.getfloat(section, option)
        return boll_value

    @staticmethod
    def write_config(datas, file_name):
        """
        写入配置文件,参数必须按一下格式section：区域名、option
        :param datas: 参数需按照指定的格式传入如：
                        datas = {
                            "section":{"option": "values2"},
                            "section2":{'option2': "values2"}
                        }
        :param file_name: 配置文件的路径及文件名
        :return:
        """
        write_info = ConfigParser()

        for key in datas:
            write_info[key] = datas[key]

        with open(file_name, 'a+', encoding='utf-8') as file:
            write_info.write(file)

    @staticmethod
    def batch_write(section_name, data, file_path):
        """
        批量写入配置信息
        :param section_name:section名称
        :param data:
                    data = {'mobilephone': phone,
                            'memberid': res[0]['id'],
                            'pwd': 123456
                            }
        :param file_path: 配置文件路径
        :return:
        """
        batch_conf = ConfigParser()
        batch_conf[section_name] = data

        with open(file_path, 'a+', encoding='utf-8') as file:
            batch_conf.write(file)


if __name__ == '__main__':
    from common_code import project_path

    conf = DoConfig(project_path.CONFIG_FILE_PATH)
    # print(conf.read_info('Flag', 'button'))
    #
    # data1 = {
    #     "section": {'ServerAliveInterval': 45,
    #                 'Compression': 'yes',
    #                 'CompressionLevel': 9}
    # }
    # conf.write_config(data1, 'config.conf')
    # data2 = {'ServerAliveInterval': 45,
    #          'Compression': 'yes',
    #          'CompressionLevel': 9}
    #
    # conf.batch_write('test', data2, 'test.conf')

    phone_res = eval(conf.read_info('Phone', 'phone_header'))
    print(phone_res)
