document.addEventListener("DOMContentLoaded", function () {
    const popups = document.querySelectorAll(".popa");
    const infBlocks = document.querySelectorAll(".inf > div");
    const closeButtons = document.querySelectorAll(".close");

    function hidePopup() {
        popups.forEach((popup) => {
            popup.style.display = "none";
        });
    }

    infBlocks.forEach((infBlock) => {
        infBlock.addEventListener("click", () => {
            const popup = infBlock.querySelector(".popa");
            if (popup) {
                hidePopup();
                popup.style.display = "flex";
            }
        });
    });

    closeButtons.forEach((button) => {
        button.addEventListener("click", function (e) {
            e.stopPropagation(); // чтоб не срабатывало на весь body
            hidePopup();
        });
    });

    window.addEventListener("click", function (event) {
        // Клик вне попапа — закрыть
        if (!event.target.closest(".popa") && !event.target.closest(".inf > div")) {
            hidePopup();
        }
    });
});


const btnShow = document.getElementById('btn_show');
const btnHide = document.getElementById('btn_hide');
const popup = document.getElementById('pop_log');

function pop_log_content (url) {

    fetch(url)
    .then((response) => response.text())
    .then((html) => {
        const content = popup.querySelector(".pop_log");
        if (content) content.innerHTML = html;
    })
    .catch((error) => console.error("Ошибка загрузки попапа:", error));
}

btnShow.addEventListener('click', function () {

    popup.style.display = 'block';
    console.log('PRIFFKI')
});

btnHide.addEventListener('click', function () {
    popup.style.display = 'none';
    console.log('POKA')
});

document.getElementById("to_promos").addEventListener("click", function () {
    const promosBlock = document.getElementById("promos");
    if (promosBlock) {
        promosBlock.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }
});
