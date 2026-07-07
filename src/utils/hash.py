import hashlib

def calculate_sha256(content: str) -> str:
    """Calculate the SHA-256 hash of a string."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()
