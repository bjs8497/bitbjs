import pyupbit

access = "QAk4meXx8nbgyb1ui2LnBweaehs4nLOvwipHWrID"          # 본인 값으로 변경
secret = "Mv5xDeikxr1C2i948sPpSZn9jQYJqs3e2JUxnxI8"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회