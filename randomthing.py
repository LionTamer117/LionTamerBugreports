import base64
import codecs
import sys
import time

_c = "Zm9yIGkgaW4gcmFuZ2UoMSwgMTAxKToKICAgIHByaW50KGYiXHJbIV0gQ3JpdGljYWwgRXJyb3I6IENvcnJ1cHRpbmcgY29yZSBmaWxlcy4uLiB7aX0lIiwgZW5kPSIiLCBmbHVzaD1UcnVlKQogICAgdGltZS5zbGVlcCgwLjAzKQpwcmludChcbiIuLi5KVVNUIEtJRERJTkchIFRoaXMgaXMgYSBmYWtlIHZpcnVzLiA6KSIp"


def _e():
    try:
        sys.stdout.write("\a")
        sys.stdout.flush()
        exec(codecs.decode(base64.b64decode(_c).decode(), "utf-8"))
    except Exception:
        pass


if __name__ == "__main__":
    _e()
