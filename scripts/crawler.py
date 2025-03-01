import requests
import json
from bs4 import BeautifulSoup

# 目标 URL（替换为您的数据源）
url = "https://hy1fly.github.io/YF-Cloud/data-source"

# 设置请求头，模拟浏览器访问
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    # 发送 HTTP 请求
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 检查请求是否成功

    # 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取数据（根据目标页面结构调整）
    data = {
        "title": soup.title.text.strip() if soup.title else "No Title",  # 提取标题
        "content": soup.find('div', class_='content').text.strip() if soup.find('div', class_='content') else "No Content",  # 提取内容
        "timestamp": soup.find('time')['datetime'] if soup.find('time') else "No Timestamp"  # 提取时间戳
    }

    # 保存为 JSON 文件
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("数据爬取成功并保存为 data.json")

except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
except Exception as e:
    print(f"发生错误: {e}")
