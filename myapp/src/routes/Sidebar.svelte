<script>
    import { onMount } from "svelte";
  
    let isDragging = false;
    let dragStartX = 0;
    let dragStartY = 0;
    let scrollLeft = 0;
    let scrollTop = 0;
    let status = 1;

    const imageUrls = {
    1: 'https://i.ibb.co/Y3JQZnM/first.png',
    2: 'https://i.ibb.co/DtWkgF4/second.png',
    3: 'https://i.ibb.co/xF62KSy/third.png',
    4: 'https://i.ibb.co/nzg6wwD/fourth.png',
    5: 'https://www.masaischool.com/images/new-homepage/outcome/holistic-outcome.png'
  };

  let autoChangeTimeout;

  let autoClickTimeout;
  let isHovered = false;

  // Function to handle automatic button click
  const startAutoClick = () => {
    autoClickTimeout = setInterval(() => {
      if (isHovered) {
        const nextStatus = (status % 5) + 1;
        handleStatus(nextStatus);
      }
    }, 5000);
  };

  // Start automatic click when the component is mounted
  onMount(startAutoClick);

  // Function to stop automatic button click
  const stopAutoClick = () => {
    clearInterval(autoClickTimeout);
  };

  // Function to handle automatic image and button change
  const startAutoChange = () => {
    autoChangeTimeout = setInterval(() => {
      const randomStatus = Math.floor(Math.random() * 5) + 1;
      status = randomStatus;
    }, 5000);
  };

  // Start automatic change when the component is mounted
  onMount(() => {
    startAutoChange();
  });

  // Function to stop automatic image and button change
  const stopAutoChange = () => {
    clearInterval(autoChangeTimeout);
  };
  
    const handleDragStart = (e) => {
      isDragging = true;
      dragStartX = e.clientX;
      dragStartY = e.clientY;
    };
  
    const handleDrag = (e) => {
      if (isDragging) {
        const deltaX = dragStartX - e.clientX;
        const deltaY = dragStartY - e.clientY;
        dragStartX = e.clientX;
        dragStartY = e.clientY;
  
        scrollLeft += deltaX;
        scrollTop += deltaY;
  
        const element = document.getElementById("draggable-container");
        if (element) {
          element.scrollLeft = scrollLeft;
          element.scrollTop = scrollTop;
        }
      }
    };
  
    const handleDragEnd = () => {
      isDragging = false;
    };
  
    const handleStatus = (newStatus) => {
      status = newStatus;
    };
  
    onMount(() => {
      // Initialize your logic here if needed
    });
  </script>
  
  <style>

