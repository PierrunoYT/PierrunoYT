import os
import random
from github import Github

def get_repo_info(repo):
    return f"- [{repo.name}]({repo.html_url}) - {repo.description or 'No description'}"

g = Github(os.environ['GITHUB_TOKEN'])
user = g.get_user()

top_repos = sorted(user.get_repos(), key=lambda r: r.stargazers_count, reverse=True)[:3]

# Get all non-fork repositories
all_repos = [repo for repo in user.get_repos() if not repo.fork]

# Select 3 random projects
random_projects = random.sample(all_repos, min(3, len(all_repos)))

readme_content = f"""
# 👋 Hello, I'm {user.name or user.login}

<div align="center">
  <img src="https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif" alt="Welcome!" width="300"/>
</div>

## 🚀 Welcome to my GitHub space!

I'm passionate about AI, development tools, and innovative projects. Here you'll find a mix of practical utilities and curated resources.

### 🌟 Top Projects

{''.join(get_repo_info(repo) + '\\n' for repo in top_repos)}

### 🎲 Random Weekly Showcase

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
"""

with open('README.md', 'w') as f:
    f.write(readme_content)
