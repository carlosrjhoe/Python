"""Crie três classes representando três funcionários de uma empresa, descreva como atributo de classe primário o cargo, e como atributos secundários seus respectivos nomes e salários, estes dados devem ser imutáveis. Insira os registros destes funcionários em uma lista e exiba em tela o conteúdo da lista de funcionários.
"""

from collections import namedtuple

funcionario = namedtuple('ID', 'Cargo Detalhes')
funcionarios = []

func_01 = funcionario('gerente', {'nome': 'carlos', 'salario': 5228.21})
func_02 = funcionario('diretor(a)', {'nome': 'mayara', 'salario': 14548.21})

funcionarios.append(func_01)
funcionarios.append(func_02)

for i in funcionarios:
    print(f'{i}')