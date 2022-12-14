### ENGLISH

# Dopy

_A Python app to automate repetitive tasks._

<!--step0-->

Are you tired of opening the same folders, the same programs and the same files every day?

Tired of having to open the same browser tabs, type in the same logins and passwords, and answer the same emails every day?

Well, I have a solution for you: Dopy!

Dopy is an application written in Python that does the heavy lifting for you.

On the first launch, just inform what you want to open, in the desired order. Next time, press 'Executar automação' button and the program will open what you asked for, without complaining. Simple and easy!

**Note: Dopy is on an early stage of development, right now it can autostart files, folders and applications, as well open tabs on browser.**

## Requirements

1. Windows 10 or 11 (you don't need to install Python to run this program!)
2. Unfortunately, I haven't had time to create a Linux or Mac version yet, but it's in the plans, stay tuned for updates!

## Installation/Configuration

1. Download the latest rar file ("Dopy.rar") on [Releases](https://github.com/renanleitev/dopy/releases), extract and execute the "Dopy.exe" app located in Dopy/dist.
2. Optional: If you have Python installed, just run the "dopy_final.py" script located in the main folder (latest release).
3. Follow the instructions on the screen, it will ask about what you want to open (files, folders, documents, musics, videos, programs...).
4. After the setup, press 'Executar automação' and reopen to start the automatization.
5. Grab some coffee and wait the program to finish the job :)

## Changing the configuration file

1. After the first run, two files will be generated in Dopy/dist: "listaprograma.txt" (for programs) and "listasite.txt" (for websites).
2. You can edit the order of programs/websites using Dopy, but feel free to edit the files if you wish. 
3. Programs: to change the order of events or even change what will be opened, open "listaprograma.txt" and change the category (folder, music, documents) or the name of the program/file/folder.
4. Sites: open "listaprograma.txt", to change which browser will be opened, just change the browser name (leave "application:" text intact); to modify the order of the sites or even change the name of the site, change the name of the sites below the browser name.
5. Optional: You can delete "listaprograma.txt" or "listasite.txt" and open "Dopy.exe" again to generate another configuration file.

## Roadmap

1. <s>Add an option to autostart browser tabs, while opening other applications, files and folders.</s> DONE!
2. Add an option to autostart browser tabs, input information (login and password) and access your account.
3. Add an option to autostart a file (docx, xlsx, csv), input information (text, image or link), save and close the file.
4. Add an option to autostart a file (docx, xlsx, csv), copy information (text, image or link) and send that to email.
5. <s>Add a GUI (user interface), with PyQt or Tkinter.</s> DONE!
6. Add more options (suggestions are welcome!)

*Under development...*

---

### PORTUGUÊS

# Dopy

_Uma aplicação em Python para resolver tarefas repetivas._

Você está cansado de abrir as mesmas pastas, os mesmos programas e os mesmos arquivos todos os dias?

Cansado de ter que abrir as mesmas abas do navegador, digitar os mesmos logins e senhas e responder os mesmos e-mails todos os dias?

Bem, eu tenho uma solução para você: Dopy!

Dopy é um aplicativo escrito em Python que faz o trabalho pesado para você.

Na primeira inicialização, basta informar o que deseja abrir, na ordem desejada. Da próxima vez, basta apertar o botão 'Executar automação' e o programa vai abrir o que você pediu, sem reclamar. Simples e fácil!

**Observação: Dopy está em estágio inicial de desenvolvimento, neste momento pode iniciar automaticamente arquivos, pastas e aplicativos, bem como abrir abas no navegador.**

## Requisitos

1. Windows 10 ou 11 (você não precisa instalar o Python para executar este programa!)
2. Infelizmente ainda não tive tempo de criar uma versão para Linux ou Mac, mas está nos planos, fique atento às atualizações!

## Instalação/Configuração

1. Baixe o arquivo rar ("Dopy.rar") em [Releases](https://github.com/renanleitev/dopy/releases), extraia e execute o aplicativo "Dopy.exe" localizado em Dopy/dist.
2. Opcional: Se você tiver o Python instalado, basta executar o script "dopy_final.py" localizado na pasta principal (última versão).
3. Siga as instruções na tela, ele perguntará sobre o que você deseja abrir (arquivos, pastas, documentos, músicas, vídeos, programas...).
4. Após a configuração, pressione o botão "Executar automação" para iniciar a automatização.
5. Pegue um café e espere o programa terminar o trabalho :)

## Alterando o arquivo de configuração

1. Após a primeira execução, dois arquivos serão gerados em Dopy/dist: "listaprograma.txt" (para programas) e "listasite.txt" (para sites).
2. Você pode editar a ordem dos programas/sites usando o Dopy, mas fique à vontade para editar os arquivos se desejar.
3. Programas: para alterar a ordem dos eventos ou mesmo alterar o que será aberto, abra "listaprograma.txt" e altere a categoria (pasta, música, documentos) ou o nome do programa/arquivo/pasta.
4. Sites: abra "listaprograma.txt", para alterar qual navegador será aberto, altere apenas o nome do navegador (deixe o texto "aplicativo:" intacto); para modificar a ordem dos sites ou mesmo alterar o nome do site, altere o nome dos sites abaixo do nome do navegador.
5. Opcional: Você pode excluir "listaprograma.txt" ou "listasite.txt" e abrir "Dopy.exe" novamente para gerar outro arquivo de configuração.

## Próximas atualizações

1. <s>Adicionar uma opção para iniciar automaticamente as guias do navegador, enquanto abre outros aplicativos, arquivos e pastas.</s> FEITO!
2. Adicionar uma opção para iniciar automaticamente as guias do navegador, inserir informações (login e senha) e acessar a sua conta.
3. Adicionar uma opção para iniciar automaticamente um arquivo (docx, xlsx, csv), inserir informações (texto, imagem ou link), salvar e fechar o arquivo.
4. Adicionar uma opção para iniciar automaticamente um arquivo (docx, xlsx, csv), copiar informações (texto, imagem ou link) e enviar para e-mail.
5. <s>Adicionar uma GUI (interface de usuário), com PyQt ou Tkinter.</s> FEITO!
6. Adicionar mais opções (sugestões são bem-vindas!)

*Em desenvolvimento...*
