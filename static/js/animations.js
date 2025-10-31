// Create floating particles
function createParticles() {
    const particles = document.querySelector('.floating-particles');
    const colors = ['#4F46E5', '#06B6D4', '#818CF8'];
    
    for (let i = 0; i < 50; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.width = Math.random() * 10 + 'px';
        particle.style.height = particle.style.width;
        particle.style.background = colors[Math.floor(Math.random() * colors.length)];
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.animationDuration = (Math.random() * 6 + 3) + 's';
        particle.style.animationDelay = Math.random() * 5 + 's';
        particles.appendChild(particle);
    }
}

// Typing animation
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.innerHTML = '';
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    type();
}

// Interactive counter animation
function animateCounter(element, target, duration = 2000) {
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        element.textContent = Math.floor(current);
        
        if (current >= target) {
            element.textContent = target;
            clearInterval(timer);
        }
    }, 16);
}

// Initialize animations when page loads
document.addEventListener('DOMContentLoaded', () => {
    createParticles();
    
    // Initialize counters
    document.querySelectorAll('.counter').forEach(counter => {
        animateCounter(counter, parseInt(counter.dataset.target));
    });
    
    // Initialize typing effect
    const titleElement = document.querySelector('.typing-text');
    if (titleElement) {
        typeWriter(titleElement, 'Extract valuable information from any webpage with ease');
    }

    // Initialize hover effects for feature cards
    document.querySelectorAll('.feature-card').forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });
});
