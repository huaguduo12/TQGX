import requests
from github import Github

# GitHub 配置
GITHUB_TOKEN = ""  # 替换为你的 GitHub Personal Access Token
REPO_NAME = "huaguduo12/ceshi"  # 替换为你的存储库名称
FILE_PATH = "ADD.txt"  # 替换为文件路径（如 data.txt）

# 要读取的网页
WEBPAGE_URL = "https://example.com"  # 替换为目标网页 URL

def fetch_webpage_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None

def write_to_github(content):
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(REPO_NAME)
        file = repo.get_contents(FILE_PATH)
        repo.update_file(
            FILE_PATH, 
            "Updated content", 
            content, 
            file.sha, 
            branch="main"
        )
        print("File updated successfully on GitHub.")
    except Exception as e:
        print(f"Error writing to GitHub: {e}")

def main():
    print("Fetching webpage content...")
    content = fetch_webpage_content(WEBPAGE_URL)
    if content:
        print("Writing content to GitHub...")
        write_to_github(content)

if __name__ == "__main__":
    main()
