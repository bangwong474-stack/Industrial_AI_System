const express=require("express");
const bodyParser=require("body-parser");
require('dotenv').config();

const app=express();
app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());

const PORT=process.env.PORT||3000;

let user=[];

app.post('/signup',(req,res)=>{const{email,password}=req.body;if(!email||!password)
return res.status(400).send('Fill all fields');const exist=users.find(u=> u.email===email);
if(exist) return res.status(400).send('User exists');users.push({email,password});
res.send('sign up successfully');});


app.post('/login',(req,res)=>{const{email,password}=req.body;
const user=users.find(u=>u.email===email & u.password===password);
if(!user)return res.status(401).send('Invalid credentials');
res.send('Login successfully');});

app.listen(PORT,()=>console.log(`Server running on http://localhost:${PORT}`));

app.get("/",(req,res)=>{res.send("Industrial AI system is live")});