<script>
  let activeIndex = 0;

  let carouselData = [
    {
      src: "https://cdn.pixabay.com/photo/2014/02/27/16/10/flowers-276014_1280.jpg",
      alt: "First slide",
    },
    {
      src: "https://images.pexels.com/photos/268533/pexels-photo-268533.jpeg?cs=srgb&dl=pexels-pixabay-268533.jpg&fm=jpg",
      alt: "Second slide",
    },
    {
      src: "https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8=",
      alt: "Third slide",
    },
  ];

  function prevSlide() {
    activeIndex = (activeIndex - 1 + carouselData.length) % carouselData.length;
  }

  function nextSlide() {
    activeIndex = (activeIndex + 1) % carouselData.length;
  }
</script>

<div class="msguru-masai-left-carousel">
  <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
    <div class="carousel-inner">
      {#each carouselData as item, i (item.src)}
        <div class="carousel-item {i === activeIndex ? 'active' : ''}">
          <img class="d-block w-100" src={item.src} alt={item.alt} />
        </div>
      {/each}
    </div>
    <a
      class="carousel-control-prev mainGp"
      href="#carouselExampleControls"
      role="button"
      data-slide="prev"
      on:click={prevSlide}
    >
      <i
        class="bx bx-chevron-left-circle carousel-button-msguru-masai"
        style="position: absolute; left: 0;"
      />
    </a>
    <a
      class="carousel-control-next"
      href="#carouselExampleControls"
      role:button
      data-slide="next"
      on:click={nextSlide}
    >
      <i
        class="bx bx-chevron-right-circle carousel-button-msguru-masai"
        style="position: absolute; right: 0;"
      />
    </a>
  </div>
</div>

<style>
  .d-block{
    border-radius: 10px;
  }
  .msguru-masai-left-carousel {
    /* width: 100%; */
    /* border: 1px solid red; */
  }
  .carousel-inner {
    position: relative;
    box-sizing: border-box;
    transition: transform 0.3s ease; /* Add smooth transition effect */
  }
  .carousel-button-msguru-masai {
    font-size: 2rem;
    color: black;
    background-color: rgb(255, 255, 255);
    border-radius: 50px;
  }
  .carousel-button-msguru-masai:hover {
    background-color: rgb(164, 164, 164);
  }

  /* .mainGp{
       box-sizing: border-box;
        padding: 10px; 
       
    
    } */

  @media screen and (max-width: 850px) {
    .msguru-masai-left-carousel {
      width: 90%;
      margin: auto;
    }
    /* .d-block {
      border-radius: 10px;
    } */
  }
</style>
