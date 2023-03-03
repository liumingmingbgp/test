from pathlib import Path
import time

filepath = '8_自动组织文件/test.txt'

### 获取文件大小
def get_filesize(filepath):
    fsize = Path(filepath).stat().st_size
    fsize = fsize/float(1000*1000)
    return round(fsize,4)
filesize = get_filesize(filepath)
print(f'文件大小：{filesize}MB')

### 获取文件创建与修改时间
def get_time(timestamp):
    '''格式化时间戳'''
    t = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', t)   
 
ctime = Path(filepath).stat().st_ctime  # 文件创建时间
ctime = get_time(ctime)

mtime = Path(filepath).stat().st_mtime  # 文件修改时间
mtime = get_time(mtime)

print(f'文件创建时间：{ctime}, 文件修改时间：{mtime}')