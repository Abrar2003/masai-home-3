<script>
    import { onMount } from "svelte";

    let data = [
        {
            heading: "100% Live Distance Learning",
            description: "India’s Only Live Tech-Learning Course With Tier 1 Instructors. Get Real-Time Feedback, Interactive Sessions & A Personalised Learning Experience.",
            image: "https://www.masaischool.com/images/new-homepage/curriculum-style/course-image1.webp"
        },
        {
            heading: `${`Generative AI Integrated Program`}`,
            description: "Harness & Implement The Power Of AI In Coding & Data Analytics. What’s More? Use Custom AI Tools To Enhance Placement Preparation.",
            image: "https://www.masaischool.com/images/new-homepage/curriculum-style/course-image2.webp"
        },
        {
            heading: "Industry Ready Curriculum",
            description: "Our Curriculum Is Regularly Updated Through Industry Feedback. In-Demand Specialisations Are Added To Aid Our Students Launch Sustainable Careers.",
            image: "https://www.masaischool.com/images/new-homepage/curriculum-style/course-image3.webp"
        },
        {
            heading: "Focus On Learning Agility",
            description: "We Prioritise Flexible Thinking & Continuous Skill Development. Stay Nimble In An Ever-Changing World By Embracing Adaptability, Curiosity & Rapid Learning.",
            image: "https://www.masaischool.com/images/new-homepage/curriculum-style/course-image4.webp"
        },
        {
            heading: "Industry Ready In Just 25-30 Weeks",
            description: "Curriculum At Masai Is Designed To Be Intensive & Extensive. With Our Unique Pedagogy Learn Right In Less Time. All We Ask Is Your Dedication!",
            image: "https://www.masaischool.com/images/new-homepage/curriculum-style/course-image5.webp"
        }
    ];

    

    let currentHeadingIndex = 0;
    let currentImage = data[currentHeadingIndex].image;

    onMount(() => {
        const container = document.getElementById("scroll-container");
        container.addEventListener("scroll", handleScroll);
    });

    function handleScroll(event) {
        const container = event.target;
        const scrollTop = container.scrollTop;
        const headingHeight = container.scrollHeight / data.length;

        const newHeadingIndex = Math.floor(scrollTop / headingHeight);
        if (newHeadingIndex !== currentHeadingIndex) {
            currentHeadingIndex = newHeadingIndex;
            updateImage();
        }
    }

    function updateImage() {
        currentImage = data[currentHeadingIndex].image;
    }
</script>

<style>
   @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@400;700&family=Roboto&family=Work+Sans&display=swap'); 
    .container {
        /* border: 1px solid black; */
        display: flex;
        justify-content: space-between;
        max-width: 1280px;
        gap: 30px;
        margin-bottom: 100px;
    }

    #scroll-container {
        width: 40%;
        height: 300px;
        overflow-y: scroll;
        /* border: 1px solid #ccc; */
    }
    #scroll-container::-webkit-scrollbar {
        width: 0.4rem;
        /* background-color: red; */
    }
    .headline{
        margin-top: 40px;
        font-size: 37px;
        text-align: center;
        font-weight: bold;
    }

    .heading {
        height: 300px;
        text-align: center;
        padding: 20px;
        margin-top: 100px;
        /* border: 19px solid black; */
    }

    .image-box {
        height: 395px;
        width: 45%;
        margin-top: 20px;
        border: 1px solid #ccc;
        border-radius: 24px;
    }
    .scroll-p{
        color: black;
        text-align: start;

    }
    .scroll-icon{
        display: none;
    }
    p{
        text-align: start;
        font-size: 16px;
        font-family: Open Sans, sans-serif;
        font-weight: 400;
        margin: 24px 24px 24px 0px;
        padding: 0px 50px 0px 0px;
    /* border: 1px solid red; */
    }
    .scroll-head-imgbox{
        display: none;
    }
    .redhead{
        color: #ed0331;
    }
    .btn-div{
        display: flex;
        justify-content: center;
        margin-top: -100px;
    }
    .button {
    background-color: #ed0331;
    color: white;
    padding: 10px 25px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    margin-top: 10px;
    font-size: 19px;
    font-weight: 600;
    
}
.scroll-p{
    font-size: 24px;
    font-weight: 700;
    font-family: poppins;
    
}
    @media (max-width: 768px) {
        .container {
            flex-direction: row;
        }
        #scroll-container{
            /* border: 1px solid blue; */
            /* margin-bottom: 600px; */
            height: auto;
            width: 100%;
            overflow: visible;
            text-align: center;
        }

        .heading {
            /* border: 1px solid red; */
            height: 270px;
            /* width: 10%; */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border-radius: 8px;
            margin-bottom: 30px;
            text-align: center !important;
            text-decoration: none;
        }

        .image-box {
            width: 10%;
            display: none;
        }
        .scroll-head{
            background-color: #6e71cc;
            color: white;
            padding: 30px 0px 30px 0px;
            margin: 20px;
            border-radius: 20px;
        }
        .scroll-head-imgbox{
            display: flex;
            background-color: white;
            width: 100px;
            height: 100px;
            border-radius: 50%;
            margin: auto;
        }
        .scroll-head-img{
            margin: auto;
            margin-left: 10px;
            margin-top: 10px;
        }
        .redhead{
            color: white;
        }
        .btn-div{
        display: flex;
        justify-content: center;
        /* margin-top: 1030px; */
    }
    }
