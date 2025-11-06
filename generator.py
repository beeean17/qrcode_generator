import qrcode

#version: QR 코드 크기 (1-40)
#
#1: 21x21
#40: 177x177
#None: 자동으로 데이터에 맞게 조정
#rror_correction: 오류 복구 수준

#ERROR_CORRECT_L: ~7% 복구
#ERROR_CORRECT_M: ~15% 복구 (기본값)
#ERROR_CORRECT_Q: ~25% 복구
#ERROR_CORRECT_H: ~30% 복구
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

URL = 'http://158.179.162.196/'  # 생성 사이트 링크
IMG_Name = "chart"  # 파일 이름
IMG_Type = "png"  # 파일 형식

qr.add_data(URL)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{IMG_Name}.{IMG_Type}")