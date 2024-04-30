document.addEventListener('DOMContentLoaded', function() {
    const boxes = document.querySelectorAll('.index-div');

    boxes.forEach(function(box) {
        const textElement = box.querySelector('.index-description');
        const maxLength = 350;

        if (textElement.textContent.length > maxLength) {
            textElement.textContent = textElement.textContent.slice(0, maxLength) + '...';
        }

        box.addEventListener('mouseenter', function() {
            const randomColor = getRandomColor();
            box.style.borderColor = randomColor;
            box.style.boxShadow = `inset -1px 10px 334px -14px ${randomColor}`;
        });

        box.addEventListener('mouseleave', function() {
            box.style.borderColor = '#ccc';
            box.style.boxShadow = 'inset -1px 10px 44px -14px';
        });
    });
});

function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

document.getElementById('toggle-categories').addEventListener('click', function() {
    document.getElementById('categories-sidebar').classList.toggle('show');
    document.querySelector('.index-container').classList.toggle('shifted'); // Добавляем/удаляем класс сдвига контента
});


function showText(element) {
    // Найти заголовок и описание внутри элемента
    var title = element.querySelector('.index-title');
    var description = element.querySelector('.index-description');
    // Убрать класс 'hidden' для показа текста
    title.classList.remove('hidden');
    description.classList.remove('hidden');
}

function hideText(element) {
    // Найти заголовок и описание внутри элемента
    var title = element.querySelector('.index-title');
    var description = element.querySelector('.index-description');
    // Добавить класс 'hidden' для скрытия текста
    title.classList.add('hidden');
    description.classList.add('hidden');
}
