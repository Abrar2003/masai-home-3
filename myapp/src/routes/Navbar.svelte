<script>
  import axios from "axios";
  import { onMount } from "svelte";
  let isSignup = true;
  let isSignin = true;

  function toggleForm(event) {
    event.preventDefault();
    isSignup = !isSignup;
  }

  function toggleEdit(event) {
    event.preventDefault();
    isSignin = !isSignin;
    showOtpForm = false;
  }
  let signedUser = "";
  let email = "";
  let fullname = "";
  let mobileNumber = "";
  let otp = "";
  let emailOrMobile = "";
  let showSignupForm = true;
  let showOtpForm = false;
  let showError = false;
  let showFullnameError = false;
  let showEmailError = false;
  let showMobileError = false;

  function handleInputChange() {
    if (emailOrMobile.length === 10 || validateEmail(emailOrMobile)) {
      showError = false;
    } else {
      showError = true;
    }
  }
  function handleFullnameChange() {
    if (fullname.length > 3) {
      showFullnameError = false;
    } else {
      showFullnameError = true;
    }
  }
  function handleEmailChange() {
    if (validateEmail(email)) {
      showEmailError = false;
    } else {
      showEmailError = true;
    }
  }

  function validateEmail(input) {
    return input.includes("@");
  }

  function handleMobileChange() {
    if (mobileNumber.length === 10) {
      showMobileError = false;
    } else {
      showMobileError = true;
    }
  }

  async function handleSignupSubmit() {
    if (mobileNumber.length === 10 || validateEmail(email)) {
      isSignup = false;
      isSignin = false;
      showOtpForm = true;
      showFullnameError = false;
      showEmailError = false;
      showMobileError = false;
    } else {
      showFullnameError = true;
      showEmailError = true;
      showMobileError = true;
    }
    emailOrMobile = email;
    try {
      let res = await axios.post(
        "http://aalam003.pythonanywhere.com/auth/register",
        {
          full_name: fullname,
          email: email,
          phone: mobileNumber,
        }
      );
      alert(`Your OTP is ${res.data.otp}`);
    } catch (error) {
      alert(`please login ${error.response.data.message}`);
    }
  }

  async function handleSigninSubmit() {
    if (emailOrMobile.length === 10 || validateEmail(emailOrMobile)) {
      isSignup = false;
      isSignin = false;
      showOtpForm = true;
      showError = false;
    } else {
      showError = true;
    }
    try {
      let res = await axios.post(
        "http://aalam003.pythonanywhere.com/auth/login",
        {
          key: emailOrMobile,
        }
      );
      alert(`Your OTP is ${res.data.otp}`);
    } catch (error) {
      alert(error.response.data.message);
    }
  }

  async function handleOtpSubmit() {
    // window.location.href = '/';
    try {
      let res = await axios.post(
        "http://aalam003.pythonanywhere.com/auth/verify",
        {
          key: email || emailOrMobile,
          otp: otp,
        },
        {
          withCredentials: true,
        }
      );
      signedUser = res.data.name;
      localStorage.setItem("token", JSON.stringify(res.data));
      alert(`${res.data.message} ${res.data.name}`);
    } catch (error) {
      alert(error.response.data.message);
    }
  }
  function getName() {
    const token = JSON.parse(localStorage.getItem("token"));
    return token.name;
  }

  onMount(() => {
    signedUser = getName();
  });
</script>

