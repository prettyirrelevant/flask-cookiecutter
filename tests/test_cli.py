import pytest
from src import cli


def test_blueprint_list(app, cli_runner):
    result = cli_runner.invoke(cli.list)

    assert "[]" in result.output
    assert result.exit_code == 0


def test_blueprint_create_and_delete(cli_runner):
    create = cli_runner.invoke(cli.create_bp, ["testing"])
    delete = cli_runner.invoke(cli.delete, ["testing"])
    assert "Created blueprint" in create.output
    assert "Created __init__.py" in create.output
    assert "Created views.py" in create.output
    assert create.exit_code == 0
    assert "Blueprint deleted in" in delete.output
    assert delete.exit_code == 0


def test_blueprint_create_and_delete_full(cli_runner):
    create = cli_runner.invoke(cli.create_bp, ["testing_full", "-f", True])
    delete = cli_runner.invoke(cli.delete, ["testing_full"])
    assert "Created blueprint" in create.output
    assert "Created __init__.py" in create.output
    assert "Created views.py" in create.output
    assert "Created static directory in " in create.output
    assert "Created templates directory in " in create.output
    assert create.exit_code == 0
    assert "Blueprint deleted in" in delete.output
    assert delete.exit_code == 0


def test_blueprint_delete_error(cli_runner):
    create = cli_runner.invoke(cli.delete, ["invalid"])
    assert "Directory does not exist!" in create.output
    assert create.exit_code == 0
