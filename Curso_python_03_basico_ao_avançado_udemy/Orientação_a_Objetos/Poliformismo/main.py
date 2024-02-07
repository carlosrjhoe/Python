from notificacao import notificar, Notificacao, NotificacaoEmail, NotificacaoSMS

notificacao_rmail = NotificacaoEmail('Notificação envida via e-mail')
notificar(notificacao_rmail)

notificacao_sms = NotificacaoSMS('Notificação envida via sms')
notificar(notificacao_sms)