import pytest
from models import Projeto, Tarefa, Membro
from exceptions import (
    TarefaNaoEncontradaError,
    TarefaDuplicadaError,
    MembroDuplicadoError
)
from enums import StatusTarefa

# Projeto base para reuso
@pytest.fixture
def projeto_exemplo():
    return Projeto("Sistema X", "2025-07-01", "Desenvolvimento de um sistema")

def test_adicionar_tarefa(projeto_exemplo):
    projeto_exemplo.adicionar_tarefa("Login", "Criar tela de login", "Alice")
    assert len(projeto_exemplo._tarefas) == 1
    assert projeto_exemplo._tarefas[0]._titulo == "Login"

def test_adicionar_tarefa_duplicada(projeto_exemplo):
    projeto_exemplo.adicionar_tarefa("Login", "Criar tela de login", "Alice")
    with pytest.raises(TarefaDuplicadaError):
        projeto_exemplo.adicionar_tarefa("Login", "Outra descrição", "Bob")

def test_concluir_tarefa(projeto_exemplo):
    projeto_exemplo.adicionar_tarefa("API", "Criar API REST", "Bob")
    projeto_exemplo.concluir_tarefa("API")
    assert projeto_exemplo._tarefas[0].status == StatusTarefa.CONCLUIDA

def test_concluir_tarefa_inexistente(projeto_exemplo):
    with pytest.raises(TarefaNaoEncontradaError):
        projeto_exemplo.concluir_tarefa("Inexistente")

def test_adicionar_membro(projeto_exemplo):
    projeto_exemplo.adicionar_membro("Carlos", "Dev")
    assert len(projeto_exemplo._membros) == 1
    assert projeto_exemplo._membros[0]._nome == "Carlos"

def test_adicionar_membro_duplicado(projeto_exemplo):
    projeto_exemplo.adicionar_membro("Carlos", "Dev")
    with pytest.raises(MembroDuplicadoError):
        projeto_exemplo.adicionar_membro("Carlos", "QA")

def test_listar_tarefas(projeto_exemplo):
    projeto_exemplo.adicionar_tarefa("Login", "Criar tela de login", "Alice")
    projeto_exemplo.adicionar_tarefa("Cadastro", "Tela de cadastro", "Bob")
    tarefas = projeto_exemplo.listar_tarefas()
    assert len(tarefas) == 2
    assert "Login" in tarefas[0]

def test_relatorio_projeto(projeto_exemplo):
    projeto_exemplo.adicionar_membro("Carlos", "Dev")
    projeto_exemplo.adicionar_tarefa("Login", "Criar tela de login", "Alice")
    relatorio = projeto_exemplo.relatorio_projeto()
    assert "Sistema X" in relatorio
    assert "Carlos" in relatorio
    assert "Login" in relatorio