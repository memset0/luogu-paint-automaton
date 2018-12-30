import json, requests

delta_x = 100 # set to move the picture
delta_y = 100 # real_x = gived_x + delta_x

headers = {
	'referer': 'https://www.luogu.org/paintBoard',
	'User-agent': 'wxw_ak_ioi'
}

cookies = { '__client_id': '', '_uid': '' }
user_list = [
	{
		'__client_id': '****************************************', # Do not show it to others
		'_uid': '*****' # enter your own user id
	},
	{
		'__client_id': '****************************************',
		'_uid': '*****'
	}
]	

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

def get_board():
	request = requests.get('https://www.luogu.org/paintBoard/board', verify=False, headers=headers, cookies=cookies)
	with open('board.out', 'wb+') as file:
		file.write(request.content)
		file.close()
	content = str(request.content).split('\\n')
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
	request = requests.post('https://www.luogu.org/paintBoard/paint', verify=False, headers=headers, cookies=cookies, data=data)
	status = json.loads(request.content)['status']
	if status == 200:
		print('[200] Success by', cookies['_uid'], '!')
	elif status == 401:
		print('[401] Not login.')
	elif status == 500:
		print('[500] Please wait for trying again.')
	else:
		print('[???] Unknown error.')

def get_todo():
	content = open('todo.list', 'r+').read()
	todolist = []
	for line in content.split('\n'):
		if len(line.split(' ')) < 3:
			continue
		x, y, c = line.split(' ')
		todolist.append(info(x, y, c))
	return todolist

def check(x, y, color):
	board = get_board()
	now_color = get_real_color(board[x][y])
	if color == now_color:
		return True
	else:
		return False

while True:
	todolist = get_todo()
	for todo in todolist:
		print('todo (', todo.x, ',', todo.y, ') to', todo.c)
		try:
			while not check(todo.x, todo.y, todo.c):
				print('paint (', todo.x, ',', todo.y, ') to', todo.c)
				for user in user_list:
					cookies = user
					paint(todo.x, todo.y, todo.c)
					if check(todo.x, todo.y, todo.c):
						break
		except:
			print('error')
