const messagesList = document.querySelector(".messages-list");
const messageForm = document.querySelector(".message-form");
const messageInput = document.querySelector(".message-input");

messageForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const message = messageInput.value.trim();
  if (message.length === 0) {
    return;
  }

  const messageItem = document.createElement("li");
  messageItem.classList.add("message", "sent");
  messageItem.innerHTML = `
      <div class="chat-message mb-3 text-end">
      <div class="fw-bold text-muted">You</div>
        <div class="d-flex justify-content-end">
            <div class="bg-primary text-white p-3 rounded border">${message}</div>
        </div>
    </div>`;
  messagesList.appendChild(messageItem);

  messageInput.value = "";

  fetch("", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      csrfmiddlewaretoken: document.querySelector("[name=csrfmiddlewaretoken]")
        .value,
      message: message,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      const response = data.response;
      const messageItem = document.createElement("li");
      messageItem.classList.add("message", "received");
      messageItem.innerHTML = `
        <div class="chat-message mb-3">
        <div class="fw-bold text-muted">ZapAI</div>
          <div class="d-flex">
              <div class="bg-light p-3 rounded border text-black">${response}</div>
          </div>
      </div>`;
      messagesList.appendChild(messageItem);
    });
});