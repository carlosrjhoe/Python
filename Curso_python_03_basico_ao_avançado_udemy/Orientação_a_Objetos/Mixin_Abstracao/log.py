# Abstração
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        self._log(f'Error: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        print(f'{msg} - {self.__class__.__name__}')


if __name__ == '__main__':
    l = LogFileMixin()
    l._log('Olá, bom dia..')