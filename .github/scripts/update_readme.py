import os
import random
from github import Github
from datetime import datetime, timedelta

def get_repo_info(repo):
    return f"- [{repo.name}]({repo.html_url}) - {repo.description or 'No description'}"

def get_random_projects(repos, seed):
    random.seed(seed)
    return random.sample(repos, min(3, len(repos)))

g = Github(os.environ['GITHUB_TOKEN'])
user = g.get_user()

top_repos = sorted(user.get_repos(), key=lambda r: r.stargazers_count, reverse=True)[:3]

# Get all non-fork repositories
all_repos = [repo for repo in user.get_repos() if not repo.fork]

# Use the current week number as the seed for random selection
current_week = datetime.now().isocalendar()[1]
random_projects = get_random_projects(all_repos, current_week)

readme_content = f"""
# 👋 Hello, I'm {user.name or user.login}

<div align="center">
  <img src="https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif" alt="Welcome!" width="300"/>
</div>

## 🚀 Welcome to my GitHub space!

I'm passionate about AI, development tools, and innovative projects. Here you'll find a mix of practical utilities and curated resources.

### 🌟 Top Projects

{''.join(get_repo_info(repo) + '\\n' for repo in top_repos)}

### 🎲 Weekly Project Showcase

{''.join(get_repo_info(repo) + '\\n' for repo in random_projects)}

## 🛠️ Technologies & Tools

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=Python&logoColor=white)
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![AI](https://img.shields.io/badge/-AI-00FFFF?style=flat-square&logo=ai&logoColor=white)
![Git](https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white)

## 📊 GitHub Stats

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username={user.login}&show_icons=true&theme=radical" alt="{user.name or user.login}'s GitHub Stats" />
</div>

## 🤝 Let's Connect!

Feel free to reach out for collaborations or just a chat about tech!

[![Discord](https://img.shields.io/badge/-PierrunoYT-7289DA?style=flat-square&logo=discord&logoColor=white)](https://discord.com/users/PierrunoYT)

---
*This README is automatically updated every week. Last update: {datetime.now().strftime('%Y-%m-%d')}*
"""

with open('README.md', 'w') as f:
    f.write(readme_content)
