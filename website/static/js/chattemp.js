document.addEventListener('DOMContentLoaded', function() {
    const messagesContainer =
document.getElementById('messages-container');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');

    sendButton.addEventListener('click', function() {
        sendMessage();
    });

    messageInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const message = messageInput.value.trim();
        if (message !== '') {
            appendMessage('You', message);
            messageInput.value = '';
        }
    }

    function appendMessage(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        if (sender === 'You') {
            messageDiv.classList.add('user-message');
        }
        messageDiv.innerHTML = `<strong>${sender}:</strong> 
${message}`;
        messagesContainer.appendChild(messageDiv);
        // Scroll to bottom
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
});