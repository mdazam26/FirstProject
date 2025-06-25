import React, { useEffect, useState } from 'react';
import './viewpage.css'
import { useNavigate } from 'react-router-dom';
import { FiLogOut } from 'react-icons/fi';
import { MdDelete } from "react-icons/md";
import { MdEdit } from "react-icons/md";

function UserView() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [id, setId] = useState('');
    const [userData, setUserData] = useState(null);
    const [edit,setEdit] = useState(false);
    const [names,setNames]=useState('');
    const navigate = useNavigate();
    
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`http://localhost:5000/user/getall`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ username: sessionStorage.getItem('username') })
                });

                if (!response.ok) {
                    throw new Error('Network response was not OK');
                }

                const data = await response.json(); 
                // setUserData(data); 
                console.log("Response Data:", data.email,'----',response);
                setEmail(data.email);
                setUsername(data.username);
                setPassword(data.password);
                setId(data.id);
                setNames(data.name);
                // console.log("User Data:", email, username);
                if (response.status != 200) {
                    navigate('/login');
                }
            } catch (error) {
                console.error("Fetch error:", error);
                // alert("Error occurred, Try again");
                // navigate('/login');
            }
        };

        fetchData(); 
    }, [username]); 
    const handleDelete=(id)=>{  
        const response = fetch(`http://localhost:5000/user/delete/${id}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        console.log("Delete Response:", response);
        navigate('/register');``
    }
    const   handleEditButton=()=>{
        const response = fetch(`http://localhost:5000/user/update`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: id,
                name: names,
                username: username,
                email: email,
                password: password
            })
        })
        console.log("Edit Response:", response);
        setEdit(false);
        // navigate('/user-profile');
    }


    return (
    <div className="login-page">
        <div className='login-container'>
            <div className='logout-icon' onClick={()=>navigate("/login")}> <FiLogOut /> Logout</div>
            <h1 className='login-title'>Page View </h1>
            <span>{username}</span>
            {/* <span>{email}</span>
            <span>{password}</span> */}
            <div className='delete-icon'> <MdEdit color="blue" onClick={()=>setEdit(true)}/> <MdDelete color='red'  onClick={() => handleDelete(id)}/></div>
            <form className='login-form' >
                <div className='login-info'>
                    <span>Name:</span>
                    {edit?<input
                        className='login-input'
                        type="text"
                        placeholder="Nam"
                        value={names}
                        onChange={(e) => setNames(e.target.value)}
                        required
                    />:names}
                </div>
                <div className='login-info'>
                    <span>User Name:</span> 
                    {edit?<input
                        className='login-input'
                        type="text"
                        placeholder="Username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />:username}
                </div>
                <div className='login-info'>
                    <span>User Email:</span> 
                    {edit?<input
                        className='login-input'
                        type="text"
                        placeholder="User Email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />:email}
                </div>
                <div className='login-info'>
                    <span>Password:</span>
                    {edit?<input
                        className='login-input'
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />:"*******"}
                </div>
               { edit ?<button type="submit" className='login-button' onClick={()=>handleEditButton()}>Save</button>:""}
            </form>

        </div>
    </div>
  )
}

export default UserView;
