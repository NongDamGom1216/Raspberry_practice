# 아날로그 SPI 통신

import spidev
import time

# 딜레이 시간(센서 측정 간격)
delay = 0.5

# MCP3008 채널 중 센서에 연결한 채널 설정
pot_channel = 0

# SPI 인스턴스 spi 생성
spi = spidev.SpiDev()

# SPI 통신 시작하기
spi.open(0, 0)

# SPI통신 속도 설정
spi.max_speed_hz = 100000

#0~7 까지 8개의 채널에서 SPI 데이터 읽기
def readadc(adcnum):
    if adcnum < 0 or adcnum > 7:
        return -1

    r = spi.xfer2([1, 8+adcnum <<4, 0]) # 요청 값 리턴
    # << 는 비트 shift 연산자
    # 예를 들어 <<4 는 00000011 -> 00110000
    data = ((r[1] & 3) << 8) + r[2] # 10비트 해석
    # 여기서 3은 00000011
    # r[1] = xxxxxxxx
    # r[1] & 3 = 000000xx
    # (r[1] & 3) << 8 = 000000xx 00000000 여기서 r[2] 더하면 000000xx xxxxxxxx
    # 총 10비트의 값이 데이터로 들어간다

    return data

while True:
    # readadc 함수로 pot_channel의 SPI 데이터를 읽기
    pot_value = readadc(pot_channel)
    print("---------------------------")
    print("LDR value: %d" % pot_value)
    time.sleep(delay)
