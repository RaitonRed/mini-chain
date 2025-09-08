import uhashlib

def sha256_hex(data):
    h = uhashlib.sha256()
    h.update(data)
    return ''.join('{:02x}'.format(b) for b in h.digest())
