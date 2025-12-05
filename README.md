# 文件夹批量创建脚本

这是一个功能强大的Python脚本，可以帮助您在指定目录中自动按顺序编号创建文件夹。

## 功能特点

- 📁 **自动编号**：自动检测已有编号并从下一个可用编号开始创建文件夹
- 📂 **批量创建**：支持创建单个或多个文件夹
- 🎯 **自定义目录**：可以选择在任意目录创建文件夹，默认使用脚本所在目录
- 🛡️ **错误检查**：包含完整的错误处理和用户友好的提示信息
- 💡 **智能识别**：自动识别已有文件夹的编号，避免重复

## 使用方法

### 1. 运行脚本

直接运行 `create_numbered_folders.py` 文件：

```bash
python create_numbered_folders.py
```

### 2. 选择创建目录

- 直接回车：使用脚本所在目录作为默认创建目录
- 输入路径：指定自定义的创建目录

### 3. 创建文件夹

输入要创建的文件夹名称和数量：

- **创建单个文件夹**：输入文件夹名称，例如 `test`
- **批量创建文件夹**：输入文件夹名称和数量，例如 `test 5`
- **退出脚本**：输入 `quit` 或 `exit`

## 示例

### 示例1：创建单个文件夹

```
请输入要创建的文件夹名称和数量（如：test 5，输入'quit'退出）: test
已创建文件夹: D:\workspace\VSC\AutoCreateFolders\test_01
```

### 示例2：批量创建5个文件夹

```
请输入要创建的文件夹名称和数量（如：test 5，输入'quit'退出）: test 5
正在创建 5 个文件夹...
已创建文件夹: D:\workspace\VSC\AutoCreateFolders\test_02
已创建文件夹: D:\workspace\VSC\AutoCreateFolders\test_03
已创建文件夹: D:\workspace\VSC\AutoCreateFolders\test_04
已创建文件夹: D:\workspace\VSC\AutoCreateFolders\test_05
已创建文件夹: D:\workspace\VSC\AutoCreateFolders\test_06

✅ 已成功创建 5 个文件夹！
```

### 示例3：继续创建文件夹

```
请输入要创建的文件夹名称和数量（如：test 5，输入'quit'退出）: test
已创建文件夹: D:\workspace\VSC\AutoCreateFolders\test_07
```

## 文件夹命名规则

创建的文件夹将按照以下格式命名：

```
文件夹名称_01
文件夹名称_02
文件夹名称_03
...
```

- 编号使用两位数格式（01, 02, 03...）
- 自动检测已有的最高编号，从下一个编号开始创建

## 注意事项

1. 确保您对指定的创建目录有写入权限
2. 文件夹名称不能包含以下非法字符：`< > : " / \ | ? *`
3. 创建数量必须是大于0的整数
4. 如果指定的目录不存在，脚本会提示错误

## 系统要求

- Python 3.x
- 兼容 Windows、macOS 和 Linux 系统

## 安装和运行

1. 下载 `create_numbered_folders.py` 文件
2. 打开终端或命令提示符
3. 导航到脚本所在目录
4. 运行命令：`python create_numbered_folders.py`

## 退出脚本

在创建文件夹的提示中输入以下命令之一退出：
- `quit`
- `exit`
