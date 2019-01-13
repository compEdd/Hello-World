def right_justify(monty):
	inln = len(monty)
	fxln = 70 - inln
	just = ' ' * fxln + monty
	print(just)
