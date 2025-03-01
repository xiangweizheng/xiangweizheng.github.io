import os
import json
from datetime import datetime
from douban_book_info import search_douban_book, create_book_review

class BookManager:
    def __init__(self):
        self.books_file = 'data/reading_list.json'
        self.ensure_data_directory()
        self.load_books()

    def ensure_data_directory(self):
        """确保数据目录存在"""
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

    def load_books(self):
        """加载书籍列表"""
        self.books = []
        if os.path.exists(self.books_file):
            try:
                with open(self.books_file, 'r', encoding='utf-8') as f:
                    self.books = json.load(f)
            except json.JSONDecodeError:
                print('读取书籍列表失败，将创建新的列表')

    def save_books(self):
        """保存书籍列表"""
        with open(self.books_file, 'w', encoding='utf-8') as f:
            json.dump(self.books, f, ensure_ascii=False, indent=2)

    def add_book(self, title):
        """添加新书到列表"""
        # 检查书是否已存在
        if any(book['title'] == title for book in self.books):
            print(f'《{title}》已在列表中')
            return

        # 获取豆瓣信息
        print(f'正在获取《{title}》的信息...')
        book_info = search_douban_book(title)
        if not book_info:
            print(f'未找到《{title}》的信息')
            return

        # 添加到列表
        book_entry = {
            'title': book_info['title'],
            'author': book_info['author'],
            'publisher': book_info['publisher'],
            'publish_date': book_info['publish_date'],
            'isbn': book_info['isbn'],
            'cover_image': book_info['cover_image'],
            'status': '想读',
            'add_date': datetime.now().strftime('%Y-%m-%d'),
            'start_date': '',
            'finish_date': '',
            'rating': 0,
            'notes': []
        }
        self.books.append(book_entry)
        self.save_books()

        # 创建读书笔记文章
        if create_book_review(book_info):
            print(f'已为《{title}》创建读书笔记')

    def update_book_status(self, title, status, start_date=None, finish_date=None, rating=None):
        """更新书籍状态"""
        for book in self.books:
            if book['title'] == title:
                book['status'] = status
                if start_date:
                    book['start_date'] = start_date
                if finish_date:
                    book['finish_date'] = finish_date
                if rating is not None:
                    book['rating'] = rating
                self.save_books()
                print(f'已更新《{title}》的状态')
                return
        print(f'未找到《{title}》')

    def add_note(self, title, note):
        """添加读书笔记"""
        for book in self.books:
            if book['title'] == title:
                note_entry = {
                    'date': datetime.now().strftime('%Y-%m-%d'),
                    'content': note
                }
                book['notes'].append(note_entry)
                self.save_books()
                print(f'已为《{title}》添加笔记')
                return
        print(f'未找到《{title}》')

    def list_books(self, status=None):
        """列出书籍"""
        filtered_books = self.books
        if status:
            filtered_books = [book for book in self.books if book['status'] == status]

        if not filtered_books:
            print('没有找到符合条件的书籍')
            return

        for book in filtered_books:
            print(f"\n书名：《{book['title']}》")
            print(f"作者：{book['author']}")
            print(f"状态：{book['status']}")
            if book['start_date']:
                print(f"开始阅读：{book['start_date']}")
            if book['finish_date']:
                print(f"完成阅读：{book['finish_date']}")
            if book['rating']:
                print(f"评分：{book['rating']}星")
            if book['notes']:
                print(f"笔记数量：{len(book['notes'])}")

def main():
    manager = BookManager()
    while True:
        print('\n=== 读书管理系统 ===')
        print('1. 添加新书')
        print('2. 更新书籍状态')
        print('3. 添加读书笔记')
        print('4. 查看书籍列表')
        print('5. 退出')
        choice = input('请选择操作：')

        if choice == '1':
            title = input('请输入书名：')
            manager.add_book(title)
        elif choice == '2':
            title = input('请输入书名：')
            print('\n状态选项：')
            print('1. 想读')
            print('2. 在读')
            print('3. 已读')
            status_choice = input('请选择状态：')
            status_map = {'1': '想读', '2': '在读', '3': '已读'}
            status = status_map.get(status_choice)
            if not status:
                print('无效的状态选择')
                continue

            start_date = None
            finish_date = None
            rating = None

            if status == '在读':
                start_date = datetime.now().strftime('%Y-%m-%d')
            elif status == '已读':
                finish_date = datetime.now().strftime('%Y-%m-%d')
                rating = int(input('请输入评分（1-5星）：'))

            manager.update_book_status(title, status, start_date, finish_date, rating)
        elif choice == '3':
            title = input('请输入书名：')
            note = input('请输入笔记内容：')
            manager.add_note(title, note)
        elif choice == '4':
            print('\n状态筛选：')
            print('1. 所有书籍')
            print('2. 想读的书')
            print('3. 在读的书')
            print('4. 已读的书')
            filter_choice = input('请选择：')
            status_map = {'2': '想读', '3': '在读', '4': '已读'}
            status = status_map.get(filter_choice)
            manager.list_books(status)
        elif choice == '5':
            break
        else:
            print('无效的选择')

if __name__ == '__main__':
    main()