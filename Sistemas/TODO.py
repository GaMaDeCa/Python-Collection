# Lista TODO - Gabriel Matheus de Castro


#>Uso:
#from TODO import TODO
#to=TODO() #Ou TODO.TODO()



#>Adicionando itens:
#to.add('1 kilo de frango')
#to.add('300 gramas de mussarela')
#to.add('10 tomates')

#>Ou tambem pode:
#to.add('1 kilo de frango','300 gramas de mussarela','10 tomates')

#>Removendo itens:
#to.remove(1)
#to.remove(0)
#to.remove(1,3,2)



#>Salvando lista(Exportando):
#to.exportarLista('lista_salva.txt')

#>Carregando lista(Importando):
#to.importarLista('lista_salva.txt')



#>Printar Lista:
#to.printTodo()

#>Printar Lista sem Checkboxes:
#to.printTodo(False)

#>Printar Lista Enumerada:
#to.printTodo(enumerado=True)

#>Printar Lista Com Titulo:
#to.printTodo(temTitulo=True,titulo='>MINHA LISTA TODO')

#>Printar Lista sem quebra de linha('\n'):
#to.printTodo(end='')



#>Mudar selecionado:
#to.setChecked(0,True)
#to.setChecked(1,True)

#>Autochecar ao adicionar item:
#to.setAutoCheck(True)



#>Outras Funcoes:
#add(*todo)
#remove(*i)
#setAutoCheck(boolean)
#setTituloPadrao(titulo)
#clearTituloPadrao()
#isChecked(i)
#setChecked(i,boolean)
#getLista()
#setLista(lista_todo)
#exportarLista(caminho,checkboxes=True,temTitulo=False,titulo='\n<----{LISTA TODO}---->\n',enumerado=False,end='\n')
#importarLista(caminho)
#todoGenerator(checkboxes,temTitulo,titulo,enumerado) #Use com o loop, for todo in todoGenerator(....
#printTodo(checkboxes=True,temTitulo=False,titulo='\n<----{LISTA TODO}---->\n',enumerado=False,end='\n')

class TODO:
    def __init__(self):
        self.lista_todo=[]
        self.titulo=None
        self.autocheck=False
    def add(self,*todo):
        if len(todo)==1:
            self.lista_todo.append([self.autocheck,todo[0]])
        else:
            for t in todo:
                self.lista_todo.append([self.autocheck,t])
    def remove(self,*i):
        if len(i)==1:
            self.lista_todo.pop(i[0])
        else:
            for n in i:
                self.lista_todo.pop(n)
    def setAutoCheck(self,boolean):
        self.autocheck=boolean
    def setTituloPadrao(self,titulo):
        self.titulo=titulo
    def clearTituloPadrao(self):
        self.titulo=None
    def isChecked(self,i):
        return self.lista_todo[i][0]
    def setChecked(self,i,boolean):
        self.lista_todo[i][0]=boolean
    def getLista(self):
        return self.lista_todo
    def setLista(self,lista_todo):
        self.lista_todo=lista_todo
    def exportarLista(self,caminho,checkboxes=True,temTitulo=False,titulo='\n<----{LISTA TODO}---->\n',enumerado=False,end='\n'):
        lista_string=''
        for todo in self.todoGenerator(checkboxes,temTitulo,titulo,enumerado):
            lista_string+=todo+end
        open(caminho,'a').write(lista_string)
    def importarLista(self,caminho):
        nova_lista_todo=[]
        enumerado=False
        com_checkboxes=False
        for linha in open(caminho,'r').readlines():
            chkbox1=linha.find('[X] ')
            chkbox2=linha.find('[ ] ')
            if linha.startswith('0 '):
                enumerado=True
            if chkbox1!=-1 or chkbox2!=-1:
                com_checkboxes=True
            formatado=linha[linha.find(' ')+1:] if enumerado else linha
            boolean=True if chkbox1!=-1 else False
            formatado=(boolean,(formatado.replace('[X] ','').replace('[ ] ','') if com_checkboxes else formatado).replace('\n',''))
            nova_lista_todo.append(formatado)
        self.lista_todo=nova_lista_todo
    def todoGenerator(self,checkboxes,temTitulo,titulo,enumerado):
        if temTitulo:
            yield titulo if self.titulo==None else self.titulo
        if checkboxes or enumerado:
            for i,todo in enumerate(self.lista_todo):
                yield f'{i if enumerado else ""}{" " if enumerado else ""}{"" if not checkboxes else "[X] " if todo[0] else "[ ] "}{todo[1]}'
        else:
            for todo in self.lista_todo:
                yield todo[1]
    def printTodo(self,checkboxes=True,temTitulo=False,titulo='\n<----{LISTA TODO}---->\n',enumerado=False,end='\n'):
        for todo in self.todoGenerator(checkboxes,temTitulo,titulo,enumerado):
            print(todo,end=end)
