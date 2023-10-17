<script>
  import Button from "./Button/Button.svelte";
  import { onMount } from "svelte";
  let currentIndex = 0;
  const dataObjects = [
    {
      id: 1,
      name: "Ramendra Vikram Sign Parihar",
      image:
        "https://www.masaischool.com/images/new-homepage/banner-student-image3.webp",
      description:
        "Going through the 11-11-6 curriculum was a breathtaking experience. Every new unit came with great enthusiasm and a new challenge",
      companyLogo:
        "https://www.masaischool.com/images/new-homepage/company-logo3.svg",
    },
    {
      id: 2,
      name: "Hitesh Tripathi",
      image:
        "https://www.masaischool.com/images/new-homepage/banner-student-image1.webp",
      description:
        "I liked that everything is taught in a structured manner, and there is no spoon-feeding. That helps us learn by ourselves when we do.",
      companyLogo:
        "https://www.masaischool.com/images/new-homepage/company-logo1.svg",
    },
    {
      id: 3,
      name: "Pooja Kumari",
      image:
        "https://www.masaischool.com/images/new-homepage/banner-student-image2.webp",
      description:
        "I developed Communication Skills, People Skills, Mindset, active patience, JAVA, DSA, JavaScript, CSS, and HTML.",
      companyLogo:
        "https://www.masaischool.com/images/new-homepage/company-logo2.svg",
    },
  ];

  function nextSlide() {
    currentIndex = (currentIndex + 1) % dataObjects.length;
    setTimeout(nextSlide, 5000); // Change slide every 5 seconds (5000 milliseconds)
  }

  onMount(() => {
    setTimeout(nextSlide, 5000); // Start the slider after the component is mounted
  });
</script>

<div class="almuni-main-div-ms">
  <div class="almuni-main-div-ms-child">
    <div class="almuniMain-div-ms-left">
      <h2 class="alumini-ms-masai-heading">
        Realise Your Potential
        <br />
        With
        <span>
          Assured Outcomes <img
            src="https://masaischool.com/images/new-homepage/yellow-vector.svg"
            alt=""
          />
        </span>

        Delivered.
      </h2>
      <p class="ms-masai-para-geading">
        India’s only outcome-based career institute. Enter the tech workforce
        industry-ready.
      </p>
      <Button buttonData={"get your dream job"} />
    </div>
    <div class="almuniMain-div-ms-right">
      <!-- -------------------------- -->

      <div class="alu-img-box">
        <img
          class="alu-img"
          src={dataObjects[currentIndex].image}
          alt="Slide"
        />
      </div>
      <!-- ................................ -->

      <div class="alumini-desc">
        <div class="" />
        <div>
          <p>
            <img
              class="quote-start"
              src="https://www.masaischool.com/images/new-homepage/quote-start.svg"
              alt="Quote Start"
            />{dataObjects[currentIndex].description}<img
              class="quote-end"
              src="https://www.masaischool.com/images/new-homepage/quote-end.svg"
              alt="Quote End"
            />
          </p>
        </div>

        <h5>{dataObjects[currentIndex].name}</h5>
        <span />
        <img
          src={dataObjects[currentIndex].companyLogo}
          alt="Company Logo"
          style="width: 150px; margin-top: 10px;"
        />
      </div>

      <!-- -------------------------- -->
    </div>
  </div>
</div>

