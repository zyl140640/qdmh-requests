import os

import yaml


# 该path为config/config.yaml
def get_object_path(path):
    """
    读取config目录
    :param path: 路径
    :return: 根目录+路径
    """
    return os.getcwd() + '/' + path


# 该方法的path可直接填写yaml文件名例如address_add.yaml，只需要更新case_data_path的路径，就可以执行新的路径下所有文件
def get_object_data_path(path):
    """
    读取data目录
    :param path:该path为yaml文件名称
    :param case_data_path: 该路径为data目录下以及文件夹名称
    :return:返回yaml文件路径
    """
    paths = read_yaml_key('config/config.yaml', 'case_data_path')
    return os.getcwd() + paths + path


# 读取文件单独参数
def read_yaml_key(path, key):
    """

    :param path:该path为yaml文件名称
    :param key:想要读取的参数
    :return:返回yaml文件单独key
    """
    with open(get_object_path(path), mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


# 读取文件所有内容
def read_yaml(path):
    """

    :param path:config/config.yaml
    :return:返回yaml文件所有数据
    """
    with open(get_object_path(path), mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


# 修改config文件操作
def change_yaml(path, key, data):
    """

    :param path:config/config.yaml
    :param key:想要修改的参数
    :param data:参数对应的值
    """
    with open(get_object_path(path), encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        value[key] = data
    with open(get_object_path(path), mode='w', encoding='utf-8') as f:
        # 将Python中的字典或者列表转化为yaml格式的数据
        yaml.dump(value, f, allow_unicode=True, sort_keys=False)
        f.close()


# 清空文件
def clear_yaml(path):
    """

    :param path:config/config.yaml
    """
    with open(get_object_path(path), mode='w', encoding='utf-8') as f:
        f.truncate()
