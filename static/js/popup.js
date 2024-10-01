document.addEventListener("DOMContentLoaded", function() {
    function showPopup(message) {
        const popup = document.getElementById("popup");
        const popupMessage = document.getElementById("popupMessage");
        const closePopup = document.getElementById("closePopup");

        popupMessage.textContent = message;
        popup.classList.remove("hidden");

        closePopup.onclick = function() {
            popup.classList.add("hidden");
        };
    }

    // Retrieve messages from Django
    const messages = JSON.parse(document.getElementById('messages').textContent || '[]');
    if (messages.length > 0) {
        showPopup(messages[0]);
    }
});



