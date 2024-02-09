import { useState, useContext } from "react";
import { Link } from "react-router-dom";
import NavBar from "../components/NavBar";
import { AuthContext } from "../components/AuthContext";

export default function Login() {
  const { setUser } = useContext(AuthContext); // Access setUser from AuthContext
  const [loginInfo, setLoginInfo] = useState({ username: "", password: "" });
  
  
  const handleLoginChange = (e) => {
    setLoginInfo({ ...loginInfo, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(loginInfo),
    })
      .then((r) => {
        if (!r.ok) {
          throw new Error("Login failed");
        }
        return r.json();
      })
      .then((data) => {
        localStorage.setItem("user", JSON.stringify(data)); 
        setUser(data);
      })
      .catch((e) => {
        console.error(e);
      });
  };

  return (
    <main>
      {/* <NavBar /> */}
      <div></div>
      <div className="loginMain">
        <div className="logoContainer"></div>
        <div className="titleContainer">
          <h1 className="loginTitle">Time Capsule Login</h1>
        </div>
        <form className="loginForm" onSubmit={handleSubmit}>
          <div className="loginPage">
            <label htmlFor="username">Username: </label>
            <input
              value={loginInfo.username}
              id="username"
              name="username"
              onChange={handleLoginChange}
            />
          </div>
          <div className="loginPage">
            <label htmlFor="password">Password: </label>
            <input
              value={loginInfo.password}
              type="password"
              id="password"
              name="password"
              onChange={handleLoginChange}
            />
            <div>
              <input className="button" type="submit" value="Login" />
            </div>
          </div>
        </form>
        <p className="font">
          Don't have an account? <Link to="/sign_up" className="links">Sign Up</Link>
        </p>
      </div>
    </main>
  );
}
