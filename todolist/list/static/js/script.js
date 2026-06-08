// Night mode toggle functionality
        document.addEventListener('DOMContentLoaded', function() {
            const toggleBtn = document.getElementById('nightModeToggle');
            const body = document.body;
            
            // Check for saved preference
            const nightMode = localStorage.getItem('nightMode');
            if (nightMode === 'true') {
                body.classList.add('night-mode');
                toggleBtn.textContent = '☀️ Light Mode';
            }
            
            toggleBtn.addEventListener('click', function() {
                body.classList.toggle('night-mode');
                const isNightMode = body.classList.contains('night-mode');
                toggleBtn.textContent = isNightMode ? '☀️ Light Mode' : '🌙 Dark Mode';
                localStorage.setItem('nightMode', isNightMode);
            });
        });