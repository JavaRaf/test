import os, subprocess
from database import Data


def git_push_ids():
        
    if not os.path.exists('.git'):
        subprocess.run('git init', shell=True, check=True)
    try:
        subprocess.run(f'git config user.name github_actions', shell=True, check=True)
        subprocess.run(f'git config user.email bot@email.com', shell=True, check=True)

        subprocess.run(f'git pull origin {Data.git_branch}', shell=True, check=True)  
        
        subprocess.run('git add responded_ids.txt', shell=True, check=True)

        subprocess.run('git commit -m "update responded_ids.txt"', shell=True, check=True)
        subprocess.run(f'git push -u https://{Data.git_username}:{Data.git_tok}@github.com/{Data.git_username}/{Data.git_this_repo} {Data.git_branch}', shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(e)



