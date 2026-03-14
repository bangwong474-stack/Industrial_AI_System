async function login(){

const email=document.getElementById("email").value;
const password=document.getElementById("password").value;

const response=await
fetch("https://industrial-ai-system.onrender.com/login",{

method:"POST",

headers:{"Content-Type":"application/json"
},

body:JSON.stringify({
email:email,
password:password
})

});

const data=await response.json();

document.getElementById("result").innerText=data.message;

}