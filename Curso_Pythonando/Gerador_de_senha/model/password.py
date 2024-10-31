from datetime import datetime
from pathlib import Path


class BaseModel:
    BASE_DIR = Path(__file__).resolve().parent.parent
    BD_DIR = BASE_DIR / 'db'

    def save(self):
        table_path = Path(self.BD_DIR / f'{self.__class__.__name__}.txt')
        if not table_path.exists():
            table_path.touch()

        with open(table_path, 'a') as arquivo:
            arquivo.write(' | '.join(map(str, self.__dict__.values())))
            arquivo.write('\n')


class Password(BaseModel):
    def __init__(self, domain=None, password=None, expire=False) -> None:
        self.domain = domain
        self.password = password
        self.create_at = datetime.now().isoformat()


if __name__ == '__main__':
    p1 = Password('pythonado', 1234)
    p1.save()