<div class="tp">
  <div class="nav-head">
    <p class="head-p">
      Applications for our 6th November Batches are now open!
    </p>
    <button class="applynow-btn">APPLY NOW</button>
  </div>
  <div class="nav-container">
    <nav class="navbar navbar-expand-lg navbar-light">
      <div class="logo-head">
        <div class="hambugrer-msguru-masai">
          <button
            class="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon" />
          </button>
          <a class="navbar-brand" href="/">
            <img
              src={"https://masai-website-images.s3.ap-south-1.amazonaws.com/logo.png"}
              alt="SvelteKit"
            /></a
          >
        </div>

        <!-- ----------------------------Mobile Responsive Login Signup----------------------------------- -->

        <div class="mobile-form">
          <button
              class="btn btn-outline-success my-2 my-sm-0 refer-btn"
              type="submit">REFER & EARN</button
            >
            <!-- <button class="btn btn-outline-success my-2 my-sm-0" type="submit">SIGN UP</button> -->
            {#if !signedUser}
              <button
                class="btn btn-primary signup-btn"
                type="button"
                data-bs-toggle="offcanvas"
                data-bs-target="#offcanvasRight"
                aria-controls="offcanvasRight"
                style="text-transform: uppercase;">sign up</button
              >
              <!--  -->
              <!-- <p class="signed-user-name-msguru-masai">Guru Prasad</p> -->
            {:else}
              <button
                class="btn btn-primary signup-btn signed-user-name-msguru-masai"
                type="button"
                aria-controls="offcanvasRight">{signedUser}</button
              >
              <!-- <p class="signed-user-name-msguru-masai">{signedUser}</p> -->
            {/if}
        </div>


        <!-- ----------------------------Mobile Responsive Login Signup----------------------------------- -->
      </div>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <!-- <li class="nav-item active">
          <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
        </li> -->
          <li class="nav-item">
            <a class="nav-link" href="/">COURSES</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/">FEES</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/">EVENTS</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/">LEARN</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/">SUCCESS STORIES</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/">HIRE FROM US</a>
          </li>
        </ul>
      </div>

      <!-- ----------------------------Desktop Responsive Login Signup----------------------------------- -->
      <div class="desktop-form">
        <button
            class="btn btn-outline-success my-2 my-sm-0 refer-btn"
            type="submit">REFER & EARN</button
          >
          <!-- <button class="btn btn-outline-success my-2 my-sm-0" type="submit">SIGN UP</button> -->
          {#if !signedUser}
            <button
              class="btn btn-primary signup-btn"
              type="button"
              data-bs-toggle="offcanvas"
              data-bs-target="#offcanvasRight"
              aria-controls="offcanvasRight"
              style="text-transform: uppercase;">sign up</button
            >
            <!--  -->
            <!-- <p class="signed-user-name-msguru-masai">Guru Prasad</p> -->
          {:else}
            <button
              class="btn btn-primary signup-btn signed-user-name-msguru-masai"
              type="button"
              aria-controls="offcanvasRight">{signedUser}</button
            >
            <!-- <p class="signed-user-name-msguru-masai">{signedUser}</p> -->
          {/if}
      </div>
      <div class="desktop-form-signin">
        <form class="form-inline my-2 my-lg-0">
          
          <div
            class="offcanvas offcanvas-end"
            tabindex="-1"
            id="offcanvasRight"
            aria-labelledby="offcanvasRightLabel"
          >
            <div class="offcanvas-header">
              <div class="offcanvas-header">
                <div class="offcanvas-head1">
                  {#if isSignup}
                    <p id="offcanvasRightLabel">Create Account</p>
                  {:else if isSignin}
                    <p id="offcanvasRightLabel">Sign In</p>
                  {:else}
                    <!-- <p>Enter OTP</p> -->
                  {/if}
                </div>
              </div>

              <button
                type="button"
                class="btn-close text-reset"
                data-bs-dismiss="offcanvas"
                aria-label="Close"
              />
            </div>
            <!-- <div class="offcanvas-head2">
        <h6>Already have an account? <a href="/">Sign in</a></h6>
      </div> -->
            <div class="offcanvas-head2">
              {#if isSignup}
                <h6>
                  Already have an account? <a href="/" on:click={toggleForm}
                    >Sign in</a
                  >
                </h6>
              {:else if isSignin}
                <h6>
                  New User? <a href="/" on:click={toggleForm}>Sign up</a>
                </h6>
              {:else}
                <h6 />
              {/if}
            </div>

            <div class="offcanvas-body2" />
            <div class="offcanvas-body">
              {#if isSignup}
                <!-- Signup Form -->
                <form on:submit|preventDefault={handleSignupSubmit}>
                  <div class="mb-3">
                    <label for="exampleInputname1" class="form-label"
                      >Full Name
                      <p class="requiredred">*</p></label
                    >
                    <input
                      type="text"
                      class="form-control"
                      id="exampleInputname1"
                      aria-describedby="emailHelp"
                      bind:value={fullname}
                      on:input={handleFullnameChange}
                      required
                    />
                    {#if showFullnameError}
                      <p class="errortag">Please enter a valid name</p>
                    {/if}
                    <!-- <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div> -->
                  </div>
                  <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label"
                      >Email address
                      <p class="requiredred">*</p></label
                    >
                    <input
                      type="email"
                      class="form-control"
                      id="exampleInputEmail1"
                      aria-describedby="emailHelp"
                      bind:value={email}
                      on:input={handleEmailChange}
                      required
                    />
                    {#if showEmailError}
                      <p class="errortag">Please enter a valid email</p>
                    {/if}
                    <!-- <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div> -->
                  </div>
                  <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label"
                      >Phone Number
                      <p class="requiredred">*</p></label
                    >
                    <input
                      type=""
                      class="form-control"
                      id="exampleInputPassword1"
                      bind:value={mobileNumber}
                      on:input={handleMobileChange}
                      required
                    />
                    {#if showMobileError}
                      <p class="errortag">Please enter a valid mobile</p>
                    {/if}
                  </div>
                  <button type="submit" class="btn btn-primary btn-submit"
                    >Submit</button
                  >
                </form>
              {:else if isSignin}
                <!-- Signin Form -->
                <form on:submit|preventDefault={handleSigninSubmit}>
                  <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label"
                      >Phone number or email address
                      <p class="requiredred">*</p></label
                    >
                    <input
                      type=""
                      class="form-control"
                      id="exampleInputPassword1"
                      bind:value={emailOrMobile}
                      on:input={handleInputChange}
                      required
                    />
                    {#if showError}
                      <p class="errortag">Email or Phone is invalid</p>
                    {/if}
                  </div>
                  <button type="submit" class="btn btn-primary btn-submit"
                    >Continue</button
                  >
                </form>
              {/if}
              {#if showOtpForm}
                <br />
                <br />
                <br />
                <form on:submit|preventDefault={handleOtpSubmit}>
                  <h3>Verify Number</h3>
                  <br />
                  <!-- <h6 for="otp">Enter OTP sent to 1234567890 <button>Edit</button></h6> -->
                  {#if showOtpForm}
                    <h6>
                      Enter OTP sent to {emailOrMobile}
                      <a href="/" on:click={toggleEdit}>Edit</a>
                    </h6>
                  {:else}
                    <h6 />
                  {/if}
                  <br />
                  <input
                    class="form-control"
                    type="text"
                    id="otp"
                    bind:value={otp}
                    required
                  />
                  <br />
                  <br />
                  <button class="btn btn-primary btn-submit" type="submit"
                    >VERIFY</button
                  >
                </form>
              {/if}
            </div>
          </div>
        </form>
      </div>

      <!-- ----------------------------Desktop Responsive Login Signup End----------------------------------- -->
    </nav>
  </div>
</div>
<div class="filler" />

<style>
  .mobile-form{
    display: none;
  }
  .form-inline {
    display: flex;
    align-items: center;
  }
  .tp {
    position: fixed;
    top: 0px;
    background-color: white;
    z-index: 10;
    width: 100%;
  }
  .filler {
    height: 150px;
  }
  .nav-head {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    background-color: #fedfe5;
  }
  .nav-container {

    width: 1280px;
    margin: auto;
  }
  .nav-container > nav {
    display: flex;
    flex-direction: row;
  }
  .logo-head {
    /* border: 1px solid red; */
    display: flex;
  }
  .applynow-btn {
    background-color: #ed0331;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
  }

  .head-p {
    font-size: 17px;
    font-weight: bold;
    margin-top: 15px;
  }
  .nav-item {
    display: flex;
    margin: 10px;
    font-size: 16px;

    font-weight: 600 !important;
    font-family: "Open Sans", ui-sans-serif, system-ui, -apple-system,
      BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial,
      "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
      "Segoe UI Symbol", "Noto Color Emoji";
  }
  /* .navbar-collapse{
        display: flex;
        justify-content: space-between;

    } */
  .navbar-nav {
    margin-left: 100px;
  }
  .form-inline {
    /* border: 1px solid black; */
    padding: 5px;
    display: flex;
    justify-content: space-between;
  }
  .form-label {
    /* margin-left: -100px; */
    display: flex;
    justify-content: start;
  }
  .errortag {
    color: #ed0331;
    font-weight: 300;
    font-size: 15px;
  }
  .form-control {
    width: 90%;
    height: 45px;
    border-radius: 8px;
  }
  .navbar-brand>img{
    /* width: 100%; */
    width: 100px;
  }
  .mb-3 {
    font-size: 14px;
    font-weight: bold;
    font-family: "Open Sans", ui-sans-serif, system-ui, -apple-system,
      BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial,
      "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
      "Segoe UI Symbol", "Noto Color Emoji";
  }
  .signed-user-name-msguru-masai {
    border: none !important;
    color: black !important;
    font-weight: 500 !important;
    font-size: 1.2rem;
  }

  .offcanvas-head1 {
    text-align: center;
    width: 300px;
    display: flex;
    justify-content: center;
    font-size: 24px;
    font-weight: bold;
  }
  .requiredred {
    color: red;
    margin-top: 15px;
  }
  .offcanvas-head2 {
    /* margin-left: px; */
    /* border: 1px solid black; */
    display: flex;
    justify-content: center;
  }
  .btn-submit {
    width: 90%;
    height: 45px;
  }
  .signup-btn {
    color: #ed0331;
    border: 1px solid #ed0331;
    background-color: white;
    font-weight: 500;
    padding: 8px 16px;
    height: 50px;
    border-radius: 8px;
    margin-left: 15px;
    margin-right: 30px;
  }
  .refer-btn {
    border: none;
    background-color: #e5feff;
    color: rgba(5, 15, 32, 0.5);
    font-weight: 550;
    height: 45px;
    border-radius: 8px;
  }
  .navbar-toggler, .navbar-toggler-icon{
    outline: none;
    border: none;
  }

  @media (max-width: 768px) {
    .nav-head {
      display: flex;
      flex-wrap: wrap;
      text-align: center;
    }
    .applynow-btn {
      margin-top: -40px;
      margin-bottom: 10px;
    }
    nav {
      /* background-color: blue; */
      display: flex;
      flex-direction: row;
    }
    .logo-head {
      width: 15%;
    }

    /* .navbar-light{
  border: 1px solid rgb(229, 133, 133);
} */
    /* .logo-head{
  border:1px solid rgb(21, 129, 218);

} */
    .hambugrer-msguru-masai {
      display: flex;
      align-items: center;
    }

    .signup-btn {
      color: #ed0331;
      border: none;
      background-color: white;
      font-weight: 500;
      /* padding: 8px 16px; */
      height: 50px;
      border-radius: 8px;
      /* width: 30%; */
      margin: 0%;
    }
    .refer-btn {
      border: none;
      background-color: #e5feff;
      color: rgba(5, 15, 32, 0.5);
      font-weight: 550;
      height: 45px;
      border-radius: 8px;
      margin: 0%;
      /* width: 30%; */
    }
    .mobile-form{
    display:  flex;
    align-items: center;

  }
  .desktop-form{
    display: none;
  }
  }
  
  @media (max-width: 480px) {
    .logo-head {
      width: 5%;
      padding: 0;
      margin: 0;
    }
    .nav-container{
      border: 1px solid black;
      max-width: 480px ;
      padding: 0%;
    }
    .navbar-toggler, .navbar-toggler-icon{
    outline: none;
    border: none;
    max-width: 30px;
    margin-right: 20px;
  }
  nav{
    border: 1px solid red;
    padding: 0px 0px ;
  }

  .signup-btn {
      color: #ed0331;
      border: none;
      background-color: white;
      font-weight: 500;
      font-size: 12px;
      /* padding: 8px 16px; */
      height: 40px;
      border-radius: 8px;
      /* width: 30%; */
      margin: 0%;
    }
    .refer-btn {
      border: none;
      background-color: #e5feff;
      color: rgba(5, 15, 32, 0.5);
      font-weight: 550;
      font-size: 12px;
      padding-right: 40px;
      height: 35px;
      border-radius: 8px;
      margin: 0%;
      width: 50%;
      /* margin-left: -20px; */
    }
    /* .navbar-brand>img{
    width: 50px;
  } */
  }
</style>