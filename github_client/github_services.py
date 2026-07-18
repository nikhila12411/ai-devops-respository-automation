import os
from github import Github


class GitHubService:

    def __init__(self):
        token = os.getenv("GITHUB_TOKEN")

        if not token:
            raise Exception("GitHub token is missing")

        self.github = Github(token)

    def get_repositories(self, organization):
        org = self.github.get_organization(organization)

        repositories = []

        for repo in org.get_repos():
            repositories.append(repo.name)

        return repositories


if __name__ == "__main__":
    service = GitHubService()

    repos = service.get_repositories("YOUR_ORGANIZATION")

    for repo in repos:
        print(repo)
