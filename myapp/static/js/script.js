function emailSend(){
   // window.alert("hii");
   var userName= document.getElementById('first_name').value;
   var phone=document.getElementById('phone_input').value;
   var email=document.getElementById('email_addr').value;

var messageBody="Name "+ userName+"<br/> Phone "+ phone + "<br/> Email " + email;
   Email.send({
    Host : "smtp.elasticemail.com",
    Username : "shrutishukla6140@gmail.com",
    Password : "12FD304EA9BB9167603A1B5A2A34F92F8C9A",
    To : 'snapit.lko@gmail.com',
    From : "shrutishukla6140@gmail.com",
    Subject : "This is the subject",
    Body : messageBody
}).then(
  message => alert(message)
);
}

 