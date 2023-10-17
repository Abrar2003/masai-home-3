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
      const token = JSON.parse(localStorage.getItem("token"))
      return token.name
    }
  
    onMount(() => {
      signedUser = getName();
    });
  </script>




<div class="nav-container">
    <div class="nav-head">
        <div class="nav-head">
            <p class="head-p">
              Applications for our 6th November Batches are now open!
            </p>
            <button class="applynow-btn">APPLY NOW</button>
          </div>
    </div>
    <div class="nav-main">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
            <a class="navbar-brand" href="/">
                <img
                  class="logo-img"
                  src={"https://masai-website-images.s3.ap-south-1.amazonaws.com/logo.png"}
                  alt="SvelteKit"
                /></a>
                

          
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav mr-auto">
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
          </nav>
          <div>
            <form class="form-inline my-2 my-lg-0 form-main">
                
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

    </div>
</div>


<style>

    .nav-main{
        display: flex;
        max-width: 1280px;
        margin: auto;
        justify-content: space-evenly;
        align-items: center;
    }

    @media (max-width: 768px) {
        .nav-main{
            display: flex;
            justify-content: space-evenly;
        }
        nav{
            display: flex;
            /* flex-wrap: wrap-reverse; */
            /* width: ; */
            border: 1px solid red;
        }
        .navbar-toggler{
            width: 30px;
        }
        .navbar-toggler-icon{
            width:30px;
        }
        .form-main{

        }
        .refer-btn{
            width: 50%;
        }
        .signin-btn{
            width: 50%;
        }
    }
</style>