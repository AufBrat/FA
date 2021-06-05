import socket
import os
import shutil


dirname = os.path.join(os.getcwd(), 'docs')
def process(req):
    global conn
    if req == 'pwd':
        return dirname
    elif req == 'ls':
        return '; '.join(os.listdir(dirname))
    elif req[:3] == 'cat':
        path = os.path.join(os.getcwd(), 'docs', req[4::])
        if os.path.exists(path):
            with open(path, 'r+') as f:
                line = ''
                for l in f:
                    line+=l
            return line
        else:
            return 'Такого файла не существет!'
    elif req[:5] == 'mkdir':
        path = os.path.join(os.getcwd(), 'docs', req[6::])
        if not os.path.exists(path):
            os.makedirs(path)
            return f'Папка создана.'
        else: 
            return 'Такая папка уже существет!'
    elif req[:5] == 'rmdir':
        path = os.path.join(os.getcwd(), 'docs', req[6::])
        if os.path.exists(path):
            shutil.rmtree(os.path.join(os.getcwd(), 'docs', req[6::]))
            return f'Папка удалена.'
        else:
            return 'Такой папки не существует!'
    elif req[:6]  == 'create':
        open(os.path.join(os.getcwd(), 'docs', req[7:]), 'tw', encoding='utf-8').close()
        return f'Файл создан.'
    elif req[:6]  == 'remove':
        os.remove(os.path.join(os.getcwd(), 'docs', req[7:]))
        return f'Файл удален.'
    elif req[:6]  == 'rename':
        req = req.split(' ')
        os.rename(os.path.join(os.getcwd(), 'docs', req[1]), os.path.join(os.getcwd(), 'docs', req[2]))
        return 'Файл переименован.'
    elif req[:4]  == 'copy':
        req = req.split(' ')
        shutil.copyfile(os.path.join(os.getcwd(), 'docs', req[1]), os.path.join(os.getcwd(), 'docs', req[2]))
        return 'Файл скопирован.'
    elif req.split(' ')[0] == 'get':																				#скачать текстовый файл
        if req.split(' ')[1] != '_eoc_':
            if os.path.exists(os.path.join(dirname,req.split(' ')[1])):
                if os.path.isfile(os.path.join(dirname,req.split(' ')[1])):
                    if '..' in req.split(' ')[1]:
                        return 'Не допускается использование ..'
                    with open(os.path.join(dirname,req.split(' ')[1]),'r',encoding='UTF-8') as f:
                        return 'success-!-!-!->'+f.read()
                else:
                    return 'Это не файл!'
            else:
                return 'Нет такого файла!'
        else:
            return 'Не введено название файла!'
    elif req.split(' ')[0] == 'push':																				#загрузить текстовый файл от клиента
        if req.split(' ')[1] != '_eoc_':
            if '..' in req.split(' ')[1] or '/' in req.split(' ')[1] or '\\' in req.split(' ')[1]:
                return 'Не допускается использование .. / \\'
            filecontent = conn.recv(1024)
            with open(os.path.join(dirname,req.split(' ')[1]),'w') as f:
                f.write(filecontent.decode())
            return 'Готово!'
    return 'bad request'

PORT = 6666

sock = socket.socket()
sock.bind(('', PORT))
sock.listen()
print("Прослушиваем порт: ", PORT)
while True:
    conn, addr = sock.accept()
    
    request = conn.recv(1024).decode()
    print(request)
    
    response = process(request)
    conn.send(response.encode())
conn.close()