<script>
  let isMedia = 460;
  export let disable = true;
</script>

<div>
  <div class="masai-middle-footer">
    <div class:masai-logo={isMedia}>
      <img
        class="masai-footer-logo-small"
        src="https://masaischool.com/images/footer/masai-logo-dark.svg"
        alt="Masai School Logo"
      />
    </div>
    <div class="masai-social-media">
      <p class:followMe={isMedia}>Follow us -</p>
      <a target="_blank" href="https://twitter.com/masaischool">
        <p><i class="bx bxl-twitter" /></p>
      </a>
      <a target="_blank" href="https://www.facebook.com/masaischool/">
        <p><i class="bx bxl-facebook-circle" /></p>
      </a>
      <a target="_blank" href="https://www.linkedin.com/company/masai-school/">
        <p><i class="bx bxl-linkedin-square" /></p>
      </a>
      <a href="https://www.linkedin.com/company/masai-school/">
        <p><i class="bx bxl-instagram" /></p>
      </a>
      <a target="_blank" href="https://github.com/masai-school">
        <p>
          <i class="bx bxl-github" />
        </p>
      </a>
      <a
        target="_blank"
        href="https://www.youtube.com/channel/UCENOACKQiqejXP-bb9sCnMg?view_as=subscriber"
      >
        <p>
          <i class="bx bxl-youtube" />
        </p>
      </a>
    </div>
  </div>
</div>

<style>
  .masai-middle-footer {
    /* height: 80px; */
    display: flex;
    align-items: center;

    justify-content: space-between;
    width: 90%;
    margin: auto;
    padding: 2rem 0rem;
  }
  .masai-footer-logo-small {
    cursor: pointer;
  }
  .masai-social-hr-line {
    width: 90%;
    margin: auto;
  }
  .masai-social-media {
    /* width: 35%; */
    gap: 1rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .masai-social-media > p {
    color: grey;
  }
  .masai-social-media > a {
    text-decoration: none;
    color: grey;
    font-size: 1rem;
  }
  .masai-social-media > a > p {
    font-size: 1.6rem;
    color: grey;
  }
  .masai-social-media > a > p:hover {
    color: white;
    transition: ease all 0.5s;
  }

  /* Media Queries */
  @media screen and (max-width: 1020px) {
    .followMe,
    .masai-logo > img {
      display: none;
    }
    .masai-social-media {
      margin: auto;
    }
  }
</style>
