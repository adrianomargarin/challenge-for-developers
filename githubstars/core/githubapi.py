import requests


class GithubAPI(object):

    def __init__(self, username):
        self.username = username

    def serializer(self, contents):
        result = []

        for content in contents:
            result.append({
                'id': content['id'],
                'name': content['name'],
                'url': content['url'],
                'language': content['language'],
                'username': self.username,
            })

        return result

    def get_repositories(self):
        return requests.get('https://api.github.com/users/{}/starred?sort=updated&direction=desc'.format(self.username))

    def get_content(self):
        response = self.get_repositories()

        return self.serializer(response.json())
