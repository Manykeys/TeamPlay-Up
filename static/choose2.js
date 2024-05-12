var is_authorized = document.cookie.includes('is_authorized=true');
if (!is_authorized) {
    window.location.href = "/"; // Перенаправление на главную страницу
}