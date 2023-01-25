
import pygal

for codigo_da_cidade in sorted(pygal.i18n.COUNTRIES.keys()):
    print(f'{codigo_da_cidade}, pygal.i18n.COUNTRIES["codigo_da_cidade"]')