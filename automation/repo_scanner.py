class RepositoryScanner:

    def scan(self, repository):

        print(f"Scanning repository: {repository}")

        report = {
            "repository": repository,
            "terraform": False,
            "docker": False,
            "github_actions": False,
            "python": False
        }

        return report


if __name__ == "__main__":

    scanner = RepositoryScanner()

    result = scanner.scan("sample-repository")

    print(result)
