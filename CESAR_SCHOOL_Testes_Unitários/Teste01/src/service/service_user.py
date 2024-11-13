from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        """Verificar se os parametros é Str e diferente de None, verificar se o nome não existe para adicionar"""
        if name is not None and job is not None:
            if not isinstance(name, str) or not isinstance(job, str) or not name.strip() or not job.strip():
                return "Erro: Nome e profissão devem ser strings não vazias."

        for user in self.store.bd:
            if user.name == name:
                return f"Erro: Usário já existe no sistema."

        user = User(name, job)
        self.store.bd.append(user)
        return "Usuário adicionado com sucesso!"

    def del_user(self, name):
        """Verificar se os parametros é Str e diferente de None, verificar se o nome já existe para remover"""
        if not isinstance(name, str) or not name.strip():
            return "Erro: Nome deve ser uma string não vazia."

        for user in self.store.bd:
            if user.name == name:
                self.store.bd.remove(user)
                return "Usuário deletado com sucesso."
        return "Erro: Usuário não encontrado no sistema."

    def update_user(self, old_name, new_name):
        """Verificar se os parametros é Str e diferente de None, verificar se o nome já existe para atualizar;"""
        if not isinstance(old_name, str) \
                or not old_name.strip() or not isinstance(new_name, str) \
                or not new_name.strip():
            return "Erro: Nome antigo e novo devem ser strings não vazias."
        if old_name == new_name:
            return "Erro: O nome antigo e o novo nome não podem ser iguais."

        for user in self.store.bd:
            if user.name == old_name:
                user.name = new_name
                return f"Nome do usuário atualizado com sucesso."
        return "Erro: Usuário não encontrado no sistema."

    def get_user_by_name(self, name):
        """Verificar se os parametros é Str e diferente de None E verificar se o nome já existe para recuperar;"""
        if not isinstance(name, str) or not name.strip():
            return "Erro: Nome deve ser uma string não vazia."
        for user in self.store.bd:
            if user.name == name:
                return user
        return "Erro: Usuário não encontrado no sistema."
