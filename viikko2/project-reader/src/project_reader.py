from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed_toml = toml.loads(content)
        poetry_info = parsed_toml["tool"]["poetry"]

        name = poetry_info["name"]
        description = poetry_info["description"]
        license = poetry_info["license"]
        authors = poetry_info["authors"]
        deps = list(poetry_info["dependencies"])
        dev_deps = list(poetry_info["group"]["dev"]["dependencies"])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            name,
            description,
            license,
            authors,
            deps,
            dev_deps,
        )
