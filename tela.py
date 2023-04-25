from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'),sg.Input(key='Usuário',size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*',size=(20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window('Tela de Login', layout)

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos =='Entrar':
        if valores['Usuário'] == 'rafael' and valores['senha'] == '123456':
            print('Bem-vindo a Boca do Jaca!')




 