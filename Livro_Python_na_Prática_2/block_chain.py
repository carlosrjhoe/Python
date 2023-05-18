def executa(base_dir, no_dir, chain):
    caminhos = []
    base = base_dir
    no = no_dir
    chain = chain
    caminhos.append[0](base)
    caminhos.append[1](no)
    caminhos.append[2](chain)
    return caminhos

class Cluster:
    def __init__(self, bloco, params, config):
        self.bloco = bloco
        self.params = params
        self.config = config
        self.nodes = ['bloco_01', 'bloco_02', 'bloco_03', 'bloco_04']
        self.bloco_ = {node: executa(caminho = caminhos,
                    bloco = self.bloco,
                    params = self.params,
                    confg = self.confg) for node in self.nodes}