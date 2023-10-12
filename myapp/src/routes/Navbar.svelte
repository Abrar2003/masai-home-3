<script>
  let isSignup = true;

  function toggleForm(event) {
    event.preventDefault();
    isSignup = !isSignup;
  }
</script>

<nav class="navbar navbar-expand-lg navbar-light ">
  <a class="navbar-brand" href="/">
    <img
      src={"https://masai-website-images.s3.ap-south-1.amazonaws.com/logo.png"}
      alt="SvelteKit"
    /></a
  >
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
    <form class="form-inline my-2 my-lg-0">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit"
        >REFER & EARN</button
      >
      <!-- <button class="btn btn-outline-success my-2 my-sm-0" type="submit">SIGN UP</button> -->
      <button
        class="btn btn-primary"
        type="button"
        data-bs-toggle="offcanvas"
        data-bs-target="#offcanvasRight"
        aria-controls="offcanvasRight">SIGN UP</button
      >

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
            {:else}
            <p id="offcanvasRightLabel">Sign In</p>
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
          {:else}
            <h6>
              New User? <a href="/" on:click={toggleForm}
                >Sign up</a
              >
            </h6>
          {/if}
        </div>

        <div class="offcanvas-body2">
        </div>
        <div class="offcanvas-body">
            {#if isSignup}
              <!-- Signup Form -->
              <form>
                <div class="mb-3">
                  <label for="exampleInputEmail1" class="form-label"
                    >Full Name<p class="requiredred">*</p></label
                  >
                  <input
                    type="email"
                    class="form-control"
                    id="exampleInputEmail1"
                    aria-describedby="emailHelp"
                  />
                  <!-- <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div> -->
                </div>
                <div class="mb-3">
                  <label for="exampleInputEmail1" class="form-label"
                    >Email address<p class="requiredred">*</p></label
                  >
                  <input
                    type="email"
                    class="form-control"
                    id="exampleInputEmail1"
                    aria-describedby="emailHelp"
                  />
                  <!-- <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div> -->
                </div>
                <div class="mb-3">
                  <label for="exampleInputPassword1" class="form-label"
                    >Phone Number<p class="requiredred">*</p></label
                  >
                  <input
                    type="password"
                    class="form-control"
                    id="exampleInputPassword1"
                  />
                </div>
                <button type="submit" class="btn btn-primary btn-submit"
                  >Submit</button
                >
              </form>
            {:else}
              <!-- Signin Form -->
              <form>
                
                <div class="mb-3">
                  <label for="exampleInputPassword1" class="form-label"
                    >Phone number or email address<p class="requiredred">*</p></label
                  >
                  <input
                    type="password"
                    class="form-control"
                    id="exampleInputPassword1"
                    required
                  />
                </div>
                <button type="submit" class="btn btn-primary btn-submit"
                  >Continue</button
                >
              </form>
            {/if}
          </div>
          
      </div>
    </form>
  </div>
</nav>

<style>
    
  .nav-item{
        display: flex;
        margin: 10px;
        font-size: 16px;
        
        font-weight: 600 !important;
        font-family: "Open Sans", ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
    }
    /* .navbar-collapse{
        display: flex;
        justify-content: space-between;

    } */
    .navbar-nav{
        margin-left: 100px;
    }
    .form-inline{
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
  .form-control {
    width: 90%;
    height: 45px;
    border-radius: 8px;
  }
  .mb-3 {
    font-size: 14px;
    font-weight: bold;
    font-family: "Open Sans", ui-sans-serif, system-ui, -apple-system,
      BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial,
      "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
      "Segoe UI Symbol", "Noto Color Emoji";
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
</style>
