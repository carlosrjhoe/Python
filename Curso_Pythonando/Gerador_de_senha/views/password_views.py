import string
import secrets
import hashlib
import base64
from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken


class FernetHasher:
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase
    BASE_DIR = Path(__file__).resolve().parent.parent
    KYE_DIR = BASE_DIR / "keys"

    def __init__(self, key):
        if not isinstance(key, bytes):
            key = key.encode()

        self.fernet = Fernet(key)
    

    @classmethod
    def _get_random_string(cls, length=5):
        string = ""
        for i in range(10):
            string = string + secrets.choice(cls.RANDOM_STRING_CHARS)
        return string

    @classmethod
    def create_key(cls, archive=False):
        value = cls._get_random_string()
        hasher = hashlib.sha256(value.encode("utf-8")).digest()
        key = base64.b64encode(hasher)
        if archive:
            return key, cls.archive_key(key)
        return key, None

    @classmethod
    def archive_key(cls, key):
        file = "key.key"
        while Path(cls.KYE_DIR / file).exists():
            file = f"key_{cls._get_random_string(length=5)}.key"

        with open(cls.KYE_DIR / file, "wb") as arq:
            arq.write(key)

        return cls.KYE_DIR / file
    
    def encrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()

        return self.fernet.encrypt(value)
    
    def decrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()
        try:
            return self.fernet.decrypt(value).decode()
        except InvalidToken as e:
            return 'Token inválido'


if __name__ == "__main__":
    # FernetHasher.create_key(archive=True)
    fernet_carlos = FernetHasher('CAiVY9inIJ/OBp3ttfmLSEkhA7A2ARMKBhH4kprEZIc=')
    senha = fernet_carlos.decrypt(b'gAAAAABnI25YQbB7YXrN7HR-2H_sLpKG4naiu2fQOZYLl1NJ1sWkgJFPwyfbEQKMvSR9MbK4qW6h2PWskhuFmtrendPNuDRhDw==')
    print(senha)
    
