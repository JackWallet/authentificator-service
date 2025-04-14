import secrets


def generate_random_token(length_bytes: int = 32) -> str:
    return secrets.token_urlsafe(nbytes=length_bytes)
