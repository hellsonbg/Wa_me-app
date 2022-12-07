import time
import PySimpleGUI as sg
from PySimpleGUI import Column
from PySimpleGUI import Push
import webbrowser
from images import *


#variavel que guarda o telefone informado
wp='0'

ddd_val = ['27','11','12','13','14','15','16','17','18',
'19','21','22','24','27','28','31','32','33','34','35',
'37','38','41','42','43','44','45','46','47','48','49',
'51','53','54','55','61','62','63','64','65','66','67',
'68','69','71','73','74','75','77','79','81','82','83',
'84','85','86','87','88','89','91','92','93','94','95',
'96','97','98','99']

#tema de cores do app
sg.change_look_and_feel('DarkGreen5')
font2 = ("Arial", 7)
while True:

    

    #layout imagem da janela principal
    layout_esq =[[Push(),sg.Image(filename='wpp.png'),Push()],
    [Push(),sg.Text(' Github   ➜',font=font2),sg.Button(image_data=github_png,key=("-LINK-"),button_color=(sg.theme_background_color()),border_width=0,size=(4,4)),Push()]]
    #layout da input dados
    layout_dir=[
    [Push(),sg.Text("Insira o Telefone:"),Push()],
    [],
    [sg.Text('DDD:',size=(4,0)),sg.Input(size=(2,0),key=("-DDD-"),enable_events=True),sg.Text('Tel:'),sg.Input(size=(9,0),key=("-TEL-"),enable_events=True),sg.Button("OK",key=("-SUBMIT-"),button_color='green'),sg.Button("SAIR",key=("-CANCEL-"),button_color='red')],
    
    
    
    
    ]


    #layout janela principal
    layout = [[Column(layout_esq),Column(layout_dir)]]


    
    #janela principal
    janela = sg.Window("wpp_me",layout=layout)
   
    

    tela = janela

    while True:
        
        event, values = tela.read()

######## tratamento do input do telefone e DDD

        if event == '-DDD-' and values['-DDD-'] and values['-DDD-'][-1] not in ('0123456789'):
            janela['-DDD-'].update(values['-DDD-'][:-1])

            if event == '-DDD-' and len(values['-DDD-']) >2:
                janela['-DDD-'].update(values['-DDD-'][:-1]) 

        if event == '-TEL-' and values['-TEL-'] and values['-TEL-'][-1] not in ('0123456789'):
            janela['-TEL-'].update(values['-TEL-'][:-1]) 

            if event == '-TEL-' and len(values['-TEL-']) >9:
                janela['-TEL-'].update(values['-TEL-'][:-1])

        if event == '-TEL-' and len(values['-TEL-']) >9:
                janela['-TEL-'].update(values['-TEL-'][:-1])

        if event == '-DDD-' and len(values['-DDD-']) >2:
                janela['-DDD-'].update(values['-DDD-'][:-1])
########

        if event in ("-LINK-"):
            webbrowser.open('https://github.com/hellsonbg', new=1)

        if event in(sg.WIN_CLOSED,"-CANCEL-"):
            janela.close()
            break
        if event == "-SUBMIT-":

            #extrair dados da tela
            tel = values["-TEL-"]
            ddd = values["-DDD-"]
            cd = "55"#declara código 55 para o telefone padrão 
            tel_com = cd+ddd+tel
            wp = tel_com #colocando o telefone completo na variavel
            link = "https://wa.me/{}".format(wp)#ajustando o link

            #variaveis que guardam a validação para os números informados após apertar ok 
            validacao = 0
            validacao_ddd = 0
            validacao_tel = 0
            
            while True:
                
                if values["-DDD-"] in ddd_val: #verifica se o DDD está cadastrado no banco de dados
                    validacao_ddd = 1
                if len(tel) == 9 and not 0:#verifica se o Tel tem digitos o suficiente
                    validacao_tel = 1
                if validacao_tel and validacao_ddd == 1: #guarda na variavel de validação se todos os requisitos foram cumpridos
                    validacao = 1
                
                break
            
            if validacao == 0: #se os requisitos não forem cumpridos, dá o aviso do que não está de acordo
                error_message = ''
                if validacao_tel == 0:
                    error_message += "Digite um número válido!"
                if validacao_ddd == 0:
                    error_message += "\nDigite um DDD válido!"
                sg.popup_no_buttons(error_message)

            if validacao == 1: #se tudo preencheu aos requisitos, abre o navegador padrão com o link para a conversa no número digitado
                
                sg.popup_auto_close("executando comandos...",auto_close_duration=1,button_type=5)
                webbrowser.open(link, new=1)
                sg.popup_auto_close("Pronto, comandos concluídos!!",auto_close_duration =1,button_type=5)
                janela.close()
                break
    break
         
        
    
