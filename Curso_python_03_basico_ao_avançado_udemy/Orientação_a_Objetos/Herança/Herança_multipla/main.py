from login import Log, LogFileMixin, LogPrintMixin

l = LogPrintMixin()
l.log_error('Deu errado')
l.log_success('Deu certo')

g = LogFileMixin()
g.log_error('Deu muito ruim')
g.log_success('Deu muito certo')