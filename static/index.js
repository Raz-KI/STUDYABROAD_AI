async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput.trim()) return;

    // put the user message in chat box above
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div class="user-message">${userInput}</div>`;
    
    // This block for sending the user-input to serrver
    const response = await fetch('/chat', { // Which function to send to
        method: 'POST',     // Since we are "posting" from web to server
        headers: {      // The content type
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }), // The actual data sent. It is sent with message as key and the userinput as value
        // console.out
    });

    const data = await response.json();
    chatBox.innerHTML += `<div class="bot-message">${data.response}</div>`;
    document.getElementById('user-input').value = '';
    chatBox.scrollTop = chatBox.scrollHeight;
}