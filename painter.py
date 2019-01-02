import json, requests

delta_x = 100 # set to move the picture
delta_y = 100 # real_x = gived_x + delta_x

headers = {
	'referer': 'https://www.luogu.org/paintBoard',
	'User-agent': 'wxw_ak_ioi'
}

cookies = { '__client_id': '', '_uid': '' }

def get_real_color(c):
	if len(c) > 1:
		return int(c)
	if ord(c) >= ord('a'):
		return ord(c) - ord('a') + 10
	else:
		return ord(c) - ord('0')

class info:
	def __init__(self, x, y, c):
		self.x = int(x) + delta_x
		self.y = int(y) + delta_y
		self.c = get_real_color(c)

def requests_get(url):
	while True:
		try:
			req = requests.get(url, verify=False,
			headers=headers, cookies=cookies, timeout=10)
		except:
			pass
		break
	return req

def requests_post(url, data=None):
	while True:
		try:
			req = requests.post(url, verify=False,
			headers=headers, cookies=cookies, data=data, timeout=10)
		except:
			pass
		break
	return req

def get_board():
	request = requests_get('https://www.luogu.org/paintBoard/board')
	with open('board.out', 'wb+') as file:
		file.write(request.content)
		file.close()
	content = request.content.decode('ascii').split('\n')
	board = []
	for i in range(0, 800):
		line = []
		for j in range(0, 400):
			color = content[i][j]
			line.append(color)
			# print(i, j, point)
		board.append(line)
	return board

def paint(x, y, color):
	data = { 'x': x, 'y': y, 'color': color }
	request = requests_post('https://www.luogu.org/paintBoard/paint', data)
	status = json.loads(request.content)['status']
	if status == 200:
		print('[200] Success by', cookies['_uid'], '!')
		return True
	elif status == 401:
		print('[401] Not login. (', cookies['_uid'], ')')
	elif status == 500:
		# print('[500] Please wait for trying again.')
		pass
	else:
		print('[???] Unknown error.')
	return False

def get_todo():
	content = open('todo.list', 'r+').read()
	todolist = []
	for line in content.split('\n'):
		if len(line.split(' ')) < 3:
			continue
		x, y, c = line.split(' ')
		todolist.append(info(x, y, c))
	return todolist

def get_cookies():
	content = open('cookies.list', 'r+').read()
	cookies_list = []
	for line in content.split('\n'):
		cookies = {}
		if len(line.split(' ')) < 2:
			continue
		cookies['__client_id'], cookies['_uid'] = line.split(' ')
		cookies_list.append(cookies)
	return cookies_list

def clear_todo(todolist):
	board = get_board()
	answer = []
	for todo in todolist:
		if get_real_color(board[todo.x][todo.y]) != todo.c:
			answer.append(todo)
	return answer

def check(x, y, color):
	board = get_board()
	now_color = get_real_color(board[x][y])
	if color == now_color:
		return True
	else:
		return False

if __name__ == '__main__':
	while True:

		todolist = clear_todo(get_todo())
		cookies_list = get_cookies()
		if len(todolist):
			print('length of todolist is', len(todolist))
		else:
			print('nothing to do.')

		for todo in todolist:
			print('todo (', todo.x, ',', todo.y, ') to', todo.c)
			try:
				success = check(todo.x, todo.y, todo.c)
				while not success:
					# print('paint (', todo.x, ',', todo.y, ') to', todo.c)
					for user in cookies_list:
						cookies = user
						success = paint(todo.x, todo.y, todo.c)
						if success:
							break
			except:
				print('error')
