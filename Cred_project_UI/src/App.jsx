import { useState } from 'react'
import './App.css'
import LoginUser from './Pages/LoginPage'
import { Routes, Route, Navigate } from "react-router";
import { BrowserRouter as Router } from "react-router-dom";
import RegisterUser from './Pages/RegisterPage';
import UserView from './Pages/ViewPage';

function App() {
  const [count, setCount] = useState(0)

  return (
    <Router>
      <Routes>
        <Route path="/login" element={ <LoginUser />}/>
        <Route path="/" element={<RegisterUser/>} />
        <Route path="/register" element={<RegisterUser/>} />
        <Route path="/user-profile" element={<UserView/>} />
        {/* Add more routes as needed */}
      </Routes>
    </Router>
  )
}

export default App
