cd ~/repos

#### 克隆远程仓库到本地
git clone http://github.com/shouldsee/wxpy

cd wxpy
####尝试安装
#### --user 表示安装到本地而不是全局，需要的权限比较低
python setup.py install --user

#### 报错，依赖(dependency)不存在
### 用pip 安装指定的包 （request）
# in <module>
# ImportError: No module named requests
pip install request --user

#### 或者按照一个txt文件统一安装多个包
#cat requirements.txt 
#itchat==1.2.32
#requests
#future

### 再次尝试安装
python setup.py install --user

#### 安装成功！
#### Using /home/believerx/.local/lib/python2.7/site-packages
#### Finished processing dependencies for wxpy==0.3.9.8

