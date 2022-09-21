from importlib.resources import contents
import io
import sys
import urllib.request as request

def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO('dados.zip', mode='w')
    
    content_length = response.getheader('Content-length')
    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)
    
    response.closed()
    out_file.closed()
    print('Finalizado')
    
if __name__ == '__main__':
    main()
