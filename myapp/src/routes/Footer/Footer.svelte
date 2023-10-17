<script>
  import BottomFooter from "./BottomFooter.svelte";
  import CopyRight from "./CopyRight.svelte";
  import MiddleFooter from "./MiddleFooter.svelte";
  import TechStacks from "./TechStacks.svelte";

  let isMedia = 460;
</script>

<div class="mas-msguru-maisai-footer-main">
  <div class="masai-footer">
    <!-- Top -->
    <div>
      <div class="masai-top-footer" class:media={isMedia}>
        <img
          src="https://masaischool.com/images/footer/arrow-gif.gif"
          alt="Footer Arrow Logo"
        />
        <div class="masai-get-started">
          <span>Get Started</span>
          <span>Join the Program </span>
        </div>
        <button class="masai-get-dream-job">Get your dream job</button>
      </div>
    </div>
    <hr />
    <!-- Middle -->
    <div class="masai-reverse">
      <div>
        <MiddleFooter />
      </div>

      <hr class="masai-social-hr-line" />
      <!-- Bottom -->
      <div>
        <TechStacks />
        <BottomFooter />
      </div>
    </div>
    <CopyRight />
  </div>
</div>

<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    /* font-family: Helvetica Neue, Helvetica, Arial, sans-serif; */
    font-family: Open Sans, ui-sans-serif, system-ui, -apple-system,
      BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans,
      sans-serif, "Apple Color Emoji", "Segoe UI Emoji", Segoe UI Symbol,
      "Noto Color Emoji";
  }
  hr {
    border: 0.5px solid rgb(247, 176, 176);
  }
  .mas-msguru-maisai-footer-main{
    background-color: rgb(0, 0, 0);
    width: 100%;
    /* height: 500px; */

  }
  .masai-footer {
    color: white;
    max-width: 1138px;
    margin: auto;
    background-color: rgb(0, 0, 0);
  }
  .masai-top-footer {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    padding: 15px 0px;
  }
  .masai-top-footer > img {
    width: 96px;
    height: 96px;
  }
  .masai-get-started {
    display: flex;
    flex-direction: column;
    text-align: center;
  }
  .masai-get-started > span:first-child {
    font-weight: 600;
    color: white;
    font-size: 24px;
  }
  .masai-get-started > span:last-child {
    font-size: 1rem;
    color: #ffdb66;
    font-weight: 600;
  }
  .masai-get-dream-job {
    background-color: red;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    cursor: pointer;
    border-radius: 5px;
    padding: 12px 25px;
    border: none;
    color: white;
    font-size: 1rem;
  }

  /* ------------------------------------------------- */

  .masai-middle-footer {
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

  .masai-reverse {
    display: flex;
    flex-direction: column;
  }

  /* ----------------------------------------- */
  /* Media Queries */
  /* ----------------------------------------- */
  @media screen and (max-width: 768px) {
  }

  @media screen and (max-width: 1020px) {
    .masai-middle-footer-disable {
      display: none;
    }
    .media > img,
    .masai-logo > img,
    .followMe,
    .media > img {
      display: none;
    }
    .masai-reverse {
      flex-direction: column-reverse;
    }
  }

  @media screen and (max-width: 460px) {
    .media {
      flex-direction: column;
    }

    .masai-social-media {
      width: 100%;
      /* border: 1px solid red; */
      gap: 2rem;
      flex-wrap: wrap;
    }
    .masai-logo {
    }
  }
</style>
