async function sendMessage(){

const message=document.getElementById("message").Value;

const response=await
fetch("https://Industrial_AI_System.onrender.com/chat",{

method:"POST",

headers:{"Content-Type":"application/json"
},

body:JSON.stringify({
message:message
})

});

const data=await response.json();

document.getElementById("reply").innerText=data.reply;

}