</style>
<div class="scroll-head">
    <div class="scroll-head-imgbox">
    <img class="scroll-head-img" src="https://www.masaischool.com/images/new-homepage/curriculum-style/graduate.svg"/>
</div>
<h3 class="headline" >Best-In-Class <span class="redhead">Curriculum </span><span class="redhead">& </span><span class="redhead">Pedagogy</span></h3>
</div>
<div class="container">
    <div id="scroll-container">
        
            <div class="heading" style="text-align: center;">
                <img class="scroll-icon" src="/"/>
                <h3 class="scroll-p"><span style="color:rgb(237, 3, 49)">100% </span>Live Distance Learning</h3>
                <p>India’s Only Live Tech-Learning Course With Tier 1 Instructors. Get Real-Time Feedback, Interactive Sessions & A Personalised Learning Experience.</p>
            </div>
            <div class="heading">
                <img class="scroll-icon" src="/"/>
                <h3 class="scroll-p">Generative <span style="color:rgb(237, 3, 49)"> AI Integrated</span>  Program</h3>
                <p>Harness & Implement The Power Of AI In Coding & Data Analytics. What’s More? Use Custom AI Tools To Enhance Placement Preparation.</p>
            </div>
            <div class="heading">
                <img class="scroll-icon" src="/"/>
                <h3 class="scroll-p"><span style="color:rgb(237, 3, 49)">Industry Ready </span>Curriculum</h3>
                <p>Our Curriculum Is Regularly Updated Through Industry Feedback. In-Demand Specialisations Are Added To Aid Our Students Launch Sustainable Careers.</p>
            </div>
            <div class="heading">
                <img class="scroll-icon" src="/"/>
                <h3 class="scroll-p">Focus On Learning <span style="color:rgb(237, 3, 49)"> Agility </span> </h3>
                <p>We Prioritise Flexible Thinking & Continuous Skill Development. Stay Nimble In An Ever-Changing World By Embracing Adaptability, Curiosity & Rapid Learning.</p>
            </div>
            <div class="heading">
                <img class="scroll-icon" src="/"/>
                <h3 class="scroll-p">Industry Ready In Just <span style="color:rgb(237, 3, 49)"><br/>25-30 Weeks</span></h3>
                <p>Curriculum At Masai Is Designed To Be Intensive & Extensive. With Our Unique Pedagogy Learn Right In Less Time. All We Ask Is Your Dedication!</p>
            </div>
    </div>
    <div class="image-box">
        <img src={currentImage} alt="Current Image" style="width: 100%; height: 395px; border-radius: 24px" />
    </div>
</div>
<div class="btn-div">
    <button class="button">GET YOUR DREAM JOB</button>
</div>
