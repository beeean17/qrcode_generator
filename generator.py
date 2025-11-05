import qrcode

img = qrcode.make('https://www.seoultech.ac.kr/')
img.save('seoultech.png')
