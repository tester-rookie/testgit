import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.1.245.111', port=22022, username='gsv8app', password='gsv8app')
# 执行命令
# stdin, stdout, stderr = ssh.exec_command(r'cd $LOGPATH/rating/test/rat_gprs_xiaodh3/')
stdin, stdout, stderr = ssh.exec_command(r'ls -ll')

# 获取命令结果
result = stdout.read()
print(result)
# 关闭连接
ssh.close()
