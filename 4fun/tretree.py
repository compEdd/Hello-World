###Retornar uma arvore criada pela multiplicação em pares de '1...1'

#Aceita apenas valores que contenham 1 em toda sua constituição
#fail=controlar a entrada '1...1'

def prnt_tree(var):
	varl = str(var)
	vars = var*var
	if "1" in varl[:]:
		print(vars)
	else:
		print('Not "1...1"')

#Usa a função prnt para gera sequências ascendentes de lan(var)
def mnt_tree(var):
	mt = len(str(var))
	vadd = var
	for mt in range(mt):
		prnt_tree(int(vadd))
		vadd = str(vadd) + "1"
	print("-"*mt + "The tree" + "-"*mt)

def cplt_tree(var):
	input = len(str(var*var))
	prnt = len(str(prnt_tree(var)))
	varw = 1

	while input >= prnt:
		input = len(str(prnt_tree(int(varw))))
		prnt_tree(int(varw))
		varw = str(varw) + '1'
	print('end')
