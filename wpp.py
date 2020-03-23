# sistema operacional: linux (debian 9)                                                                                *
# autor: fernando                                                                                                      *
# e-mail: fernando_bortotti@hotmail.com                                                                                *
# o quê programa faz? este programa manda mensagem automática pelo whatsapp usando uma lista de pessoas ou grupos.     *
# data: 22/03/2020                                                                                                     *
# navegador: google_chrome                                                                                             *
# driver necessário: ChromeDriver - WebDriver for Chrome na mesma pasta do programa                                    *
# nome: wpp.py                                                                                                         *
#***********************************************************************************************************************

#! /usb/bin/python3 
# -.- conding: utf-8 -.- 

# importar o time, pois ele é importante para não travar o navegador, pois podemos usar pausa para mandar as mensagens
import time

# importar o selenium
from selenium import webdriver

#vamos definir uma classe
class zap:
    # iniciando o selenium
    def __init__(self):
        #mensagem a ser enviada
        self.mensagem = "linux é vida!!"
        
        #lista de grupos ou pessoas que tu deseja enviar a mensagem
        self.grupos_ou_pessoas = ['nome_1','nome_2']
        
        #drive do google chrome
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=options) #nome do arquivo executável no chrome na pasta 
        # no meu caso o nome foi chromedriver
    
    # criando a função para enviar a mensagem
    def enviar(self):
        #abre a página da web 
        self.driver.get('https://web.whatsapp.com')
        
        #tempo de 40 para você logar com o qrcode no zap zap da web 
        time.sleep(40)
        
        # criando o laço para enviar a mensagem para sua lista de contato
        for grupo in self.grupos_ou_pessoas:
                usuario =self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(grupo))
                usuario.click()
                #
                msg_box = self.driver.find_element_by_class_name('_13mgZ')
                #
                msg_box.send_keys(self.mensagem)
                botao = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                time.sleep(3)
                botao.click()
auto = zap()
auto.enviar()
