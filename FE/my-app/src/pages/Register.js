
export default function Register() {
    return (
        <div className="container mt-4">
            <h2>Register Form</h2>
            <form method="post" id="signup_form">
                <div className="form-outline mb-4">
                    <input type="email" id="email" name="email" className="form-control" />
                    <label className="form-label" for="email">Email address</label>
                </div>

                <div className="form-outline mb-4">
                    <input type="password" id="password" name="password" className="form-control" />
                    <label className="form-label" for="password">Password</label>
                </div>

                <div className="form-outline mb-4">
                    <input type="password" id="confirm_password" name="confirm_password" className="form-control" />
                    <label className="form-label" for="confirm_password">Confirm password</label>
                </div>
                <button type="submit" className="btn btn-primary btn-block mb-4">Sign up</button>
                <p> 
                    Aleady have an account? <br />
                    <a href="/login">Log in here</a>
                </p>
            </form>
        </div>
    );
};