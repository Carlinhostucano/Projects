from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.geometry('390x453')
janela.resizable(width=False, height=False)
cor = '#33353d'
janela.config(bg=cor)
janela.iconbitmap('calculadora.ico')
janela.title('Calculadora')

frame_cima = Frame(janela, bg='black', relief='solid')
frame_cima.place(x=0, y=0, height=100, width=390)
frame_baixo = Frame(janela, relief='solid')
frame_baixo.place(x=0, y=101, height=353, width=390)


def addnum(num):
    sinais = (mais, menos, mult, div, potencia, raiz)
    for sinal in sinais:
        if sinal['bg'] == 'white':
            sinal['bg'] = 'orange'
            sinal['fg'] = 'white'
            display['text'] = ''
    match display['text']:
        case '0':
            display['text'] = num
            conta['text'] = num
        case _:
            display['text'] += num
            conta['text'] += num

def addsimb(simb):
    match simb:
        case ',':
            conta['text'] +='.'
            display['text'] +=','
        case '(':
            if conta['text'][:-1] == range(0,10):
                messagebox.showerror('Erro de sintaxe', 'Por favor, insira um operador antes de abrir os parênteses.')
            else:
                conta['text'] +='('
                abre['bg'] = 'white'
                abre['fg'] = 'black'
        case ')':
            if (mais['bg'] == 'white' or menos['bg'] == 'white' or mult['bg'] == 'white'
                    or div['bg'] == 'white' or raiz['bg'] == 'white' or potencia['bg'] == 'white' or '.' == conta['text'][:-1] or '(' == conta['text'][:-1]):
                messagebox.showerror('Falha ao fechar parênteses', 'Não foi possível fechar os parênteses.')
            else:
                if statraiz['text'] == 'aberto':
                    conta['text'] += ')'
                    statraiz['text'] = 'fechado'
                conta['text'] += ')'
                if conta['text'].count('(') == conta['text'].count(')'):
                    abre['bg'] = 'orange'
                    abre['fg'] = 'white'
        case '+':
            if mais['bg'] == 'white' or menos['bg'] == 'white' or mult['bg'] == 'white' or div['bg'] == 'white' or potencia['bg'] == 'white' or raiz['bg'] == 'white' or '(' == conta['text'][:-1]:
                messagebox.showerror('Falha ao adicionar sinal', 'Não foi possível adicionar o sinal.')
            else:
                if statraiz['text'] == 'aberto':
                    conta['text'] += ')'
                    statraiz['text'] = 'fechado'
                conta['text'] +='+'
                mais['bg'] = 'white'
                mais['fg'] = 'black'
        case '-':
            if mais['bg'] == 'white' or menos['bg'] == 'white' or mult['bg'] == 'white' or div['bg'] == 'white' or potencia['bg'] == 'white' or raiz['bg'] == 'white':
                messagebox.showerror('Falha ao adicionar sinal', 'Não foi possível adicionar o sinal.')
            else:
                if statraiz['text'] == 'aberto':
                    conta['text'] += ')'
                    statraiz['text'] = 'fechado'
                conta['text'] += '-'
                menos['bg'] = 'white'
                menos['fg'] = 'black'
        case '*':
            if mais['bg'] == 'white' or mult['bg'] == 'white' or div['bg'] == 'white' or potencia['bg'] == 'white' or raiz['bg'] == 'white' or '(' == conta['text'][:-1]:
                messagebox.showerror('Falha ao adicionar sinal', 'Não foi possível adicionar o sinal.')
            else:
                if statraiz['text'] == 'aberto':
                    conta['text'] += ')'
                    statraiz['text'] = 'fechado'
                conta['text'] += '*'
                mult['bg'] = 'white'
                mult['fg'] = 'black'
        case '/':
            if statraiz['text'] == 'aberto':
                conta['text'] += ')'
                statraiz['text'] = 'fechado'
            if mais['bg'] == 'white' or mult['bg'] == 'white' or div['bg'] == 'white' or potencia['bg'] == 'white' or raiz['bg'] == 'white' or '(' == conta['text'][:-1]:
                messagebox.showerror('Falha ao adicionar sinal', 'Não foi possível adicionar o sinal.')
            else:
                conta['text'] += '/'
                div['bg'] = 'white'
                div['fg'] = 'black'
        case 'raiz':
            if statraiz['text'] == 'aberto':
                conta['text'] += ')'
                statraiz['text'] = 'fechado'
            if mais['bg'] == 'white' or mult['bg'] == 'white' or div['bg'] == 'white' or potencia['bg'] == 'white' or raiz['bg'] == 'white' or '(' == conta['text'][:-1]:
                messagebox.showerror('Falha ao adicionar sinal', 'Não foi possível adicionar o sinal.')
            else:
                conta['text'] += '**(1/'
                statraiz['text'] = 'aberto'
                raiz['bg'] = 'white'
                raiz['fg'] = 'black'
        case'potencia':
            if statraiz['text'] == 'aberto':
                conta['text'] += ')'
                statraiz['text'] = 'fechado'
            if mais['bg'] == 'white' or mult['bg'] == 'white' or div['bg'] == 'white' or potencia['bg'] == 'white' or raiz['bg'] == 'white' or '(' == conta['text'][:-1]:
                messagebox.showerror('Falha ao adicionar sinal', 'Não foi possível adicionar o sinal.')
            else:
                conta['text'] += '**'
                potencia['bg'] = 'white'
                potencia['fg'] = 'black'
