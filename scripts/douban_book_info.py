import requests
import re
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

def search_douban_book(title):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    search_url = f'https://www.douban.com/search?q={title}&cat=1001'
    
    try:
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 获取第一个搜索结果的链接
        result = soup.find('div', class_='result')
        if not result:
            return None
            
        book_link = result.find('a', href=re.compile(r'https://book.douban.com/subject/\d+/'))
        if not book_link:
            return None
            
        # 获取图书详情页
        book_url = book_link['href']
        book_response = requests.get(book_url, headers=headers)
        book_soup = BeautifulSoup(book_response.text, 'html.parser')
        
        # 提取图书信息
        info = {
            'title': book_soup.find('h1').text.strip(),
            'cover_image': book_soup.find('a', class_='nbg').find('img')['src'],
            'author': '',
            'publisher': '',
            'publish_date': '',
            'isbn': ''
        }
        
        # 提取图书详细信息
        info_text = book_soup.find('div', id='info').text
        for line in info_text.split('\n'):
            line = line.strip()
            if '作者' in line:
                info['author'] = line.split(':')[-1].strip()
            elif '出版社' in line:
                info['publisher'] = line.split(':')[-1].strip()
            elif '出版年' in line:
                info['publish_date'] = line.split(':')[-1].strip()
            elif 'ISBN' in line:
                info['isbn'] = line.split(':')[-1].strip()
        
        return info
    except Exception as e:
        print(f'Error: {str(e)}')
        return None

def create_book_review(book_info):
    if not book_info:
        return False
        
    # 创建文章文件名
    file_name = f"book-review-{book_info['title'].lower().replace(' ', '-')}.md"
    file_path = os.path.join('source', '_posts', file_name)
    
    # 生成文章内容
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    content = f"""---
title: {book_info['title']}的读书笔记
date: {current_date}
tags:
  - 读书笔记
categories:
  - 书影音
  - 读书
book_info:
  title: {book_info['title']}
  author: {book_info['author']}
  publisher: {book_info['publisher']}
  publish_date: {book_info['publish_date']}
  isbn: {book_info['isbn']}
  cover_image: {book_info['cover_image']}
reading_status: 在读
reading_progress:
  start_date: {datetime.now().strftime('%Y-%m-%d')}
  finish_date: 
rating: 
---

## 基本信息

![{book_info['title']}]({book_info['cover_image']})

## 读书笔记


## 精彩片段


## 个人感想


## 推荐指数

待评分

---

*以上是我的读书笔记，欢迎交流讨论！*
"""
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f'Error creating file: {str(e)}')
        return False

def main():
    title = input('请输入书名：')
    print('正在搜索豆瓣图书信息...')
    book_info = search_douban_book(title)
    
    if book_info:
        if create_book_review(book_info):
            print('读书笔记创建成功！')
        else:
            print('创建读书笔记失败。')
    else:
        print('未找到相关图书信息。')

if __name__ == '__main__':
    main()