const menu = document.querySelector("#mobile-menu")
const menuLinks = document.querySelector(".navbar__menu")

menu.addEventListener('click', function(){
    menu.classList.toggle("is-active");
    menuLinks.classList.toggle("active");
});


function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

$("#Cards").on("click",function() {
    console.log("Test")
    console.log(this.hash);
});



// $(".main__button a").click(function (e) {
//         // alert("Hello!");
//         console.log("test");
//         console.log(this.hash)
//         if (this.hash !== '') {
//             e.preventDefault();
//             const hash = this.hash;
//             console.log("test")
//             $('html, body')
//             .animate({
//                 scrollTop: $(hash).offset().top
//                 },800);
//   }
// });

function notify_error(letters) {
  Toastify({
    text: letters,
    duration: 3000,
    destination: "#contact",
    newWindow: false,
    close: false,
    gravity: "bottom", // `top` or `bottom`
    position: "center", // `left`, `center` or `right`
    stopOnFocus: true, // Prevents dismissing of toast on hover
    className: "Toastify",
    style: {
         background: "linear-gradient(to right, #9e3434, #e66431)",
      // background: "linear-gradient(to right, #00b09b, #96c93d)",
    },
    onClick: function(){} // Callback after click
  }).showToast();
}

function notify_success(letters) {
  Toastify({
    text: letters,
    duration: 3000,
    destination: "#contact",
    newWindow: false,
    close: false,
    gravity: "bottom", // `top` or `bottom`
    position: "center", // `left`, `center` or `right`
    stopOnFocus: true, // Prevents dismissing of toast on hover
    className: "Toastify",
    style: {
      background: "linear-gradient(to right, #00b09b, #96c93d)",
      //  background: "linear-gradient(to right, #9e3434, #e66431)",
    },
    onClick: function(){} // Callback after click
  }).showToast();
}

async function sendContact(ev) {
    ev.preventDefault();

    const senderEmail = document
      .getElementById('emailInput').value;
    const senderMessage = document
      .getElementById('messageInput').value;
    const senderName = document
      .getElementById('nameInput').value;

    const webhookBody = {
      content: "ALERT: <@471639809962672129>",
      embeds: [{
        title: 'Message From Website',
        fields: [
          { name: 'Name:', value: senderName },
          { name: 'Contact Details:', value: senderEmail },
          { name: 'Message:', value: senderMessage }
        ]
      }],
    };

 

    const webhookUrl = 'https://discord.com/api/webhooks/947226543179042846/gLmI3HwzfaCRjkEUOqbrsSdhkvyuanN1Thu4VtW3P1w4nV0o99-Qkw6sviyZWqA80Tsn';

    const response = await fetch(webhookUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(webhookBody),
    });

    if (response.ok) {
      notify_success("I have received your message!")
      document.getElementById("messageInput").value = "";
      document.getElementById("emailInput").value = "";
      document.getElementById("nameInput").value = "";
      // alert('I have received your message!');
    } else {
      const webhookBody = {
        content: "ALERT: <@471639809962672129>",
        embeds: [{
          title: 'Contact Form Submitted',
          fields: [
            { name: 'Name', value: senderName },
            { name: 'Message', value: senderMessage }
          ]
        }],
      };
  
      const webhookUrl = 'https://discord.com/api/webhooks/947226543179042846/gLmI3HwzfaCRjkEUOqbrsSdhkvyuanN1Thu4VtW3P1w4nV0o99-Qkw6sviyZWqA80Tsn';
      

      const response1 = await fetch(webhookUrl, {
        method: 'POST',
        headers: {

          'Content-Type': 'application/json',
        },
        body: JSON.stringify(webhookBody),
      });
      if (response1.ok) {
        notify_success("I have received your message!")
        document.getElementById("messageInput").value = "";
        document.getElementById("emailInput").value = "";
        document.getElementById("nameInput").value = "";
        // alert('I have received your message!');
      } else {
        notify_error("There was an error! Try again later!")
        // alert('There was an error! Try again later!');
    }
  }
}
