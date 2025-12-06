#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件夹批量创建脚本
功能：输入文件夹名称后，在指定目录自动按顺序编号创建文件夹
"""

import os
import re

def get_next_number(base_dir, folder_name):
    """
    获取下一个可用的编号
    :param base_dir: 基础目录
    :param folder_name: 文件夹名称
    :return: 下一个编号（整数）
    """
    # 正则表达式匹配 文件夹名_数字 的格式
    pattern = re.compile(rf"^{re.escape(folder_name)}_(\d+)$")
    max_num = 0
    
    # 遍历目录中的所有文件夹
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path):
            match = pattern.match(item)
            if match:
                num = int(match.group(1))
                if num > max_num:
                    max_num = num
    
    return max_num + 1

def create_numbered_folder(base_dir, folder_name):
    """
    创建带编号的文件夹
    :param base_dir: 基础目录
    :param folder_name: 文件夹名称
    :return: 创建的文件夹路径
    """
    # 获取下一个编号
    next_num = get_next_number(base_dir, folder_name)
    
    # 格式化文件夹名称，使用两位数编号
    new_folder_name = f"{folder_name}_{next_num:02d}"
    new_folder_path = os.path.join(base_dir, new_folder_name)
    
    # 创建文件夹
    os.makedirs(new_folder_path)
    print(f"已创建文件夹: {new_folder_path}")
    
    return new_folder_path

def main():
    """
    主函数
    """
    # 增强的欢迎信息和使用说明
    print("=" * 40)
    print("      文件夹批量创建脚本      ")
    print("=" * 40)
    print("功能：自动按顺序编号创建文件夹")
    print("格式：文件夹名称_01, 文件夹名称_02...")
    print("\n使用示例：")
    print("1. 输入目录后直接回车使用默认目录")
    print("2. 输入'test'创建test_01文件夹")
    print("3. 输入'test 5'批量创建test_02至test_06文件夹")
    print("4. 再次输入'test'创建test_07文件夹")
    print("5. 输入'changedir'或'cd'切换创建目录")
    print("6. 输入'quit'或'exit'退出脚本")
    print("=" * 40)
    
    # 设置默认目录为脚本所在目录，也可以让用户自定义
    default_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"\n默认创建目录：{default_dir}")
    base_dir = input("请输入您想要创建文件夹的目录（直接回车使用默认目录）: ").strip()
    
    # 如果用户没有输入目录，使用默认目录
    if not base_dir:
        base_dir = default_dir
        print(f"已选择默认目录：{base_dir}")
    
    # 检查目录是否存在
    if not os.path.exists(base_dir):
        print(f"\n❌ 错误：目录 {base_dir} 不存在！")
        print("请检查路径是否正确后重新运行脚本。")
        return
    
    print(f"\n✅ 已确认创建目录：{base_dir}")
    print("=" * 40)
    
    while True:
        # 获取用户输入的文件夹名称和数量
        user_input = input("\n请输入要创建的文件夹名称和数量（如：test 5，输入'cd'切换目录，'quit'退出）: ").strip()
        
        # 退出条件
        if user_input.lower() in ['quit', 'exit']:
            print("\n✅ 脚本已成功退出！")
            break
        
        # 切换目录指令
        if user_input.lower() in ['changedir', 'cd']:
            print("\n=== 切换创建目录 ===")
            print(f"当前目录：{base_dir}")
            new_dir = input("请输入新的创建目录（直接回车保持当前目录）: ").strip()
            
            # 如果用户没有输入新目录，保持当前目录
            if not new_dir:
                print("已取消切换目录，保持当前目录不变。")
                continue
            
            # 检查新目录是否存在
            if not os.path.exists(new_dir):
                print(f"❌ 错误：目录 {new_dir} 不存在！")
                continue
            
            # 检查新目录是否可写
            if not os.access(new_dir, os.W_OK):
                print(f"❌ 错误：没有权限写入目录 {new_dir}！")
                continue
            
            # 更新当前目录
            base_dir = new_dir
            print(f"✅ 已切换创建目录至：{base_dir}")
            print("=" * 40)
            continue
        
        # 解析用户输入，分离文件夹名称和数量
        parts = user_input.split()
        folder_name = parts[0]
        count = 1  # 默认创建1个
        
        # 如果用户输入了数量，解析数量
        if len(parts) > 1:
            try:
                count = int(parts[1])
                if count < 1:
                    print("❌ 错误：创建数量必须大于0！")
                    continue
            except ValueError:
                print("❌ 错误：数量必须是整数！")
                continue
        
        # 验证文件夹名称是否有效
        if not folder_name:
            print("❌ 错误：文件夹名称不能为空！请重新输入。")
            continue
        
        # 验证文件夹名称是否包含非法字符
        invalid_chars = '<>:"/\\|?*'
        if any(char in folder_name for char in invalid_chars):
            print(f"❌ 错误：文件夹名称不能包含以下字符：{invalid_chars}")
            continue
        
        try:
            # 批量创建文件夹
            if count == 1:
                # 创建单个文件夹
                create_numbered_folder(base_dir, folder_name)
            else:
                # 创建多个文件夹
                print(f"\n正在创建 {count} 个文件夹...")
                for _ in range(count):
                    create_numbered_folder(base_dir, folder_name)
                print(f"\n✅ 已成功创建 {count} 个文件夹！")
        except Exception as e:
            print(f"❌ 创建文件夹失败：{e}")
            print("请检查权限或路径后重试。")

if __name__ == "__main__":
    main()