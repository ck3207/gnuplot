# -*- coding: utf-8 -*-
__author__ = "chenk"
import os,time,zipfile

TARGET_DIR = "/usr/local/fortune_security/sqoopOper_CF/"
CONFIG_DIR = ""

collect_path_postfix = "collect" + os.sep + "jdbc"    # 采集目录
export_path = "export" + os.sep + "jdbc"    # 导出目录
mr_path = "jobs" + os.sep + "mr"    # jar包目录
core_site_path = "utils" + os.sep + "core-site.xml"    # core-site.xml文件

print("开始备份配置项")
# 备份配置项
for each in os.listdir(os.getcwd()):
    if each in ["collect","export","jobs","utils"]:
        try:
            command = "rm -rf " + each + "_bak" + " && mv " + each + " " + each + "_bak"
            os.popen(command)  # 历史配置备份
        except Exception as e:
            print(str(e))

print("备份历史配置完毕")
time.sleep(0.5)

os.popen("mkdir -p {collect,export,jobs,utils}")    # 创建目录
command = "mv " + TARGET_DIR + collect_path_postfix + " collect"
os.popen(command)   # 采集配置备份
command = "mv " + TARGET_DIR + export_path + " export"
os.popen(command)   # 导出配置备份
command = "mv " + TARGET_DIR + mr_path + " jobs"
os.popen(command)   # jar包备份
command = "mv " + TARGET_DIR + core_site_path + " utils"
os.popen(command)   # core-siet.xml 文件备份
print("备份当前配置完毕")
time.sleep(0.5)

# 删除
command = "rm -rf " + TARGET_DIR
os.popen(command)
print("删除目录:%s" % TARGET_DIR)
time.sleep(0.5)

# 解压
for each in os.listdir("package"):
    if ".zip" in each:
        try:
            zip_package = zipfile.ZipFile(os.getcwd()+os.sep+"package/"+each) # 绝对路径
            os.mkdir(TARGET_DIR)  # 创建rar文件解压后的存放路径
            zip_package.extractall()  # 解压文件到指定目录 即：上述路径下的目录
            # zip_package.extractall("sqoopOper_CF")  # 解压文件到指定目录
            print("Un_ZIP file[%s] Successfully!" % each)
        except Exception as e:
            print("Un Zip failed!")
            print(str(e))
        finally:
            zip_package.close()

print("解压包至:%s" % TARGET_DIR)
time.sleep(0.5)


def un_zip(path, file):
    """Extract rar file!
    Argue path is the dir, file is the one which will be extract!"""
    try:
        if path != "":
            os.chdir("/")
            os.chdir(path)
        zip_package = zipfile.ZipFile(file)
        os.mkdir(file[:-4])  # 创建rar文件解压后的存放路径
        zip_package.extractall(file[:-4])  # 解压文件到指定路径
        print("Un_ZIP file[%s] Successfully!" % file)
    except Exception as e:
        print("Un_ZIP file[%s] failed!" % file)
        print("Error:", str(e))
    finally:
        zip_package.close()

# 替换
command = "rm -rf " + TARGET_DIR + collect_path_postfix + " && cp -r collect/jdbc " + TARGET_DIR + collect_path_postfix
print(command)
os.popen(command)   # 采集配置备份
command = "rm -rf " + TARGET_DIR + export_path + " && cp -r export/jdbc " + TARGET_DIR + export_path
os.popen(command)   # 导出配置备份
command = "rm -rf " + TARGET_DIR + mr_path + " && cp -r jobs/mr " + TARGET_DIR + mr_path
os.popen(command)   # jar包备份
command = "rm -rf " + TARGET_DIR + core_site_path + " && cp -r utils/core-site.xml " + TARGET_DIR + core_site_path
os.popen(command)   # core-siet.xml 文件备份
print("替换配置项完毕")

# 赋权限
os.popen("chmod -R 777 sqoopOper_CF")

print("Done!")
