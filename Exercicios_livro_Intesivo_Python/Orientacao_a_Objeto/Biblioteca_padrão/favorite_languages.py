from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['carlos'] = 'python'
favorite_languages['mayara'] = 'java'
favorite_languages['neto'] = 'javascript'
favorite_languages['luna'] = 'Ruby'

if __name__ == '__main__':
    for name, linguagem in favorite_languages.items():
        print(f"{name.title()}, your favorite language is {linguagem.title()}.")