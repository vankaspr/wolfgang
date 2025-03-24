const logo = document.getElementById("logo");
const menu = document.getElementById("menu");

logo.addEventListener("click", function() {
    logo.classList.toggle("expanded");  // Сдвигаем кнопку влево
    menu.classList.toggle("visible");   // Показываем или скрываем кнопки
});

document.querySelector('.logo').addEventListener('click', function() {
    document.querySelector('.container').classList.toggle('menu-active');
});

