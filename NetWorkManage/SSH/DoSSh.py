import os

import paramiko

def ssh(host,name,key,command):#主机，登录名，登录密码，执行命令，本方法执行完就关闭连接
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=name, password=key, timeout=300)
        stdin, stdout, stderr = client.exec_command(command)
        print(name + '#:'+command)
        for line in stdout:
            print(line.strip('\n'))
        client.close()
    except Exception as e:
        print(e)


def UpLoadFil(host,name,key,LocalFile,RemoteFile):#主机，登录名，登录密码，执行命令，本方法执行完就关闭连接
    try:
        client = paramiko.Transport(host)
        client.connect(username=name, password=key)
        sftp = paramiko.SFTPClient.from_transport(client)
        # sftp.put(loaclfile, remotefile)  # loaclfile是要上传的文件,remotefile是上传后要保存的文件名
        sftp.put(LocalFile, RemoteFile)
        sftp.close()
    except Exception as e:
        print(e)

# 测试
if __name__ == '__main__':
    remote=r'/root/FileTest77.sh'
    local=os.getcwd()+r'\LocalFile\Test.sh'
    UpLoadFil('45.63.20.37','root','D{7v$n@D$VEKMDBS',local,remote)