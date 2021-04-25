#API_URL = "http://192.168.0.135:28081"
#API_URL="http://192.168.0.135:6080/"  #线上的135
#API_URL ='http://192.168.50.58:81'   #本地
API_URL ='http://192.168.0.135:6090/'
GY_DB_QA = {
    'host': '192.168.50.111',
    'port': 3306,
    'database': 'guoya_virtual_mall',
    'user': 'root',
    'password': 'swb@123456',
    'charset': 'utf8'
}

GY_EMAIL_QA = {
    'on_off': 'on',  # 邮件是否发生，on发送，off不发送
    'mail_host': 'smtp.126.com',  # 设置服务器
    'mail_user': 'wuling1105@126.com',  # 用户名
    'mail_pass': '126shouquanma',  # 口令
    'sender': 'wuling1105@126.com',
    'mail_port': 25,
    'receivers': ['wuling@guoyasoft.com', 'wuling1105@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
}
