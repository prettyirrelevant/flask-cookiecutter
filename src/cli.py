from pathlib import Path

import click
from flask import current_app as app
from flask.cli import AppGroup, with_appcontext

blueprints_cli = AppGroup(
    "blueprints", short_help="Creation and listing of blueprints."
)


@blueprints_cli.command("create")
@click.argument("name")
@click.option(
    "-f",
    "--full",
    default=False,
    show_default=True,
    type=bool,
    help="Whether the blueprint creation should be minimal",
)
@with_appcontext
def create_bp(name, full):
    """Creates a blueprint with the specified name"""

    directory = Path(f"{app.config['BASE_DIR']}/src/{name}")
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)
        click.echo("Created blueprint in {}".format(directory))

        init_file = Path(f"{directory}/__init__.py")
        with open(init_file, "a") as f:
            if full:
                lines = [
                    "from flask import Blueprint \n\n",
                    f"{name}_bp = Blueprint('{name}',__name__, template_folder='templates', static_folder='static', static_url_path='/static/{name}') \n\n",
                    "from . import views",
                ]
                f.writelines(lines)
            else:
                lines = [
                    "from flask import Blueprint \n\n",
                    f"{name}_bp = Blueprint('{name}',__name__') \n\n",
                    "from . import views",
                ]
                f.writelines(lines)
            click.echo("Created __init__.py in {}".format(init_file))

        if full:
            templates_directory = Path(f"{directory}/templates/{name}")
            templates_directory.mkdir(parents=True, exist_ok=True)
            click.echo("Created templates directory in {}".format(templates_directory))

            static_directory = Path(f"{directory}/static")
            static_directory.mkdir()
            click.echo("Created static directory in {}".format(static_directory))

        views_file = Path(f"{directory}/views.py")
        with open(views_file, "a") as f:
            lines = [f"from . import {name}_bp"]
            f.writelines(lines)
            click.echo("Created views.py.py in {}".format(views_file))

    else:
        click.echo("Blueprint/directory exists already", err=True)


@blueprints_cli.command("list")
@with_appcontext
def list():
    """List registered blueprints in Flask app."""
    bps = [_ for _ in app.blueprints.keys()]
    click.echo(bps)


@blueprints_cli.command("delete")
@click.argument("name")
@with_appcontext
def delete(name):
    """Deletes a blueprint folder"""
    directory = Path(f"{app.config['BASE_DIR']}/src/{name}")
    if directory.exists():
        rmdir_recursive(directory)
        click.echo(f"Blueprint deleted in {directory}!")
    else:
        click.echo("Directory does not exist!", err=True)


def rmdir_recursive(directory):
    for i in directory.iterdir():
        if i.is_dir():
            rmdir_recursive(i)
        else:
            i.unlink()

    directory.rmdir()
