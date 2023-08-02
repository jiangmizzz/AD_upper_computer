# How to run code
### 创建虚拟环境
在终端输入：
```powershell
python -m venv venv_name
```
即可在根目录下创建一个新的虚拟环境，其中venv_name为虚拟环境名，可以自己取。

### 复制环境
需要先将requirements.txt（列出了原来的虚拟环境中所有的依赖包）移入根目录，然后在终端输入：
```powershell
pip install -r requirement.txt
```
即可通过该requirements.txt把原来运行的虚拟环境复制到该目录下新建立的虚拟环境中。

### run code
在`myMain.py`文件的代码区右键并选择`run code`，即可运行代码。

### 生成可执行文件
安装pyinstaller后在终端输入`Pyinstaller -F -w myMain.py -n Upper_Computer`即可在dist目录下生成`Upper_Computer.exe`，同理可以取其他名字。