def clear():
    conta['text'] = '0'
    display['text'] = '0'
    sinais = (mais, menos, mult, div, potencia, raiz, abre, fecha)
    for sinal in sinais:
        sinal['bg'] = 'orange'
        sinal['fg'] = 'white'
def umadd():
    addnum('1')
def doisadd():
    addnum('2')
def tresadd():
    addnum('3')
def quatroadd():
    addnum('4')
def cincoadd():
    addnum('5')
def seisadd():
    addnum('6')
def seteadd():
    addnum('7')
def oitoadd():
    addnum('8')
def noveadd():
    addnum('9')
def zeroadd():
    addnum('0')

def maisadd():
    addsimb('+')
def menosadd():
    addsimb('-')
def multadd():
    addsimb('*')
def divadd():
    addsimb('/')
def potadd():
    addsimb('potencia')
def abreadd():
    addsimb('(')
def fechaadd():
    addsimb(')')
def raizadd():
    addsimb('raiz')
def virguladd():
    addsimb(',')

def go():
    sinais = (mais, menos, mult, div, potencia, raiz)
    val = 0
    for i, v in enumerate(sinais):
        if v['bg'] == 'white':
            if val == 0:
                messagebox.showerror('Erro de sintaxe', f'Você não informou parâmetros para o sinal <{v}>. Por favor, insira um valor e tente novamente.')
                val = 1
        else:
            val = 0
    for n in range(0, conta['text'].count('(1/')):
        if statraiz['text'] == 'aberto':
            conta['text'] += ')'
            statraiz['text'] = 'fechado'
    if val == 0:
        if conta['text'].count('(') == conta['text'].count(')'):
            try:
                resul = str(eval(conta['text'])).replace('.', ',')
                conta['text'] = resul
                display['text'] = resul
            except:
                messagebox.showerror('Erro espontâneo', 'Ops! Um erro inesperado apareceu! Sentimos muito.')

    else:
        messagebox.showerror('Falha ao dar o resultado', 'Por favor, feche todos os parênteses antes de finalizar a conta.')


