class ExtratorArgumentoUrl:
    def __init__(self, url):
        if self.url_eh_valida(url):
            self.url = url
        else:
            raise LookupError('Url inválida!')

    @staticmethod
    def url_eh_valida(url):
        if url:
            return True
        else:
            return False