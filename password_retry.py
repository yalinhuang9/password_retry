password = 'a123456'
x = 2
while x >= 0: 
	key = input('請輸入密碼:')
	if key == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤！還有',x,'次機會')
		x = x - 1