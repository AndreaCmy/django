import  qrcode
import time
from io import  StringIO
from django.http import HttpResponse

# Create your views here.
def generate_qrcode(request, data):
   # qrcode.run_example(data)
   #参数配置
   qr = qrcode.QRCode( version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
                )
   #网页 或者 文字
   qr.add_data(data)
  #生成图片
   im = qr.make_image()
   img_file = r'D:\py_qrcode.png'
   #保存地址
   im.save(img_file)
   #显示二维码
   im.show()
   response = HttpResponse("我的第一个简单的python django项目.")

   return response
