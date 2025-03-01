---
title: 我的书架
date: 2024-01-11
type: "books"
layout: "books"
---

<div class="book-filter">
  <button class="filter-btn active" data-status="all">全部</button>
  <button class="filter-btn" data-status="想读">想读</button>
  <button class="filter-btn" data-status="在读">在读</button>
  <button class="filter-btn" data-status="已读">已读</button>
</div>

<div class="book-list">
  <% site.data.reading_list.forEach(function(book){ %>
    <div class="book-card" data-status="<%= book.status %>">
      <div class="book-cover">
        <img src="<%= book.cover_image %>" alt="<%= book.title %>的封面">
      </div>
      <div class="book-info">
        <h3 class="book-title"><%= book.title %></h3>
        <p class="book-author"><%= book.author %></p>
        <p class="book-publisher"><%= book.publisher %> <%= book.publish_date %></p>
        <div class="book-status <%= book.status %>">
          <span class="status-text"><%= book.status %></span>
          <% if (book.rating > 0) { %>
            <span class="book-rating">
              <% for(var i=0; i<book.rating; i++) { %>★<% } %>
              <% for(var i=book.rating; i<5; i++) { %>☆<% } %>
            </span>
          <% } %>
        </div>
        <% if (book.notes && book.notes.length > 0) { %>
          <a href="/book-review-<%= book.title.toLowerCase().replace(/\s+/g, '-') %>/" class="read-notes">查看笔记</a>
        <% } %>
      </div>
    </div>
  <% }); %>
</div>

<style>
.book-filter {
  margin: 20px 0;
  text-align: center;
}

.filter-btn {
  padding: 8px 16px;
  margin: 0 5px;
  border: 1px solid #ddd;
  border-radius: 20px;
  background: white;
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-btn.active {
  background: #4a90e2;
  color: white;
  border-color: #4a90e2;
}

.book-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px 0;
}

.book-card {
  display: flex;
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  overflow: hidden;
  transition: transform 0.3s ease;
}

.book-card:hover {
  transform: translateY(-5px);
}

.book-cover {
  flex: 0 0 120px;
  padding: 10px;
}

.book-cover img {
  width: 100%;
  height: auto;
  border-radius: 5px;
}

.book-info {
  flex: 1;
  padding: 15px;
}

.book-title {
  margin: 0 0 5px;
  font-size: 1.2em;
  color: #333;
}

.book-author,
.book-publisher {
  margin: 5px 0;
  color: #666;
  font-size: 0.9em;
}

.book-status {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 0.8em;
  margin: 10px 0;
}

.book-status.想读 {
  background: #e3f2fd;
  color: #1976d2;
}

.book-status.在读 {
  background: #e8f5e9;
  color: #388e3c;
}

.book-status.已读 {
  background: #fff3e0;
  color: #f57c00;
}

.book-rating {
  margin-left: 10px;
  color: #ffd700;
}

.read-notes {
  display: inline-block;
  margin-top: 10px;
  color: #4a90e2;
  text-decoration: none;
  font-size: 0.9em;
}

.read-notes:hover {
  text-decoration: underline;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const bookCards = document.querySelectorAll('.book-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const status = btn.dataset.status;
      
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      bookCards.forEach(card => {
        if (status === 'all' || card.dataset.status === status) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
});
</script>