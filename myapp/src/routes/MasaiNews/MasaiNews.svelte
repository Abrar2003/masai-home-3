<script>
  import { onMount } from "svelte";

  let slides = [
    {
      id: 1,
      src: "https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Article_Prateek_Shukla_Gen_AI_92324e2d6b.jpeg",
      text: "Empowering Education Through GenAI",
    },
    {
      id: 2,
      src: "https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Thungy_1_420b226e5b.webp",
      text: "Masai School targets fivefold revenue growth in three years",
    },
    {
      id: 3,
      src: "https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Thingy_2_f2c52e6fcf.webp",
      text: "Beyond Degrees: Embracing Alternative Credentialing and Micro-learning in Tech Recruitment",
    },
  ];

  let isMobile = false;
  let currentIndex = 0;

  // const onMount = () => {};
  onMount(() => {
    function updateView() {
      isMobile = window.innerWidth <= 768;
    }

    window.addEventListener("resize", updateView);
    updateView();
  });

  function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
  }

  function prevSlide() {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
  }

  // Check if it's the last slide
  let isLastSlide = currentIndex === slides.length - 1;
</script>

<div class="msguru-center-text">
  {#if isMobile}
    <h3>
      Masai in <span class="msgur-news"
        >News
        <img
          style="width: 100px; font-weight:900;"
          src="https://masaischool.com/images/new-homepage/yellow-vector.svg"
          alt="Under Line"
        />
      </span>
    </h3>
  {:else}
    <h2>
      Masai in <span class="msgur-news"
        >News
        <img
          style="width: 130px;"
          src="https://masaischool.com/images/new-homepage/yellow-vector.svg"
          alt="Under Line"
        />
      </span>
    </h2>
  {/if}
</div>

{#if isMobile}
  <!-- Mobile Swiper -->
  <div class="mobile-swiper">
    <div class="msguru-swiper-slide">
      <img src={slides[currentIndex].src} alt={slides[currentIndex].text} />
      <p>{slides[currentIndex].text}</p>
    </div>
    <div class="masai-slider-buttons-next-prev">
      <button on:click={prevSlide} class="prev" disabled={currentIndex === 0}>
        <i class="bx bx-chevron-left" />
      </button>
      <button on:click={nextSlide} disabled={isLastSlide} class="next">
        <i class="bx bx-chevron-right" />
      </button>
    </div>
  </div>
{:else}
  <!-- Desktop Image Grid -->
  <div class="msguru-desktop-grid">
    {#each slides as slide (slide.id)}
      <div class="msguru-swiper-slide">
        <img src={slide.src} alt={slide.text} />
        <p>{slide.text}</p>
      </div>
    {/each}
  </div>
{/if}

<style>
  .msguru-desktop-grid {
    margin: auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 25px;
    width: 90%;
    /* padding: 0px 0px 45px 0px; */
    margin-bottom: 30px;
  }
  .msguru-center-text {
    text-align: center;
    margin: 0 auto;
    padding: 30px;
    font-size: 34px;
    font-weight: 700;
    /* line-height: 10px; */
  }

  .msgur-news {
    color: red;
    position: relative;
  }
  .msgur-news > img {
    position: absolute;
    bottom: 0;
    right: 0;
  }

  .mobile-swiper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .msguru-swiper-slide {
    width: 100%;
    /* border: 1px solid red; */
    /* margin: auto; */
  }
  .msguru-swiper-slide img {
    width: 100%;
    height: 55%;
  }

  .msguru-swiper-slide > p {
    font-size: 1.4rem;
    font-weight: 700;
    margin-top: 2rem;
    text-align: left;
    color: rgb(45, 45, 45);
    line-height: 28px;
  }

  .masai-slider-buttons-next-prev {
    display: flex;
    align-items: center;
    justify-content: end;
    margin-right: 10px;
    gap: 0px 10px;
    /* border: 1px solid red; */
    width: 100%;
  }

  .masai-slider-buttons-next-prev button {
    padding: 1px;
    background-color: white;
    border: 1px solid red;
    border-radius: 7px;
    color: red;
    font-size: 2rem;
  }

  .masai-slider-buttons-next-prev button:hover {
    color: white;
    background-color: red;
    cursor: pointer;
  }
</style>
