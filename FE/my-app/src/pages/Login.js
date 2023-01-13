export default function Login() {
  return (
      <div className="container mt-4">
          <h2>Login Form</h2>
          <form method="post" id="login_form">
              <div className="form-outline mb-4">
                  <input type="email" id="email" name="email" className="form-control" />
                  <label className="form-label" for="email">Email address</label>
              </div>

              <div className="form-outline mb-4">
                  <input type="password" id="password" name="password" className="form-control" />
                  <label className="form-label" for="password">Password</label>
              </div>
              <button type="submit" className="btn btn-primary btn-block mb-4">Log In</button>
              <p> 
                  Don't have account? <br />
                  <a href="/register">Sign up here</a>
              </p>
          </form>
      </div>
  );
};
  