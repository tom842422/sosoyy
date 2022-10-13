import win32con
import win32gui


# 谷歌浏览器
def upload_file(file_path):
    # 一级窗口
    nomb_01 = win32gui.FindWindow('#32770', '打开')  # 一级窗口
    # 二级窗口
    nomb_02 = win32gui.FindWindowEx(nomb_01, 0, 'ComboBoxEx32', None)
    # 三级窗口
    nomb_03 = win32gui.FindWindowEx(nomb_02, 0, 'ComboBox', None)
    # 四级窗口
    edit = win32gui.FindWindowEx(nomb_03, 0, 'Edit', None)
    button = win32gui.FindWindowEx(nomb_01, 0, 'Button', '打开(&O)')

    # 上传文件,发送文件路径
    # win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,r'D://apk.txt')
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
    # 点击打开按钮
    win32gui.SendMessage(nomb_01, win32con.WM_COMMAND, 1, button)


if __name__ == '__main__':
    upload_file(r"D:\work_download\32.xlsx")
