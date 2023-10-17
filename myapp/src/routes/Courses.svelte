<script>
  
    let courses = [
      {
        title: "Full Stack Web Development",
        image: "https://masai-website-images.s3.ap-south-1.amazonaws.com/full_stack1_329d6b5595.png",
        duration: "30 weeks",
        opportunities: ["Full Stack Developer, Software Engineer", "100% live learning with expert instructors.","Pay After Placement"],
      },
      {
        title: "Backend Development",
        image: "https://masai-website-images.s3.ap-south-1.amazonaws.com/backend_ea129d404e.png",
        duration: "35 weeks",
        opportunities: ["Opportunities: Backend Web Developer, API developer & much more.", "100% live learning with expert instructors.","Pay After Placement"],
      },
    ];
  </script>
  
  <style>


.card-container {
  border: 1px solid black;
  max-width: 1280px;
    display: flex;
    flex-direction: row;
    margin: auto;
    justify-content: center;
    padding: 20px;
}

@media (max-width: 768px) {
    .card-container {
        flex-direction: column;
    }
}

.card {
    max-width: 400px;
    /* width: 300px; */
    padding: 20px;
    margin: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.image {
    border-radius: 8px;
    width: 120px;
    height: 120px;
    object-fit: cover;
    margin-bottom: 10px;
    background: linear-gradient(89.52deg, rgba(17, 17, 17, 0.322) 2.5%, rgba(255, 255, 255, 0.7) 99.54%);
}

.opportunity {
    display: flex;
    align-items: center;
    font-weight: 600;
    font-size: 15px;
    color: black;
    text-align: start;
    padding-right: 0px;
}

.button {
    background-color: #ed0331;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 10px;
}

.button-box {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

.img-box {
    width: 400px;
    padding: 40px;
    margin-top: -20px;
    border-radius: 8px 8px 0px 0px;
    margin-left: -20px;
    height: 200px;
    background: #B7B8E5;
}

.course-title {
    font-size: 1.25rem;
    font-weight: bold;
    text-align: start;
}

p{
    text-align: start;
}

.head{
    font-size: 50px;
    font-weight: bold;
    text-align: center;
}
.headline{
 font-weight: bold;
 text-align: center;
}

@media (max-width: 768px) {
    .card {
        width: 100%;
        margin: 10px 0;
    }

    .card-container {
        padding: 10px;
    }

    .img-box {
        width: 113%;
        padding: 10px;
        height: 150px;
    }
    .head{
      font-size: 24px;
    }
    .headline{
      font-size: 20px;
    }
}
  </style>
  <br>
  <br>
  <br>
  <br>
<div>
    <h1 class="head">Our Courses</h1>
    <h3 class="headline" >Practice-Based Learning Tracks, <span style="color: #ed0331;">Supercharged By A.I.</span></h3>
</div>
<br>
  <div class="card-container">
  {#each courses as course (course.title)}
    <div class="card">
        <div class="img-box">
            <img class="image" src={course.image} alt={course.title} />
        </div>
      
      <p class="course-title">{course.title}</p>
      <p>Become job-ready in {course.duration}</p>
      <hr />
  
      <div class="opportunities">
        {#each course.opportunities as opportunity (opportunity)}
          <div class="opportunity">
            <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM369 209L241 337c-9.4 9.4-24.6 9.4-33.9 0l-64-64c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0l47 47L335 175c9.4-9.4 24.6-9.4 33.9 0s9.4 24.6 0 33.9z"/></svg>
            {opportunity}
          </div>
        {/each}
      </div>
  <br>
      <button class="button">VIEW DETAILS</button>
    </div>
  {/each}
</div>
<br>
 <div class="button-box">
    <button class="button" style="margin-top: 20px;">VIEW ALL COURSES</button>
 </div> 
  
  
  