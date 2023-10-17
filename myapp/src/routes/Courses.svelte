<script>
  
    let courses = [
      {
        title: "Full Stack Web Development",
        image: "https://masai-website-images.s3.ap-south-1.amazonaws.com/full_stack1_329d6b5595.png",
        duration: "30 weeks",
        opportunities: ["Opportunities: Full Stack Developer, Software Engineer & much more.", "100% live learning with expert instructors.","Pay After Placement"],
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

@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@400;700&family=Roboto&family=Work+Sans&display=swap');
.card-container {
  /* border: 1px solid black; */
  max-width: 1280px;
    display: flex;
    flex-direction: row;
    margin: auto;
    justify-content: center;
    /* padding: 20px; */
}
p{
  display: flex;
}

@media (max-width: 768px) {
    .card-container {
        flex-direction: column;
    }
}

.card {
    max-width: 408px;
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
    /* background: linear-gradient(89.52deg, rgba(17, 17, 17, 0.322) 2.5%, rgba(255, 255, 255, 0.7) 99.54%); */
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
    border-radius: 8px;
    cursor: pointer;
    margin-top: 10px;
}

.course-title-box{
  margin: auto;
  text-align: left;
  margin-left: 0%;
}

.button-box {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}
.p-opp{
  font-size: 14px;
  font-family: Open Sans;
  color: rgb(33, 25, 27);
  font-weight: 600;
}

.img-box {
    width: 408px;
    padding: 40px;
    margin-top: -20px;
    border-radius: 8px 8px 0px 0px;
    margin-left: -20px;
    height: 200px;
    background: #B7B8E5;
}
.img-box-1 {
    width: 408px;
    padding: 40px;
    margin-top: -20px;
    border-radius: 8px 8px 0px 0px;
    margin-left: -20px;
    height: 200px;
    background: rgb(229, 201, 183);
}

.course-title {
    font-size: 20px;
    font-weight: 700;
    text-align: start;
    font-family: poppins;
    padding-top: 20px;
    margin-bottom:-1px;
    
}

.course-p{
    text-align: start;
    font-size: 16px;
    font-weight: 100;
    font-family: sans-serif;
    color: #544D4F;
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
    <div class="card">
        <div class="img-box">
            <img class="image" src="https://masai-website-images.s3.ap-south-1.amazonaws.com/full_stack1_329d6b5595.png" alt="" />
        </div>
      <div class="course-title-box">
        <p class="course-title">Full Stack Web Development</p>
      <p class="course-p">Become job-ready in 30 weeks</p>
      </div>
      
      <hr />
  
      <div class="opportunities">
          <div class="opportunity">
           <p class="p-opp">
              <span><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_24121_5085)"><path d="M12 0C5.38293 0 0 5.38293 0 12C0 18.6171 5.38293 24 12 24C18.6171 24 24 18.6171 24 12C24 5.38293 18.6171 0 12 0Z" fill="#EEFFF7"></path><path d="M18.0823 9.45703L11.5822 15.9569C11.3872 16.1519 11.1312 16.2501 10.8752 16.2501C10.6193 16.2501 10.3633 16.1519 10.1683 15.9569L6.91833 12.707C6.52722 12.316 6.52722 11.684 6.91833 11.293C7.30927 10.9019 7.94116 10.9019 8.33228 11.293L10.8752 13.836L16.6683 8.04309C17.0593 7.65198 17.6912 7.65198 18.0823 8.04309C18.4732 8.43402 18.4732 9.06592 18.0823 9.45703V9.45703Z" fill="#6FCD9E"></path></g><defs><clipPath id="clip0_24121_5085"><rect width="24" height="24" fill="white"></rect></clipPath></defs></svg>
               <strong>Opportunities:</strong> Full Stack Developer, Software <br/><span style="margin-left:30px;">Engineer & much more.</span>

              </p>
          </div>
          <div class="opportunity">
            <p class="p-opp">
              <span><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_24121_5085)"><path d="M12 0C5.38293 0 0 5.38293 0 12C0 18.6171 5.38293 24 12 24C18.6171 24 24 18.6171 24 12C24 5.38293 18.6171 0 12 0Z" fill="#EEFFF7"></path><path d="M18.0823 9.45703L11.5822 15.9569C11.3872 16.1519 11.1312 16.2501 10.8752 16.2501C10.6193 16.2501 10.3633 16.1519 10.1683 15.9569L6.91833 12.707C6.52722 12.316 6.52722 11.684 6.91833 11.293C7.30927 10.9019 7.94116 10.9019 8.33228 11.293L10.8752 13.836L16.6683 8.04309C17.0593 7.65198 17.6912 7.65198 18.0823 8.04309C18.4732 8.43402 18.4732 9.06592 18.0823 9.45703V9.45703Z" fill="#6FCD9E"></path></g><defs><clipPath id="clip0_24121_5085"><rect width="24" height="24" fill="white"></rect></clipPath></defs></svg>
                100% live learning with expert instructors.

            </p>
          </div>
          <div class="opportunity">
            <p class="p-opp">
              <span><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_24121_5085)"><path d="M12 0C5.38293 0 0 5.38293 0 12C0 18.6171 5.38293 24 12 24C18.6171 24 24 18.6171 24 12C24 5.38293 18.6171 0 12 0Z" fill="#EEFFF7"></path><path d="M18.0823 9.45703L11.5822 15.9569C11.3872 16.1519 11.1312 16.2501 10.8752 16.2501C10.6193 16.2501 10.3633 16.1519 10.1683 15.9569L6.91833 12.707C6.52722 12.316 6.52722 11.684 6.91833 11.293C7.30927 10.9019 7.94116 10.9019 8.33228 11.293L10.8752 13.836L16.6683 8.04309C17.0593 7.65198 17.6912 7.65198 18.0823 8.04309C18.4732 8.43402 18.4732 9.06592 18.0823 9.45703V9.45703Z" fill="#6FCD9E"></path></g><defs><clipPath id="clip0_24121_5085"><rect width="24" height="24" fill="white"></rect></clipPath></defs></svg>
                Pay After Placement
            </p>
          </div>
      </div>
  <br>
      <button class="button">VIEW DETAILS</button>
    </div>
    <div class="card">
      <div class="img-box-1">
          <img class="image" src="https://masai-website-images.s3.ap-south-1.amazonaws.com/backend_ea129d404e.png" alt="" />
      </div>
    <div class="course-title-box">
      <p class="course-title">Backend Development</p>
    <p class="course-p">Become job-ready in 35 weeks</p>
    </div>
    
    <hr />

    <div class="opportunities">
        <div class="opportunity">
          <p class="p-opp">
            <span><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_24121_5085)"><path d="M12 0C5.38293 0 0 5.38293 0 12C0 18.6171 5.38293 24 12 24C18.6171 24 24 18.6171 24 12C24 5.38293 18.6171 0 12 0Z" fill="#EEFFF7"></path><path d="M18.0823 9.45703L11.5822 15.9569C11.3872 16.1519 11.1312 16.2501 10.8752 16.2501C10.6193 16.2501 10.3633 16.1519 10.1683 15.9569L6.91833 12.707C6.52722 12.316 6.52722 11.684 6.91833 11.293C7.30927 10.9019 7.94116 10.9019 8.33228 11.293L10.8752 13.836L16.6683 8.04309C17.0593 7.65198 17.6912 7.65198 18.0823 8.04309C18.4732 8.43402 18.4732 9.06592 18.0823 9.45703V9.45703Z" fill="#6FCD9E"></path></g><defs><clipPath id="clip0_24121_5085"><rect width="24" height="24" fill="white"></rect></clipPath></defs></svg>
              <strong>Opportunities:</strong> Backend Web Developer, API <br/><span style="margin-left:30px;">developer & much more.</span>

          </p>
        </div>
        <div class="opportunity">
          <p class="p-opp">
            <span><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_24121_5085)"><path d="M12 0C5.38293 0 0 5.38293 0 12C0 18.6171 5.38293 24 12 24C18.6171 24 24 18.6171 24 12C24 5.38293 18.6171 0 12 0Z" fill="#EEFFF7"></path><path d="M18.0823 9.45703L11.5822 15.9569C11.3872 16.1519 11.1312 16.2501 10.8752 16.2501C10.6193 16.2501 10.3633 16.1519 10.1683 15.9569L6.91833 12.707C6.52722 12.316 6.52722 11.684 6.91833 11.293C7.30927 10.9019 7.94116 10.9019 8.33228 11.293L10.8752 13.836L16.6683 8.04309C17.0593 7.65198 17.6912 7.65198 18.0823 8.04309C18.4732 8.43402 18.4732 9.06592 18.0823 9.45703V9.45703Z" fill="#6FCD9E"></path></g><defs><clipPath id="clip0_24121_5085"><rect width="24" height="24" fill="white"></rect></clipPath></defs></svg>
              100% live learning with expert instructors.

          </p>
        </div>
        <div class="opportunity">
          <p class="p-opp">
            <span><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_24121_5085)"><path d="M12 0C5.38293 0 0 5.38293 0 12C0 18.6171 5.38293 24 12 24C18.6171 24 24 18.6171 24 12C24 5.38293 18.6171 0 12 0Z" fill="#EEFFF7"></path><path d="M18.0823 9.45703L11.5822 15.9569C11.3872 16.1519 11.1312 16.2501 10.8752 16.2501C10.6193 16.2501 10.3633 16.1519 10.1683 15.9569L6.91833 12.707C6.52722 12.316 6.52722 11.684 6.91833 11.293C7.30927 10.9019 7.94116 10.9019 8.33228 11.293L10.8752 13.836L16.6683 8.04309C17.0593 7.65198 17.6912 7.65198 18.0823 8.04309C18.4732 8.43402 18.4732 9.06592 18.0823 9.45703V9.45703Z" fill="#6FCD9E"></path></g><defs><clipPath id="clip0_24121_5085"><rect width="24" height="24" fill="white"></rect></clipPath></defs></svg>
              Pay After Placement
          </p>
        </div>
    </div>
<br>
    <button class="button">VIEW DETAILS</button>
  </div>
</div>
<br>
 <div class="button-box">
    <button class="button" style="margin-top: 20px;">VIEW ALL COURSES</button>
 </div> 
  
  
  