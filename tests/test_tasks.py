import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from src.models.task import Task


def test_create_task():

    task = Task(
        "Criar sistema",
        "Sistema Flask",
        "Alta"
    )

    assert task.title == "Criar sistema"


def test_default_status():

    task = Task(
        "Estudar",
        "Pytest",
        "Média"
    )

    assert task.status == "Pendente"