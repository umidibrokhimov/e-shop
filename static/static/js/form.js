let form = document.querySelector('#form-contact');

form.addEventListener('submit', (e)=> {
    e.preventDefault()
    
    fullname = form.querySelector('#name')
    email = form.querySelector('#email')
    subject = form.querySelector('#subject')
    message = form.querySelector('#message')
    
    let my_text = `New user is: %0A - Fullname: ${fullname.value} %0A - Email: ${email.value} %0A - Subject: ${subject.value} %0A - Text: ${message.value}`
    
    let token = '5364201856:AAG9P3GruT17uqf0YEOsCC52vI1SapIuwSo';
    let chat_id = -1001640322912
    
    let url = `https://api.telegram.org/bot${token}/sendMessage?chat_id=${chat_id}&text=${my_text}`
    
    let api = new XMLHttpRequest()
    api.open("GET", url, true)
    api.send()

    fullname.value = ''
    email.value = ''
    subject.value = ''
    message.value = ''
})