.ms-masai-sidebar{
  /* border: 1px solid red; */
  max-width: 1280px;
  margin: auto;
}

    /* Add your CSS styles here */
    .container {
      /* border: 1px solid black; */
      max-width: 1280px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    gap: 10px;
  }
  
  #draggable-container {
    display: flex;
    flex-direction: column; /* Set to column layout */
    align-items: flex-start; /* Align items to the start */
    padding: 20px;
    background-color: #ffffff;
    border-radius: 10px;
    overflow-y: auto;
    max-height: 180vh;
    width: 30%;
  }

    .button {
      background-color: #ffffff;
      color: #333333;
      border: 1px solid #cccccc;
      border-radius: 15px;
      padding: 20px 40px;
      margin-bottom: 10px;
      cursor: pointer;
      transition: all 0.3s ease;
      
    }
    .button-list {
    list-style: none;
    padding: 0;
  }

  .dashed-vertical-line {
  border-left: 3px dashed #000;
  width: 20px; /* 1px width and black color, you can adjust as needed */
  height: 30px; /* Specify the height of your dashed line */
  margin-left: 60px; /* Adjust the left margin as needed */
}

  .button-list-item {
    margin-bottom: 10px;
  }
  
    .button.selected {
      background-color: #ffffff;;
      color: #ed0331;
      border-color: #ed0331;
      border-radius: 15px;
    }
  
    .content {
      margin-top: 20px;
    }
    .img{
        width: 100%;
        height: 560px;
        border-radius: 8px;
    }
    .button-list{
    margin: auto;
    margin-top: 10px;
  }
    .box-no{
      border: 1px solid black;
      padding: 5px 15px 5px 15px;
      border-radius: 8px;
    }
  
    @media (min-width: 768px) {
      .draggable-container {
        flex-direction: row;
        width: 70%;
        max-height: 70vh;
        overflow-y: auto;
      }
  
      .button {
        width: 100%;
        margin-bottom: 0;
        font-size: 18px;
        font-weight: 700;
        padding: auto 50px auto 50px;
      }
  
      .content {
        margin-top: 0;
        /* margin-left: 20px; */
        width: 80%;
        /* border: 1px solid red; */
      }
    }

   
  
    @media (min-width: 1024px) {
      .draggable-container {
        width: 50%;
        max-height: 60vh;
      }
    }
    .headline{
        font-weight: bold;
        font-size: 40px;
        text-align: center;
        margin-bottom: 70px;
        margin-top: -140px;
    }
    @media (max-width: 767px) {
      .headline{
        font-size: 24px;
        /* border: 1px solid black; */
        padding: 0px 60px 0px 60px;
      }
    }

    @media (max-width: 750px){
    .container{
      display: flex;
      flex-direction: column;
    }
    #draggable-container {
    display: flex;
    flex-direction: column; /* Set to column layout */
    align-items: flex-start; /* Align items to the start */
    padding: 20px;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 0 0px rgba(0, 0, 0, 0);
    overflow-y: auto;
    max-height: 40vh;
    width: 90%;
    margin-bottom: -50px;
    margin-top: -50px;
  }
  .button-list{
    display: flex;
    gap: 20px;
  }
  .button{
    height: 60px;
    width: 240px;
    text-align: center;
  }
  .dashed-vertical-line{
    display: none;
  }
  .box-no{
    display: none;
  }
   } 
    
  </style>
 

 <div class="ms-masai-sidebar">

   
  <h1 class="headline" >Driven By <span style="color: #ed0331;">Outcomes</span> To Launch Your Career In Tech</h1>
  <div class="container">
  <div
    id="draggable-container"
    on:mousedown={handleDragStart}
    on:mousemove={handleDrag}
    on:mouseup={handleDragEnd}
    on:mouseleave={handleDragEnd}
    role="presentation"
    class="draggable-container"
    on:mouseenter={() => { isHovered = true; startAutoClick(); }}
    on:mouseleave={() => { isHovered = false; stopAutoClick(); }}
  >
    <ul class="button-list">
      {#each [1, 2, 3, 4, 5] as num}
        <li class="button-list-item">
          <div
            class="button"
            class:selected={status === num}
            role="button"
            tabindex="0"
            on:click={() => handleStatus(num)}
            on:keydown={e => {
              if (e.key === "Enter") {
                handleStatus(num);
                isHovered = true;
                startAutoClick();
              }
            }}
            on:focus={() => { isHovered = true; startAutoClick(); }}
          >
            {#if num === 1}
             <span class="box-no">1</span> Career Launchpad
            {:else if num === 2}
            <span class="box-no">2</span> Nurture Ambition
            {:else if num === 3}
            <span class="box-no">3</span> Practice Based
            {:else if num === 4}
            <span class="box-no">4</span> Industry Readiness
            {:else if num === 5}
            <span class="box-no">5</span>HolisticDevelopment
            {/if}
          </div>
          <div class="dashed-vertical-line"></div>
        </li>
      {/each}
    </ul>
  </div>
  <div class="content">
    {#if status in imageUrls}
      <img class="img" src={imageUrls[status]} alt={`Image for status ${status}`} />
    {/if}
  </div>
</div>

 </div>