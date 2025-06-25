import React, { useEffect, useState } from 'react';
import './register.css'
import { useNavigate } from 'react-router-dom';

function RegisterUser() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [name,setName]=useState('');
     useEffect(() => {
    if (username) {
      sessionStorage.setItem('username', username);
    }
  }, [username]);
    const navigate = useNavigate();
    const handleSubmit=async(e)=>{
        e.preventDefault();
        try{
            const response = await fetch('http://localhost:5000/user/signup', {
                method:'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body: JSON.stringify({
                    name: name,
                    username: username,
                    email: email,
                    password: password
                })

            })
            // const res=response.text();
            console.log(response);
            if(response.ok){ 
                // alert("Register Successful");
                navigate('/login')
            }
        }
        catch(e){
            alert("Error occurred, Try again")
        }
    }
    return (
    <div className="login-page">
        <div className='login-container'>
            <h1 className='login-title'>Sign In</h1>
            <form className='login-form' onSubmit={handleSubmit}>
                <div className='login-info'>
                    <span>Enter Name:</span> 
                    <input
                        className='login-input'
                        type="text"
                        placeholder="Username"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                    />
                </div>
                <div className='login-info'>
                    <span>Enter User Name:</span> 
                    <input
                        className='login-input'
                        type="text"
                        placeholder="Username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div className='login-info'>
                    <span>Enter User Email:</span> 
                    <input
                        className='login-input'
                        type="text"
                        placeholder="User Email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div className='login-info'>
                    <span>Enter Password:</span>
                    <input
                        className='login-input'
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit" className='login-button'>Signin</button>
            </form>
            <p className='login-footer'>Already have an account? <a href="/login" style={{color:"grey"}}>login</a></p>

        </div>
    </div>
  )
}

export default RegisterUser;
