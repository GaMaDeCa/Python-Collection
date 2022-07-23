import socket

def socketGetRequest(site,porta=80,recv_size=4092):
    soquete=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    soquete.connect((site, 80))
    soquete.sendall(f'GET / HTTP/2\r\nHost: {site}\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; rv:102.0) Gecko/20100101 Firefox/102.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'.encode())
    return soquete.recv(recv_size)

nome_do_host=socket.gethostname()
endereco_ip_local=socket.gethostbyname(hostname)

print(f"Hostname: {nome_do_host}\nIP Local: {endereco_ip_local}\nIP Externo: {socketGetRequest('www.ident.me')[::-1].split(b'\n')[0][::-1]}")
