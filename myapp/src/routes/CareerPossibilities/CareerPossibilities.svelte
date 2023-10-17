<script>
  import Button from "../Button/Button.svelte";
  let videoUrl =
    'https://www.youtube.com/embed/dmavmvfXbGA?si=nwcPwsupjPs1MnC9';
</script>

<div>
  <div class="msguru-masai-careed-possibilities-main">
    <div class="msguru-masai-careed-possibilities-left">
      <h3>
        <span
          >Elevate
          <img
            src="https://masaischool.com/images/new-homepage/yellow-vector.svg"
            alt=""
          />
        </span>Your Career Possibilities
      </h3>

      <p class="msguru-masai-careed-possibilities-left-top-matter">
        It doesn’t matter where you come from, we know how to get you to your
        dream career.
      </p>

      <p>
        Our graduates consistently outperform students from top Indian
        engineering colleges & universities. 70% of companies who have hired 1
        Masai graduate come back to us with their hiring mandates.
      </p>

      <Button buttonData={"Apply Now"} />
    </div>

    <div class="msguru-masai-careed-possibilities-right">
      <!-- <img
        src="https://masaischool.com/images/new-homepage/nsdc/nsdc-cert.jpg"
        alt=""
      /> -->
      <iframe
  width="560"
  height="315"
  src={videoUrl}
  title="YouTube video player"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  allowfullscreen
></iframe>
    </div>
  </div>
</div>

<!-- <iframe
  width="950"
  height="534"
  src="https://www.youtube.com/embed/BwOxMY6DGtY?list=RDBwOxMY6DGtY"
  title="Clara Mae - Not Sad Anymore"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  allowfullscreen
/> -->

<style>
  .msguru-masai-careed-possibilities-main {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    /* width: 90%; */
    /* margin: auto; */
    max-width: 1280px;
    margin: auto;
    padding: 25px 0px;
  }

  .msguru-masai-careed-possibilities-left {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    text-align: left;
  }

  .msguru-masai-careed-possibilities-main > div {
    width: 100%;
  }

  .msguru-masai-careed-possibilities-left > h3 {
    font-size: 30px;
    font-weight: 700;
  }

  .msguru-masai-careed-possibilities-left > h3 > span {
    color: red;
    position: relative;
  }

  .msguru-masai-careed-possibilities-left > h3 > span > img {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100px;
  }

  .msguru-masai-careed-possibilities-right {
    width: 100%;
  }

  .msguru-masai-careed-possibilities-left-top-matter {
    font-weight: 600;
    font-size: 24px;
  }

  .msguru-masai-careed-possibilities-right > iframe {
    width: 100%;
  }
  @media screen and (max-width: 850px) {
    .msguru-masai-careed-possibilities-main {
      grid-template-columns: repeat(1, 1fr);
    }
    .msguru-masai-careed-possibilities-left {
      text-align: center;
      margin-bottom: 1rem;
      gap: 8px;
    }
    .msguru-masai-careed-possibilities-left-top-matter{
      line-height:1.7rem ;
    }
  }
</style>
