<script>
  import StudentImpactLeft from "./StudentImpactLeft.svelte";
  import StudentImpactRight from "./StudentImpactRight.svelte";
</script>

<div class="msguru-masai-carousel-main">
  <div class="mainWind"><StudentImpactLeft /></div>
  <div class="mainWind"><StudentImpactRight /></div>
</div>

<!-- <LefrSideSlider />
<RightSideSlider /> -->

<style>
  .msguru-masai-carousel-main {
    display: flex;
    align-items: center;
    justify-content: space-around;
    gap: 2rem;
    width: 90%;
    margin: auto;
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
  }
</style>
