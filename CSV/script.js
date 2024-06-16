document.addEventListener('DOMContentLoaded', function() {
  fetch('data.json')
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('data-container');
      data.forEach(row => {
        const div = document.createElement('div');
        for (const key in row) {
          const span = document.createElement('span');
          span.textContent = `${key}: ${row[key]}`;
          div.appendChild(span);
        }
        container.appendChild(div);
      });
    });
});