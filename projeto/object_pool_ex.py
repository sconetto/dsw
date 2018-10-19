class ReusablePool:
    """
    Gerencia objetos reusáveis para o uso no cliente
    """

    def __init__(self, size):
        self._reusables = [Reusable() for _ in range(size)]

    def acquire(self):
        return self._reusables.pop()

    def release(self, reusable):
        self._reusables.append(reusable)


class Reusable:
    """
    Classe onde será definido o objeto real que será instaciado no pool
    """

    pass


def main():
    reusable_pool = ReusablePool(10)    # Instâncio minha pull com objetos
    reusable = reusable_pool.acquire()  # Retiro um objeto para fazer uso do mesmo
    reusable_pool.release(reusable)     # Devolvo o objeto para o poll

if __name__ == "__main__":
    main()