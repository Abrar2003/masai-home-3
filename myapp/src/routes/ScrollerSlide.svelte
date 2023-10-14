<script>
    import { onMount } from "svelte";

    let data = [
        {
            heading: "100% Live Distance Learning",
            description: "India’s Only Live Tech-Learning Course With Tier 1 Instructors. Get Real-Time Feedback, Interactive Sessions & A Personalised Learning Experience.",
            image: "https://www.masaischool.com/images/new-homepage/curriculum-style/course-image1.webp"
        },
        {
            heading: "Generative AI Integrated Program",
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
    .container {
        display: flex;
        width: 100%;
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
        /* border-bottom: 1px solid #ccc; */
    }

    .image-box {
        height: 350px;
        width: 60%;
        margin-top: 20px;
        border: 1px solid #ccc;
        border-radius: 8px 8px 50px 8px;
    }
    .scroll-p{
        font-weight: bold;
        text-align: start;
    }
    p{
        text-align: start;
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
    @media (max-width: 768px) {
        .container {
            flex-direction: row;
        }
        #scroll-container{
            width: 100%;
            overflow: visible;
        }

        .heading {
            height: 240px;
            width: 100%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border-radius: 8px;
            margin-bottom: 30px;
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
        margin-top: 1030px;
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
        {#each data as { heading, description }, index}
            <div class="heading">
                <h3 class="scroll-p">{heading}</h3>
                <p>{description}</p>
            </div>
        {/each}
    </div>
    <div class="image-box">
        <img src={currentImage} alt="Current Image" style="width: 100%; height: 100%; border-radius: 8px 8px 50px 8px" />
    </div>
</div>
<div class="btn-div">
    <button class="button">GET YOUR DREAM JOB</button>
</div>
