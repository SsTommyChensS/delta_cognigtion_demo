import { Outlet, Link } from "react-router-dom";


const Layout = () => {
  return (
    <>
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <Link to="/" className="nav-link">Home</Link>
                </li>
                <li class="nav-item">
                    <Link to="/register" className="nav-link">Register</Link>
                </li>
                <li class="nav-item">
                    <Link to="/login" className="nav-link">Login</Link>
                </li>
            </ul>
        </div>
      </nav>

      <Outlet />
    </>
  )
};

export default Layout;