# -*- coding: utf-8 -*-
# 二开：https://github.com/wongzeon/ICP-Checker
import os
import time
import time
import argparse
import datetime
from ICPUrl import ICPUrl

os.environ['no_proxy'] = '*'



def main(icpurl):
    icpurl.query_base()
    while (icpurl.get_cookies()):
        while (icpurl.get_token()):
            while(icpurl.get_check_pic()):
                while (icpurl.get_sign()):
                    while(icpurl.get_beian_info()):
                        while (1):
                            if(icpurl.data_saver()):
                                break
                        break
                    break
                break
            break
        break

if __name__ == '__main__':
    # 创建解析器对象
    parser = argparse.ArgumentParser(description='批量查询ICP备案信息')

    # 创建互斥参数组
    group = parser.add_mutually_exclusive_group()

    # 添加命令行参数选项
    group.add_argument('-o', '--file-path', help='批量查询，输入文件路径')
    group.add_argument('-d', '--doma_name', help='单个查询，输入公司名称或主域名')

    # 解析命令行参数
    args = parser.parse_args()

    # 获取文件路径参数的值
    file_path = args.file_path

    # 获取单个数值
    doma_name = args.doma_name

    # 规定唯一的表格文件路径
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name_path = f"./resultss"

    if file_path:
        print('----------------------------------------------------')
        print('[*]读取到传入文件：'+file_path)
        print('[*]数据保存地址：'+file_name_path)
        print('----------------------------------------------------')
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                line = line.strip()
                icp = ICPUrl(line, file_name_path)
                main(icp)
                # main(line,file_name_path)
                time.sleep(1) # 睡眠5秒，防止接口被绊掉
    elif doma_name:
        print('----------------------------------------------------')
        icp = ICPUrl(doma_name, file_name_path)
        main(icp)
        # main(doma_name,file_name_path)
    else:
        print('请提供文件路径参数。使用 -h 或 --help 选项获取帮助信息。')
