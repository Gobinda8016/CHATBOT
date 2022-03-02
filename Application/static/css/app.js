const popup = document.querySelector('.popup');
const chatBtn = document.querySelector('.chat-btn');
const submitbtn = document.querySelector('.submit-btn');
const chatArea = document.querySelector('.chat-area');
const inputElm = document.querySelector('input');

//chat button toggeler

chatBtn.addEventListener('click', () => {
    popup.classList.toggle('show');
})

//send message

submitbtn.addEventListener('click', () => {
    let userInput = inputElm.value;
    console.log(userInput)

})