statraiz = Label(janela, text='fechado')
conta = Label(janela, text='0')
um = Button(frame_baixo, text='1', relief='solid', command=umadd, font='Arial 20 bold', bg=cor, fg='white', width=4, height=2)
dois = Button(frame_baixo, text='2', relief='solid', command=doisadd, font='Arial 20 bold', bg=cor, fg='white', width=4, height=2)
tres = Button(frame_baixo, text='3', relief='solid', command=tresadd, font='Arial 20 bold', bg=cor, fg='white', width=4, height=2)
quatro = Button(frame_baixo, text='4', relief='solid', command=quatroadd, font='Arial 20 bold', bg=cor, fg='white', width=4, height=2)
cinco = Button(frame_baixo, text='5', relief='solid', command=cincoadd, font='Arial 20 bold', bg=cor, fg='white', width=4, height=2)
seis = Button(frame_baixo, text='6', relief='solid', command=seisadd, font='Arial 20 bold', bg=cor, fg='white', width=4, height=2)
sete = Button(frame_baixo, text='7', relief='solid', command=seteadd, font='Arial 20 bold', bg=cor, fg='white', width=4, height=2)
oito = Button(frame_baixo, text='8', relief='solid', command=oitoadd, font='Arial 20 bold', bg=cor, fg='white', width=4, height=2)
nove = Button(frame_baixo, text='9', relief='solid', command=noveadd, font='Arial 20 bold', bg=cor, fg='white', width=4, height=2)
zero = Button(frame_baixo, text='0', relief='solid', command=zeroadd, font='Arial 20 bold', bg=cor, fg='white', width=4, height=2)
virgula = Button(frame_baixo, text=',', relief='solid', command=virguladd, font='Arial 20 bold', bg=cor, fg='white', width=4, height=2)
mais = Button(frame_baixo, text='+', relief='solid', command=maisadd, font='Arial 20 bold', bg='orange', fg='white', width=4, height=2)
menos = Button(frame_baixo, text='-', relief='solid', command=menosadd, font='Arial 20 bold', bg='orange', fg='white', width=4, height=2)
mult = Button(frame_baixo, text='x', relief='solid', command=multadd, font='Arial 20 bold', bg='orange', fg='white', width=4, height=2)
div = Button(frame_baixo, text='÷', relief='solid', command=divadd, font='Arial 20 bold', bg='orange', fg='white', width=4, height=2)
abre = Button(frame_baixo, text='(', relief='solid', command=abreadd, font='Arial 20 bold', bg='orange', fg='white', width=4, height=2)
fecha = Button(frame_baixo, text=')', relief='solid', command=fechaadd, font='Arial 20 bold', bg='orange', fg='white', width=4, height=2)
potencia = Button(frame_baixo, text='x ^ y', relief='solid', command=potadd, font='Arial 20 bold', bg='orange', fg='white', width=4, height=2)
raiz = Button(frame_baixo, text='x √ y', relief='solid', command=raizadd, font='Arial 20 bold', bg='orange', fg='white', width=4, height=2)
igual = Button(frame_baixo, text='=', relief='solid', command=go, font='Arial 20 bold', bg=cor, fg='white', width=4, height=2)

um.grid(row=0, column=0)
dois.grid(row=0, column=1)
tres.grid(row=0, column=2)
mais.grid(row=0, column=3)
menos.grid(row=0, column=4)
mult.grid(row=1, column=3)
div.grid(row=1, column=4)
quatro.grid(row=1, column=0)
cinco.grid(row=1, column=1)
seis.grid(row=1, column=2)
sete.grid(row=2, column=0)
oito.grid(row=2, column=1)
nove.grid(row=2, column=2)
zero.grid(row=3, column=1)
virgula.grid(row=3, column=0)
igual.grid(row=3, column=2)
abre.grid(row=2, column=3)
fecha.grid(row=2, column=4)
potencia.grid(row=3, column=3)
raiz.grid(row=3, column=4)

ce = Button(frame_cima, text='CE', command=clear, relief='solid', font='Arial 20 bold', bg='orange', fg='white')
ce.place(x=0, y=0, width=78, height=100)
display = Label(frame_cima, relief='solid', font='Arial 20 bold', bg='black', fg='white', anchor=E, text='0')
display.place(x=78, y=0, height=100, width=302)

janela.mainloop()
