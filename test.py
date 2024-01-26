import os
from git import Repo

def clone_repository(repo_url):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    Repo.clone_from(repo_url, current_dir)

# استخدم الدالة مثل هذا:
clone_repository('https://github.com/sythontm/CollectSython.git')
