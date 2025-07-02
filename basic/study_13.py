'''
python电子邮件发送
'''
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 创建邮件主体对象
email = MIMEMultipart()
# 设置发件人、收件人和主题
email['From'] = '郁涵艺-发件人'
email['To'] = '麒盛科技-收件人'
email['Subject'] = Header('当日新闻速报', 'utf-8')
# 添加邮件正文
content = """据德国媒体报道，当地时间9日，德国火车司机工会成员进行了投票，
定于当地时间10日起进行全国性罢工，货运交通方面的罢工已于当地时间10日19时开始。
此后，从11日凌晨2时到13日凌晨2时，德国全国范围内的客运和铁路基础设施将进行48小时的罢工。"""
email.attach(MIMEText(content, 'plain', 'utf-8'))

# 创建SMTP_SSL对象（连接邮件服务器）
smtp_obj = smtplib.SMTP_SSL('smtp.163.com', 465)
smtp_obj.login('13819353503@163.com', 'QEQrYTuLpLGpefMz')
smtp_obj.sendmail(
    '13819353503@163.com',
    ['1131270276@qq.com', 'hanyi.yu@keeson.com'],
    email.as_string()
)
