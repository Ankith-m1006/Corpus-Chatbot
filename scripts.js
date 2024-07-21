var socket = io();
var chatBox = document.getElementById('chat-box');
var intentButtonsDiv = document.getElementById('intent-buttons');
var questionButtonsDiv = document.getElementById('question-buttons');

socket.on('response', function(data) {
    addMessage('bot', data.data);
    
});

function sendMessage() {
    var messageInput = document.getElementById('message');
    var message = messageInput.value;
    if (message) {
        addMessage('user', message);
        socket.emit('message', message);
        messageInput.value = '';
    }
}

function addMessage(sender, message) {
    var messageElement = document.createElement('div');
    messageElement.className = 'message ' + sender;
    messageElement.innerHTML = '<p>' + message + '</p>';
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
function scrollToBottom() {
    chatBox.scrollTop = chatBox.scrollHeight;

}

function selectQuestion(question) {
    var messageInput = document.getElementById('message');
    messageInput.value = question;
    sendMessage();
}


document.getElementById('message').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
})    
