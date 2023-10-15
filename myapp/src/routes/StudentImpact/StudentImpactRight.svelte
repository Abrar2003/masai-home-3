
<script>
  let scrollData = [
    {
      id: 1,
      text: "Masai does a great job of attracting ambitious folk and it shows in the hunger with which the grads chase their own improvement and career advancement. The curriculum is shaped such that its graduates come into the job with with an understanding of workplace and technology practices that is simply missing from freshers hired from colleges. They continuously look for feedback for their curriculum and ensure that it is up to date with the pulse of the ecosystem. All of these have translated into a very smooth hiring experience for us with Masai. Our experience with Masai so far has led me to believe that its graduates would be good fits in startup culture.",
      profileImage:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/Arya_Adarsha_Gautam_a72b51d7b3.jpeg",
      name: "Arya Adarsha Gautam",
      designation: "CTO and Co-Founder - Pagarbook",
      companyImage:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/pagarbook_rect_adcdc345e4.svg",
      linkedin: "https://www.linkedin.com/in/aryaag/",
    },
    {
      id: 2,
      text: "There are many platforms that bolster an individual's 'knowledge' to show up to work and just do their tasks. But with Masai, it is quite evident that the individuals are given a well-rounded education into the different aspects besides programming that go into software engineering. The college curriculum while focusing on the theoretical aspects of programming hasn't really evolved to keep pace with the practical aspects of software engineering. Companies too can benefit significantly by sourcing developers from Masai as they have good familiarity with the tools and processes that go into building software solutions. The dominant trait amongst Masai graduates has mostly been to focus on gaining more knowledge.",
      profileImage:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/Anirban_Majumdar_e001629fcc.jpeg",
      name: "Anirban Majumdar",
      designation: "CTO and Co-Founder - Urban Piper",
      companyImage:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/urbanpiper_rect_37c839e35e.svg",
      linkedin: "https://www.linkedin.com/in/anirvan--majumdar/",
    },
    {
      id: 3,
      text: "We were looking to hire entry-level developers and Masai more than delivered. Our selection rate from Masai's candidates is higher than other avenues of hiring and the process was completed in two days flat. The offer to joining ratio with Masai candidates was 100% which is awesome! The developers had a good foundation of the technologies they need to work with and could hit the ground running. We wholeheartedly recommend Masai to companies looking to hire entry-level developers quickly.",
      profileImage:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/Vamsee_Mohan_Kamabathula_e196f3ab55.jpeg",
      name: "Vamsee Mohan Kamabathula",
      designation: "CTO and Co-Founder - Qapita Fintech",
      companyImage:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/Qapita_13fe2db4fb.png",
      linkedin: "https://www.linkedin.com/in/vamsee-mohan-kamabathula/",
    },
    {
      id: 4,
      text: "Hiring experience with Masai is a wow. All the candidates we interviewed were equally talented, selection wasn't easy. Masai training has made college and background irrelevant because once any student goes through the training the outcome is always good. We have also found that the students are trained even on soft skills, this covers the 360 degree needs of today's corporates or startups. In addition, Masai's one offer per candidate policy ensures students join once the offer is rolled out. Overall, we are confident that Masai is the new destination for quality and timely hiring.",
      profileImage:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/Pradeep_Sreeram_494522711e.jpeg",
      name: "Pradeep Sreeram",
      designation: "Engineering Lead - Eat.Fit",
      companyImage:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/eatfit_rect_02ec413e66.svg",
      linkedin: "https://www.linkedin.com/in/pradeep-sreeram/",
    },
    {
      id: 5,
      text: "We would like to extend our heartfelt appreciation to Masai for the exceptional talent we have had the privilege of working with. The hires from Masai have consistently showcased their strong work ethic and professionalism. Their technical expertise and commitment to excellence have been invaluable to our projects. They have seamlessly integrated into our teams, collaborating with colleagues and bringing fresh perspectives to the table. Notably, these individuals have demonstrated a remarkable ability to identify and implement innovative solutions using the latest technologies. Their contribution to enhancing efficiency and streamlining processes has been remarkable. The dedication and passion they exhibit in their work are truly commendable. Overall, our experience with the Masai hires has been exceptionally positive. Their enthusiasm, technical competence, and willingness to go the extra mile have exceeded our expectations. We wholeheartedly recommend Masai as a reliable partner for organizations seeking top-tier talent. Thank you once again for the opportunity to work with such talented individuals. We look forward to continuing our partnership with Masai in the future.",
      profileImage:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/Arshdeep_Singh_0d44120445.jpeg",
      name: "Arshdeep Singh",
      designation: "Director of technology - Kapiva",
      companyImage:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/svgviewer_png_output_38_4421638b42.png",
      linkedin: "https://www.linkedin.com/in/arshdeep-singh-makker",
    },
  ];

  let currentIndex = 0;

  function next() {
    if (currentIndex < scrollData.length - 1) {
      currentIndex += 1;
    }
  }

  function previous() {
    if (currentIndex > 0) {
      currentIndex -= 1;
    }
  }
