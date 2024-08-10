import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img_text = "image/car1.jpg"
img = Image.open(img_text)
I1 = ImageDraw.Draw(img)

url = 'https://api.aiforthai.in.th/lpr-v2'
payload = {'crop' : '1','rotate':'1'}
file = {'image':open(img_text,'rb')}
headers = {'Apikey':'AaGkEYDzGKhjviguVDPr1HYdmbddM8om'}

response = requests.post(url,files = file, data = payload,headers=headers)
print(response.json())

#เขียนภาพ
data = response.json()
custamFont = ImageFont.truetype('font/KanitBold.ttf',65)
I1.text((10,10),""+data[0]['lpr'],font=custamFont,fill= (0,255,0))
img.save("Imagefortrain/result.jpg")