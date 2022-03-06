const popup = document.querySelector('.popup');
const chatBtn = document.querySelector('.chat-btn');
const submitbtn = document.querySelector('.submit-btn');
const chatArea = document.querySelector('.chat-area');
const inputElm = document.querySelector('.chat-input');

//chat button toggeler

chatBtn.addEventListener('click', () => {
    popup.classList.toggle('show');
})

//send message

submitbtn.addEventListener('click', () => {
    let userInput = inputElm.value;

    let temp = `<div class="out-msg">
    <span class="my-msg">${userInput}</span>
    </div>`;

    chatArea.insertAdjacentHTML("beforeend", temp);
    inputElm.value = '';
})