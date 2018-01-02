"""
Stack_overflow_Extractor : Extracts user details based on the users stack-overflow link
"""
import ssl
import json
try:
    from github import Github
except ImportError:
    print("Package missing, need to install github API")
try:
    import urllib
except ImportError:
    print("Package missing, need to install urllib")
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Package missing, need to install BeautifulSoup")


def stackoverflow(url):
    """
    :param url: Takes Stack-overflow link as a string
    :return: Username, description, tags and links form the url
    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "lxml")
    except ConnectionRefusedError:
        print("Problem opening url. Url dosent exit")

    # Fetching the User-Name and Description

    title = soup.title.string
    description = soup.find("div", {"class" : "bio"}).find_all("p")
    description = " ".join(str(i) for i in description)
    des = BeautifulSoup(description, "lxml")
    description = des.get_text()
    user = ""
    count = 0
    for i, k in enumerate(title):
        if k == " " and count != 1:
            i += 1
            count += 1
            for j in range(title.index(k)+1, len(title)):
                if title[j] != "-":
                    user = user+title[j]
                else:
                    break
        else:
            if count == 1:
                break

    # Extracting TOP TAGS and other inter-linked LINKS
    tags = soup.find("body").find("div", id="top-tags").find_all("a", limit=6)
    links = soup.find("body").find("div", "user-links").find_all("a")

    tags = [i.string for i in tags]
    links = [i["href"] for i in links]

    return user, description, tags, links

def git_repos(links):
    """
    :param links: Links extracted from the url using Stackoverflow()
    :return: Github repositories of the specific user
    """
    repos = []
    for i in links:
        if "github" in i:
            github = Github()
            name = i[19:len(i)]
            repos = [repo.name for repo in github.get_user(name).get_repos()]

    return repos


def convert_to_json(user, description, tags, repos):
    """
    :param user: Username
    :param description: User description
    :param tags: Popular tags of the user
    :param repos: Github repositories of the user
    :return: Json file with details like username, description, popular tags and github repositories
    """
    with open("result.json", "w") as file:
        json.dump(user, file, ensure_ascii=True, sort_keys=True)
        file.write("\n\n")
        if description != None:
            json.dump(description, file, ensure_ascii=True, sort_keys=True)
            file.write("\n\n")
        file.write("\nTOP TAGS \n\n")
        for tag in enumerate(tags, start=1):
            json.dump(tag, file, ensure_ascii=True, sort_keys=True)
            file.write("\n")
        file.write("\n\n")
        if repos != []:
            file.write("Github REPOS \n\n")
            for i in enumerate(repos, start=1):
                json.dump(i, file, ensure_ascii=True, sort_keys=True)
                file.write("\n")

def main():
    """
    :return: Null
    """
    url = input()
    user, description, tags, links = stackoverflow(url)
    repos = git_repos(links)
    convert_to_json(user, description, tags, repos)

if __name__ == "__main__":
    main()
