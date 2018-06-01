# 八皇后问题：要求在棋盘上放置8个皇后，并确保任何两个皇后都不能相互攻击

def conflict(state, nextX):
	nextX = len(state)
	for i in range(nextY):
		if abs(state[i] - nextX) in (0, nextY - i):
			return True
	return False

def queens(num, state):
	if len(state) == num - 1:
		for pos in range(num):
			if not conflict(state, pos):
				yield pos

