<script>
  import { onMount } from "svelte";
  let currentIndex = 0; 
  const dataObjects = [
    {
      id: 1,
      name: "Ramendra Vikram Sign Parihar",
      image: "https://www.masaischool.com/images/new-homepage/banner-student-image3.webp",
      description: "Going through the 11-11-6 curriculum was a breathtaking experience. Every new unit came with great enthusiasm and a new challenge",
      companyLogo: "https://www.masaischool.com/images/new-homepage/company-logo3.svg",
    },
    {
      id: 2,
      name: "Hitesh Tripathi",
      image: "https://www.masaischool.com/images/new-homepage/banner-student-image1.webp",
      description: "I liked that everything is taught in a structured manner, and there is no spoon-feeding. That helps us learn by ourselves when we do.",
      companyLogo: "https://www.masaischool.com/images/new-homepage/company-logo1.svg",
    },
    {
      id: 3,
      name: "Pooja Kumari",
      image: "https://www.masaischool.com/images/new-homepage/banner-student-image2.webp",
      description: "I developed Communication Skills, People Skills, Mindset, active patience, JAVA, DSA, JavaScript, CSS, and HTML.",
      companyLogo: "https://www.masaischool.com/images/new-homepage/company-logo2.svg",
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

<style>
  @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@400;700&family=Roboto&family=Work+Sans&display=swap');
  .container {
      border: 1px solid black;
    max-width: 1280px;
    margin-top: 20px;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    align-items: center;
  }

  .flex-container {
    width: 100%;
    max-width: 1280px;
    margin-top: 20px;
    height: 1000px;
    display: flex;
    justify-content: space-between;
    /* flex-direction: column; */
    gap: 20px;
    /* align-items: center; */
    /* text-align: center; */
  }
  .quote-start
  {
    position: absolute;
    /* top: -5px; */
  }
  .quote-start{
      margin-left: -15px;
  }

  .quote-end {
      position: absolute;
  }
  .alu-box1{
      /* border: 1px solid black; */
      /* border: 10px solid red; */
      width: 100%;
      text-align: left;
      font-size: 24px;
      font-weight: 700;
  }

  .alu-img-box{
      border: 1px solid red;
      display: flex;
      width: 800px;
      height: auto;
      /* justify-content: end; */
      margin: auto;
  }
  .alu-img{
    display: flex;
    width: 100%;
    height: 500px;
      border: 1px solid red;
      background-color: rgba(121, 168, 250, 0.5);
  }

  @media (min-width: 768px) {
    .flex-container {
      flex-direction: row;
      justify-content: space-between;
      text-align: left;
    }
  }

  @media (min-width: 1024px) {
    .flex-container img {
      max-width: 350px;
    }
  }
  
  
  .alumini-desc{
      
      background: linear-gradient(89.52deg, rgba(245, 245, 245, 0.322) 2.5%, rgba(255, 255, 255, 0.7) 99.54%);
      width: 35%;
      padding: 25px;
      position: relative;
      top: -220px;
      right: -100px;
      box-shadow:0px 4px 7px 0px #BDBDBD40;
      border-radius: 8px;

      
  }
  @media (max-width: 767px) {
  /* Mobile view styles */
  .flex-container {
    flex-direction: column;
    align-items: center;
  }

  .alu-box1, .alu-img-box {
    width: 100%;
  }

  .alu-img {
    margin-top: -15px;
    /* border: 1px solid red; */
  }

  .alumini-desc {
    width: 80%;
    margin-top: 250px;
    right: 0;
  }
}

@media (min-width: 768px) and (max-width: 1023px) {
  /* Tablet view styles */
  .flex-container {
    flex-direction: column;
    align-items: center;
  }

  .alu-box1 {
    width: 100%;
  }

  .alu-img-box {
    width: 80%;
  }

  .alu-img {
    margin-top: -15px;
  }

  .alumini-desc {
    width: 80%;
    margin-top: -50px;
    right: 0;
  }
}

.dreamjob-btn {
  background-color: #ed0331;
  border-radius: 8px;
  border: none;
  padding: 10px 20px; /* Adjusted padding for better spacing */
  /* width: 350px; */
  font-size: 18px;
  font-weight: 600;
  color: white;
  letter-spacing: 1.25px;
}

.alumini-ms-masai-heading {
  font-weight:bold;
   font-size:48px;
   color: black;
   line-height: 62px;
   text-align: left;
   font-family: Poppins;
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
    width:22rem

  
  }
  .ms-masai-para-geading {
    font-size: 24px;
    font-weight: 400;
  }

@media (max-width: 767px) {
  /* Mobile view styles */
  .dreamjob-btn {
    width: 100%; /* Make the button full width on mobile */
    margin-top: 10px; /* Add margin for better spacing */
    display: flex;
    justify-content: center;
  }
  .hh1{
  font-weight:bold;
   font-size:24px;
   text-align: center;
  }
  .hh2{
    font-size: 24px;
    margin-left: 50px;
    margin-top: -10px;
  }
  .hh3{
    font-weight:bold;
   font-size:24px;
   text-align: center;
   margin-top: -55px;

  }
  .hh1with{
    display: none;
  }
  .h11with{
    display: contents;
  }
  .h1img{
    margin-top: -55px;
     width: -20%;
      margin-left:0%;
      padding: 50px;

  }
  p{
    text-align: center;
  }
  .dreamjob-btn{
    width: 70%;
    margin-left: 15%;
    margin-bottom: 60px;
  }
  .alu-img-box{
    margin-left: -40px;
  }
  
}

@media (min-width: 768px) and (max-width: 1023px) {
  /* Tablet view styles */
  .dreamjob-btn {
    width: 100%; /* Make the button full width on tablet */
    margin-top: 10px; /* Add margin for better spacing */
  }
  .hh1{
    font-size: 10px;
  }

}


</style>

<div class="container">
  <div class="flex-container">
    <div class="alu-box1">
      
      <!-- Added code snippet here -->
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
          India’s only outcome-based career institute.<br/> Enter the tech workforce
          industry-ready.
        </p>
      <button class="dreamjob-btn">GET YOUR DREAM JOB</button>
      
    </div>
    <div class="alu-img-box">
      <img class="alu-img" src={dataObjects[currentIndex].image} alt="Slide" />
    </div>
    <div class="rotated"></div>
    
    
    
    
  </div>
  <div class="alumini-desc" style="position: relative;"   >
      <div class="">
        
      </div>
      <div>
          <p><img class="quote-start" src="https://www.masaischool.com/images/new-homepage/quote-start.svg" alt="Quote Start" />{dataObjects[currentIndex].description}<img class="quote-end" src="https://www.masaischool.com/images/new-homepage/quote-end.svg" alt="Quote End" /></p>
        </div>
      
      <h5>{dataObjects[currentIndex].name}</h5><span></span>
          <img src={dataObjects[currentIndex].companyLogo} alt="Company Logo" style="width: 150px; margin-top: 10px;" />
      
    </div>
</div>






