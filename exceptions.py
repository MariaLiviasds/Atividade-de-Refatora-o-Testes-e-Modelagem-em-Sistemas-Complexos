class ProjetoError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)

class TarefaNaoEncontradaError(ProjetoError):
    def __init__(self, msg: str):
        super().__init__(msg)

class TarefaDuplicadaError(ProjetoError):
    def __init__(self, msg: str):
        super().__init__(msg)

class MembroNaoEncontradoError(ProjetoError):
    def __init__(self, msg: str):
        super().__init__(msg)

class MembroDuplicadoError(ProjetoError):
    def __init__(self, msg: str):
        super().__init__(msg)
