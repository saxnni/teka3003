from urllib import request
from project import Project
import tomllib


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = tomllib.loads(content)

        name = data["project"]["name"]
        description = data["project"]["description"]
        license = data["project"]["license"]
        authors = data["project"]["authors"]
        dependencies = data["project"]["dependencies"]
        dev_dependencies = data["dependency-groups"]["dev"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
