import os
import random
from github import Github
from datetime import datetime

def get_repo_info(repo):
    description = repo.description if repo.description else "No description provided"
    return f"<li><a href='{repo.html_url}'><b>{repo.name}</b></a><br/>{description}</li>"

def get_random_projects(repos, seed):
    random.seed(seed)
    return random.sample(repos, min(3, len(repos)))

g = Github(os.environ['GITHUB_TOKEN'])
user = g.get_user()

top_repos = sorted(user.get_repos(), key=lambda r: r.stargazers_count, reverse=True)[:3]
all_repos = [repo for repo in user.get_repos() if not repo.fork]
current_week = datetime.now().isocalendar()[1]
random_projects = get_random_projects(all_repos, current_week)

readme_content = f"""
<h1 align="center">👋 Hello, I'm {user.name or user.login}</h1>

<p align="center">
  <img src="https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif" alt="Welcome!" width="300"/>
</p>

<h2 align="center">🚀 Welcome to my GitHub space!</h2>

<p align="center">I'm passionate about AI, development tools, and innovative projects. Here you'll find a mix of practical utilities and curated resources.</p>

<h3 align="center">🌟 Top Projects</h3>

<ul>
{''.join(get_repo_info(repo) for repo in top_repos)}
</ul>

<h3 align="center">🎲 Weekly Project Showcase</h3>

<ul>
{''.join(get_repo_info(repo) for repo in random_projects)}
</ul>

<h3 align="center">🛠️ Technologies & Tools</h3>

<p align="center">
  <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=Python&logoColor=white" />
  <img src="https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/-AI-00FFFF?style=flat-square&logo=ai&logoColor=white" />
  <img src="https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white" />
</p>

<h3 align="center">📊 GitHub Stats</h3>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username={user.login}&show_icons=true&theme=radical" alt="{user.name or user.login}'s GitHub Stats" />
</p>

<h3 align="center">🤝 Let's Connect!</h3>

<p align="center">Feel free to reach out for collaborations or just a chat about tech!</p>

<p align="center">
  <a href="https://discord.com/users/PierrunoYT">
    <img src="https://img.shields.io/badge/-PierrunoYT-7289DA?style=flat-square&logo=discord&logoColor=white" />
  </a>
</p>

<p align="center">
  <i>This README is automatically updated every week. Last update: {datetime.now().strftime('%Y-%m-%d')}</i>
</p>
"""

with open('README.md', 'w') as f:
    f.write(readme_content)
