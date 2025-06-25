import React, { useEffect, useState } from 'react';
import './loginPage.css'
import { useNavigate } from 'react-router-dom';

function LoginUser() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();


    const handleSubmit=async(e)=>{
        e.preventDefault();
        try{
            const response = await fetch('http://localhost:5000/user/login', {
                method:'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body: JSON.stringify({
                    username: username,
                    password: password
                })

            })
            // const res=response.text();
            // console.log(response,response.ok ,response.status ,"response of login");
            if(response.ok || response.status === 200){ 
                // alert("Login Successful");
                navigate('/user-profile')
            }
        }
        catch(e){
            alert("Error occurred, Try again")
        }
    }
    useEffect(() => {
    if (username) {
      sessionStorage.setItem('username', username);
    }
  }, [username]);
    return (
    <div className="login-page">
        <div className='login-container'>
            <h1 className='login-title'>Login</h1>
            <form className='login-form' onSubmit={handleSubmit}>
                <div className='login-info'>
                    <span>Enter User Email:</span> 
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
                <button type="submit" className='login-button'>Login</button>
            </form>
            <p className='login-footer'>Don't have an account? <a href="/register" style={{color:"grey"}}>Register here</a></p>

        </div>
    </div>
  )
}

export default LoginUser;
