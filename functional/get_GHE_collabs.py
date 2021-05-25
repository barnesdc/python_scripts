from requests import exceptions, request
import os
import csv

"""
 Usage:
 1. To run this script, you may need to install the above
    packages if not already installed on your machine

 2. This script requires you to load the GHE_ACCESS_TOKEN
    into your environment. Type the following in the terminal
    to load your github access token:

    'export GHE_ACCESS_TOKEN=your_token_goes_here'

 3. A csv file exported from the squad metrics dashboard must be
    present and correctly named as well. You can down

 4. Upon completion of the script, a report.csv file will be created
    in the same directory.
 """


class GitHubGraphQlQuery(object):
    BASE_URL = "https://api.github.ibm.com/graphql"

    def __init__(
        self,
        github_token=None,
        query=None,
        variables=None,
        additional_headers=None
    ):
        self._query = query
        self._variables = variables or dict()
        self.github_token = github_token
        self.query = query
        self.additional_headers = additional_headers or dict()

    @property
    def headers(self):
        default_headers = dict(
            Authorization=f"token {self.github_token}",
        )
        return {
            **default_headers,
            **self.additional_headers
        }

    def generator(self):
        while True:
            try:
                yield request(
                    "post",
                    GitHubGraphQlQuery.BASE_URL,
                    headers=self.headers,
                    json={"query": self._query, "variables": self._variables},
                ).json()
            except exceptions.HTTPError as http_err:
                raise http_err
            except Exception as err:
                print(request)
                raise err

    def iterator(self):
        pass


class GitHubProvider(GitHubGraphQlQuery):
    QUERY = """
        query($org: String!, $name: String!) {
            organization(login: $org) {
                name
                repository(name:$name){
                    name
                    viewerPermission
                    collaborators(first: 100){
                        edges{
                            node{
                                    name
                                    login
                            }
                            permission
                        }
                    }
                }
            }
        }
        """
    ADDITIONAL_HEADERS = dict(
        Accept="application/vnd.github.vixen-preview+json")

    def __init__(self, organization_name, repo_name, github_token):
        super().__init__(
            github_token=github_token,
            query=GitHubProvider.QUERY,
            variables=dict(org=organization_name, name=repo_name),
            additional_headers=GitHubProvider.ADDITIONAL_HEADERS
        )

    def iterator(self):
        generator = self.generator()
        response = next(generator)
        return_json = {
            "org": response["data"]["organization"]["name"],
            "repo_name": response["data"]["organization"]["repository"]["name"],
            "collaborators": response["data"]["organization"]["repository"]["collaborators"]
        }
        return (return_json)


def main():
    repo_results = []
    # update / verify input csv file name is correct
    with open('repos-not-onboarded.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print('Processing CSV at this time')
                line_count += 1
            else:
                print('.', end='', flush=True)
                repo_name = ''.join({row[1]})
                org = ''.join({row[0]})
                gh = GitHubProvider(
                    org, repo_name, os.getenv('GHE_ACCESS_TOKEN'))
                repo = gh.iterator()
                repo_results.append(repo)
                line_count += 1
        print(f'\nProcessed {line_count} lines.')
        write_to_csv(repo_results)


def write_to_csv(repo_results):
    with open('report.csv', mode='w') as csv_file:
        repo_writer = csv.writer(
            csv_file, delimiter='}', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for repo in repo_results:
            repo_writer.writerow([repo])
    print("\nReport.csv ready for review.")


if __name__ == '__main__':
    main()