<style>
  .almuni-main-div-ms {
    border: 1px solid red;
    max-width: 1138px;
    margin: auto;
    margin-top: 10rem;
    margin-bottom: 12rem;
  }
  .almuni-main-div-ms-child {
    display: flex;
    align-items: center;
    justify-content: space-around;
    gap: 2rem;
    width: 95%;
    margin: auto;

    /* border: 1px solid red; */
  }
  .alumini-ms-masai-heading {
    font-weight: 700;
    text-align: left;
    font-size: 2.5rem;
  }
  .alumini-ms-masai-heading > span {
    position: relative;
    color: red;
  }
  .alumini-ms-masai-heading > span > img {
    position: absolute;
    /* top: 100; */
    left: 0;
    bottom: -10px;
    width: 22rem;
  }
  .almuniMain-div-ms-left {
    display: flex;
    justify-content: center;
    flex-direction: column;
    gap: 1.5rem;
  }
  .ms-masai-para-geading {
    font-size: 24px;
    width: 90%;
  }
  .almuniMain-div-ms-left,
  .almuniMain-div-ms-right {
    /* border: 1px solid red; */
    width: 50%;
    height: 500px;
  }

  .almuniMain-div-ms-right {
    display: flex;
    align-items: center;
    justify-content: end;
  }
  /* Right Side */

  .alu-img-box {
    width: 70%;
  }
  .alu-img-box > img {
    width: 100%;
    display: inline-block;
    background: rgb(121, 168, 250, 0.5);
    padding: 5rem 10px 0px 10px;
    box-sizing: border-box;
    border-radius: 2rem;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
  }
  .almuniMain-div-ms-right {
    position: relative;
  }

  .alumini-desc {
    background: linear-gradient(
      89.52deg,
      rgba(245, 245, 245, 0.322) 2.5%,
      rgba(255, 255, 255, 0.7) 99.54%
    );
    width: 80%;

    padding: 25px;
    position: absolute;
    left: -110px;
    bottom: 1rem;
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
    border-radius: 2rem;
  }
  /* @media screen and (max-width: 750px) {
    .almuniMain-div-ms {
      width: 100%;
      flex-direction: column;
      border: 1px solid red;
    }
  } */
  @media screen and (max-width: 780px){
    /* .alumini-ms-masai-heading{
      font-size: 1.4rem;
    }
    .ms-masai-para-geading {
      font-size: 1rem;
    }
    .alumini-ms-masai-heading > span > img {
      width: 12rem;
    }
    .alumini-desc{
      width: 90%;
    } */
    /* .almuni-main-div-ms-child {
      flex-wrap: wrap;

      width: 100%;
    } */
  }

  @media screen and (max-width: 780px) {
    .alumini-ms-masai-heading {
      font-size: 1.5rem;
    }
    .ms-masai-para-geading {
      width: 90%;
      font-weight: 600;
      margin: auto;
      text-align: center;
      padding: 0;
      font-size: 1rem;
    }
    .almuniMain-div-ms-left {
      gap: 0;
    }
    .almuni-main-div-ms-child{
      gap:0;
    }
    .alumini-ms-masai-heading > span {
    }
    .alumini-ms-masai-heading > span > img {
      /* left: 28%; */
      bottom: -7px;
      width: 13rem;
    }
    .almuni-main-div-ms-child {
      flex-wrap: wrap;

      width: 100%;
    }
    .almuniMain-div-ms-left,
    .almuniMain-div-ms-right {
      width: 100%;
      /* text-align: center; */
    }
    .almuniMain-div-ms-left,
    .alumini-ms-masai-heading {
      text-align: center;
    }
    .alumini-desc {
      background: white;
      width: 50%;
      left: 25%;
      bottom: -10rem;
      z-index: 0;
      /* margin: auto; */
    }
    .almuni-main-div-ms {
      margin-bottom: 28rem;
    }
    .almuniMain-div-ms-right {
      justify-content: center;
    }
    .almuni-main-div-ms-child {
      gap: 10rem;
    }
    .alu-img-box {
      width: 50%;
    }
    .alu-img-box > img {
      display: block;
      margin: auto;
    }
  }

  @media screen and (max-width: 425px){
    .alu-img-box {
      width: 95%;
    }
    .alu-img-box > img {
      display: block;
      margin: auto;
    }
    .alumini-desc {
      width: 95%;
      left: 2.2%;
      z-index: 0;
    }
  }
</style>
