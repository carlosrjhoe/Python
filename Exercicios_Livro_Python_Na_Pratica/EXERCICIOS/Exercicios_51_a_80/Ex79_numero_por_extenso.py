def num_por_extenso(numero):
    if numero == 0:
        return 'zero'
    
    unidade = (",", 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
    dezena = (",", 'vinte e', 'trinta e', 'quarenta e', 'cinquenta e', 'sessenta e', 'setenta e', 'oitenta e', 'noventa e')
    dezena_rombo = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
    
    h, t, u = ",",","
    
    