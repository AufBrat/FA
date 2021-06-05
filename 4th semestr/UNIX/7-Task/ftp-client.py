import socket
import os

HOST = 'localhost'
PORT = 6666


print('\nДля получения списка команд введите команду help.')
print('Для выхода введите команду exit.\n')

while True:
    request = input('>')
    if request == 'exit':
        print('Клиент закрыт.')
        break
	
    elif request == 'help':
        print('''
pwd - название рабочей директории
ls - содержимое текущей директории
cat <Название папки> - отправление содержимого файла
mkdir <Название папки> - создание новой папки
rmdir <Название папки> - удаление папки
create <Название файла> - создание файла
remove <Название файла> - удаление файла
rename <Название файла> - изменение названия файла
copy <Название файла> <Название нового файла> - копирование файла
get <Название файла> - скачивание файла с сервера
push <Название файла> - загрузка файла на сервер 
exit - закрытие клиента
help - помощь
''')
    else:
        sock = socket.socket()
        sock.connect((HOST, PORT))
        if request.split(' ')[0] == 'push':
            request+=' _eoc_'
            if request.split(' ')[1] != '_eoc_':
                if '..' in request.split(' ')[1] or '/' in request.split(' ')[1] or '\\' in request.split(' ')[1]:
                    print('Не допускается использование .. / \\')
                else:
                    if os.path.exists(request.split(' ')[1]):
                        if os.path.isfile(request.split(' ')[1]):
                            sock.send(request.encode())
                            with open(request.split(' ')[1],'r') as f:
                                forsend = f.read().encode()
                            sock.send(forsend)
                            answer = sock.recv(1024)
                            print(answer.decode())
                        else:
                            print('Это не файл!')
                    else:
                        print('Такого файла нет!')
            else:
                print('Вы забыли ввести название файла!')

        else:
            sock.send(request.encode())
            response = sock.recv(1024).decode()
            if request.split(' ')[0] == 'get':
                if response.split('-!-!-!->')[0] == 'success':
                    with open(request.split(' ')[1],'w') as f:
                        f.write(response.split('-!-!-!->')[1])
                    print('Готово!')
                else:
                    print(response)
            else:
                print(response)
        
        
        sock.close()