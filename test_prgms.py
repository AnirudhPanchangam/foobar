import knight_soln
import knight_moves




for i in range(64):
	for j in range(64):
		x = knight_moves.answer(i, j)
		y = knight_soln.answer(i, j)
		if x != y:
			print("answers do not match")
			print(i,j)
			print(x,y)