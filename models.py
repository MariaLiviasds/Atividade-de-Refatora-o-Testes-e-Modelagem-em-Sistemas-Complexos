from typing import List
from enums import StatusTarefa
from exceptions import (
    TarefaNaoEncontradaError,
    TarefaDuplicadaError,
    MembroDuplicadoError,
    MembroNaoEncontradoError,
)

class Tarefa:
    """Representa uma tarefa dentro de um projeto."""
    def __init__(self, titulo: str, descricao: str, responsavel: str):
        self._titulo = titulo
        self._descricao = descricao
        self._responsavel = responsavel
        self._status = StatusTarefa.PENDENTE

    @property
    def status(self) -> StatusTarefa:
        return self._status

    def concluir(self) -> None:
        self._status = StatusTarefa.CONCLUIDA

    def __str__(self) -> str:
        return f"{self._titulo} - {self._status.name} - Responsável: {self._responsavel}"

class Membro:
    """Representa um membro de equipe."""
    def __init__(self, nome: str, funcao: str):
        self._nome = nome
        self._funcao = funcao

    def __str__(self) -> str:
        return f"{self._nome} ({self._funcao})"

class Projeto:
    """Classe principal que gerencia o projeto."""
    def __init__(self, nome: str, prazo: str, descricao: str):
        self._nome = nome
        self._prazo = prazo
        self._descricao = descricao
        self._tarefas: List[Tarefa] = []
        self._membros: List[Membro] = []

    def adicionar_tarefa(self, titulo: str, descricao: str, responsavel: str) -> None:
        if any(t._titulo == titulo for t in self._tarefas):
            raise TarefaDuplicadaError(f"Tarefa '{titulo}' já existe")
        self._tarefas.append(Tarefa(titulo, descricao, responsavel))

    def adicionar_membro(self, nome: str, funcao: str) -> None:
        if any(m._nome == nome for m in self._membros):
            raise MembroDuplicadoError(f"Membro '{nome}' já existe")
        self._membros.append(Membro(nome, funcao))

    def concluir_tarefa(self, titulo: str) -> None:
        for tarefa in self._tarefas:
            if tarefa._titulo == titulo:
                tarefa.concluir()
                return
        raise TarefaNaoEncontradaError(f"Tarefa '{titulo}' não encontrada")

    def listar_tarefas(self) -> List[str]:
        return [str(t) for t in self._tarefas]

    def relatorio_projeto(self) -> str:
        linhas = [
            f"Projeto: {self._nome}",
            f"Prazo: {self._prazo}",
            f"Descrição: {self._descricao}",
            "Membros:"
        ] + [f" - {m}" for m in self._membros] + ["Tarefas:"] + [f" - {t}" for t in self.listar_tarefas()]
        return "\n".join(linhas)
