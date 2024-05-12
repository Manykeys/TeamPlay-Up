document.addEventListener("DOMContentLoaded", function() {
    // Функция для фильтрации заявок по заданному диапазону рейтинга
    function filterApplications() {
        var range1 = parseInt(document.getElementById('range1').innerText);
        var range2 = parseInt(document.getElementById('range2').innerText);
        var applications = document.querySelectorAll('.application-item');

        applications.forEach(function(application) {
            var rating = parseInt(application.querySelector('p:nth-child(3)').innerText.split(':')[1]);
            console.log(application.querySelector('p:nth-child(3)').innerText.split(':'));
            console.log(range1)
            console.log(range2)
            if ((range1 <= rating && rating <= range2)) {
                application.style.display = 'block';
            } else {
                application.style.display = 'none';
            }
        });
    }

    // Вызываем функцию для фильтрации заявок сразу после загрузки страницы
    filterApplications();

    // Обработчик события для кнопки "Принять"
    document.getElementById('sort').addEventListener('click', function(event) {
        event.preventDefault();
        filterApplications();
    });
});