</script>

<ul class="masai-guru-right-slide-main-ul">
  {#each scrollData as img (img.id)}
    <li class="masai-guru-right-slide-main-li">
      <div class="msguru-masai-manager-linkedin-main-comp">
        <div class="msguru-masai-manager-linkedin">
          <a href={img.linkedin} target="_blank">
            <p><i class="bx bxl-linkedin-square" /></p>
          </a>
        </div>
        <div>
          <p class="para">
            {img.text}
          </p>
        </div>
        <div class="bottom-image-middle">
          <div class="msguru-masai-profile-image">
            <img src={img.profileImage} alt={img.name} />
          </div>
          <div class="msguru-name-designation-masai">
            <h6>{img.name}</h6>
            <p>{img.designation}</p>
          </div>
        </div>
        <div class="msguru-masai-company-image-bottom">
          <img src={img.companyImage} alt="" />
        </div>
      </div>
    </li>
  {/each}
</ul>
<div class="navigation-buttons">
  <button class="msguru-masai-button" on:click={previous} disabled={currentIndex === 0}
    ><i class="bx bx-chevron-left button-left-right-masai-msguru" /></button
  >
  <button class="msguru-masai-button" on:click={next} disabled={currentIndex === scrollData.length - 1}>
    <i class="bx bx-chevron-right button-left-right-masai-msguru" /></button
  >
</div>

<style>
  .msguru-masai-button{
    border: 1px solid red;
    background-color: rgb(255, 255, 255);
    border-radius: 7px;
    color: rgb(255, 0, 0);



  }
  .msguru-masai-button:hover{
    background: rgb(255, 0, 0);
    color: rgb(255, 255, 255);
    transition: ease all .5s;
  }
.button-left-right-masai-msguru{
  font-size: 2rem;
}




  .masai-guru-right-slide-main-ul {
    display: flex;
    overflow-x: auto;
    gap: 10px; /* Adjust the gap value as needed */
    scroll-snap-type: x mandatory;
    scroll-snap-align: start;
  }
  .masai-guru-right-slide-main-li {
    flex-shrink: 0;
  }
  .masai-guru-right-slide-main-ul::-webkit-scrollbar {
    width: 0; /* Hide the scrollbar */
  }
  .navigation-buttons {
    display: flex;
    justify-content: flex-end;
    margin: 16px 0;
    gap: 10px;
  }
  /* -------------------------------- */
  .msguru-masai-manager-linkedin-main-comp {
    display: flex;
    flex-direction: column;
    padding: 15px;
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    border-radius: 15px;
  }

  .msguru-masai-manager-linkedin {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    margin-right: 20px;
  }
  .msguru-masai-manager-linkedin > a {
    text-decoration: none;
  }
  /* .msguru-masai-profile-image{
    display: flex;
    align-items: center;
    justify-content: flex-end;
  } */
  ul li {
    list-style-type: none;
  }

  .bxl-linkedin-square {
    display: block;
    color: rgb(23, 129, 251);
    font-size: 1.7rem;
  }
  .para {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;

    width: 400px;
    word-wrap: normal;
  }
  .bottom-image-middle {
    display: flex;
    align-items: center;
    gap: 25px;
  }

  .msguru-masai-profile-image > img {
    width: 70px;
    border-radius: 15px;
  }

  .msguru-name-designation-masai {
  }

  .bottom-image-middle {
    display: flex;
    align-items: center;
  }
  .msguru-masai-company-image-bottom {
    /* border: 1px solid red; */
    /* display: flex;
    align-items: center;
    justify-content: flex-start; */
    /* padding: 10px 0px; */
  }
  .msguru-masai-company-image-bottom > img {
    width: 100px;
    /* display: block; */
  }

  @media screen and (max-width: 850px) {
    .masai-guru-right-slide-main-li {
      scroll-snap-align: center;
    }
  }
</style>
