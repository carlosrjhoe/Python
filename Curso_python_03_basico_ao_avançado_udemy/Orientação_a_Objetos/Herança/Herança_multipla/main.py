from login import Log, LogFileMixin, LogPrintMixin
from eletronico import SmartPhone

# l = LogPrintMixin()
# l.log_error('Deu errado')
# l.log_success('Deu certo')

# g = LogFileMixin()
# g.log_error('Deu muito ruim')
# g.log_success('Deu muito certo')

galaxy = SmartPhone('Galaxy S24')
iphone = SmartPhone('Iphone 15 Pro')

galaxy.ligar()
iphone.desligado()