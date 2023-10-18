<script>
  import StudentImpactLeft from "./StudentImpactLeft.svelte";
  import StudentImpactRight from "./StudentImpactRight.svelte";
</script>

<div class="main-msguru-masai-student-impact">
  <div class="msguru-creating-impact-masai">
    <h2>
      Our Students Are <span
        >Creating Impact <img
          src="https://masaischool.com/images/new-homepage/yellow-vector.svg"
          alt=""
        />
      </span>
    </h2>
  </div>
  <div class="msguru-masai-carousel-main">
    <div class="mainWind"><StudentImpactLeft /></div>
    <div class="mainWind"><StudentImpactRight /></div>
  </div>
</div>

<!-- <LefrSideSlider />
<RightSideSlider /> -->

<style>
  .main-msguru-masai-student-impact {
    /* border: 1px solid red; */
    max-width: 1280px;
    margin: auto;
    /* -webkit-font-smoothing: antialiased; */
  }
  .msguru-creating-impact-masai {
    padding: 2rem 0rem;
  }
  .msguru-creating-impact-masai > h2 {
    text-align: center;
    font-size: 1.9rem;
    font-weight: 700;
  }
  .msguru-creating-impact-masai > h2 > span {
    color: red;
    position: relative;
  }
  .msguru-creating-impact-masai > h2 > span > img {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 230px;
  }
  .msguru-masai-carousel-main {
    display: flex;
    align-items: center;
    justify-content: space-around;
    gap: 2rem;
    width: 100%;
    margin: auto;
    /* border: 1px solid red; */
  }
  .mainWind {
    width: 50%;
  }

  @media screen and (max-width: 850px) {
    .msguru-masai-carousel-main {
      /* display: grid; */
      /* grid-template-columns: repeat(1, 1fr); */
      /* flex: 1; */
      flex-wrap: wrap;

      width: 100%;
    }
    .mainWind {
      width: 100%;
    }
    .msguru-creating-impact-masai {
      font-size: 1.5rem;
    }

    .msguru-creating-impact-masai > h2 > span > img {
      /* position: absolute;
    bottom: 0;
    left: 0;
    width: 230px; */
    }
  }

  @media screen and (max-width: 500px) {
    .msguru-creating-impact-masai > h2 {
      font-size: 1.4rem;
    }
    .msguru-creating-impact-masai > h2 > span > img {
      width: 170px;
    }
  }
  @media screen and (max-width: 360px) {
    .msguru-creating-impact-masai > h2 > span > img {
      display: none;
    }

  }
</style>
