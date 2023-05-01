document.querySelectorAll('.scroll').forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      const href = link.getAttribute('href');
      const targetElement = document.querySelector(href);
  
      // Scroll smoothly to the target element
      targetElement.scrollIntoView({
        behavior: 'smooth',
        block: 'start',
      });
    });
  });