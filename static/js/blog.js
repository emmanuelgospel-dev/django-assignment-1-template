document.addEventListener('DOMContentLoaded', () => {
  const tabs = document.querySelectorAll('.blog-tab');
  const cards = document.querySelectorAll('.blog-card');

  tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
      tabs.forEach((t) => t.classList.remove('active'));
      tab.classList.add('active');

      const category = tab.dataset.category;
      cards.forEach((card) => {
        const match = !category || card.dataset.category === category;
        card.classList.toggle('blog-hidden', !match);
      });
    });
  });
});
