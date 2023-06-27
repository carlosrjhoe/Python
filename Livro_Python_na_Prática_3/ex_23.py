"""23 - Utilizando de ferramentas da biblioteca random e da biblioteca queue, crie uma simulação de filas em um banco, onde clientes chegam e são atendidos em tempo aleatório. Calcule métricas como tempo médio de espera e tempo médio de atendimento, exibindo em tela esses valores:"""

import random
import queue

def simular_banco(n_clientes, n_caixas, tempo_min, tempo_max):
    clientes = [random.randint(tempo_min, tempo_max) for _ in range(n_clientes)]
    filas = [queue.Queue() for _ in range(n_caixas)]

    tempo_espera_total = 0
    tempo_atendimento_atual = 0
    clientes_atendidos = 0

    while clientes or any(not fila.empty() for fila in filas):
        for fila in filas:
            if not fila.empty():
                cliente = fila.get()
                cliente['tempo_atendimento'] -= 1

                if cliente['tempo_atendimento'] == 0:
                    tempo_espera_atual += cliente['tempo_espera']
                    tempo_atendimento_atual += cliente['tempo_atendimento_original']
                    clientes_atendidos += 1
                else:
                    fila.put(cliente)
                    
                if clientes:
                    cliente = {'tempo_atendimento': clientes.pop(0), 'tempo_espera': 0, 'tempo_atendimento_original': 0}
                    cliente['tempo_atendimento_original'] = cliente['tempo_atendimento']
                    fila_menor = min(filas, key=lambda fila: fila.qsize())
                    fila_menor.put(cliente)

                for fila in filas:
                    for i in range(fila.qsize()):
                        cliente = fila.get()
                        cliente['tempo_espera'] += 1
                        fila.put(cliente)

        tempo_medio_espera = tempo_espera_total / clientes_atendidos
        tempo_medio_atendimento = tempo_atendimento_atual / clientes_atendidos
        
        return tempo_medio_espera, tempo_medio_atendimento

n_clientes = 100
n_caixas = 5
tempo_min = 5
tempo_max = 20

tempo_medio_espera, tempo_medio_atendimento = simular_banco(n_clientes, n_caixas, tempo_min, tempo_max)

print(f'Tempo médio de espera: {tempo_medio_espera:.0f} minutos.')
print(f'Tempo médio de atendimento: {tempo_medio_atendimento:.0f} minutos.')