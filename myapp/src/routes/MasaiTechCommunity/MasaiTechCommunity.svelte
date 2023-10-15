<script>
  import Button from "../Button/Button.svelte";

  let items = [
    {
      id: 1,
      text: "Item 1",
      image:
        "https://www.masaischool.com/images/new-homepage/community/community11.webp",
    },
    {
      id: 2,
      text: "Item 2",
      image:
        "https://www.masaischool.com/images/new-homepage/community/community10.webp",
    },
    {
      id: 3,
      text: "Item 3",
      image:
        "https://www.masaischool.com/images/new-homepage/community/community1.webp",
    },
    {
      id: 4,
      text: "Item 4",
      image:
        "https://www.masaischool.com/images/new-homepage/community/community1.webp",
    },
    {
      id: 5,
      text: "Item 5",
      image:
        "https://www.masaischool.com/images/new-homepage/community/community1.webp",
    },
  ];
  let currentIndex = 0;

  function next() {
    if (currentIndex < items.length - 1) {
      currentIndex += 1;
    }
  }

  function previous() {
    if (currentIndex > 0) {
      currentIndex -= 1;
    }
  }
</script>

<!-- Heading -->
<div class="headding-tech-community-msguru-masai">
  <h2 class="">
    Be A Part Of Our Thriving
    <br />
    <span class="tech-community-higilite-text">
      Tech Community <img
        src="https://masaischool.com/images/new-homepage/yellow-vector.svg"
        alt="Yellow Line"
      />
    </span>
  </h2>
</div>
<!-- Heading -->
<div>
  <ul class="masai-guru-right-slide-main-ul">
    {#each items as img (img.id)}
      <li class="masai-guru-right-slide-main-li">
        <img class="imageScroll-scrll" src={img.image} alt={img.text} />
      </li>
    {/each}
  </ul>
  <div class="button-flex-msguru-masai">
   
    <div class="navigation-buttons">
      <!-- Add debug messages to your code -->
      <button
        class="msguru-masai-button"
        on:click={previous}
        disabled={currentIndex === 0}
        ><i class="bx bx-chevron-left button-left-right-masai-msguru" /></button
      >
      <button
        class="msguru-masai-button"
        on:click={next}
        disabled={currentIndex === items.length - 1}
        ><i
          class="bx bx-chevron-right button-left-right-masai-msguru"
        /></button
      >
    </div>
    <div class="community-button-msguru-masai">
      <Button buttonData={"Join Our Community"} />
    </div>
  </div>
</div>

<style>
  /* Heading */

  .headding-tech-community-msguru-masai {
    text-align: center;
    padding: 2rem 0rem;
  }
  .headding-tech-community-msguru-masai > h2 {
    font-size: 2rem;
    font-weight: 700;
  }
  .tech-community-higilite-text {
    color: red;
    position: relative;
    gap: 10px;
  }
  .tech-community-higilite-text > img {
    position: absolute;
    right: 0;
    bottom: 0;
    width: 250px;
  }

  /* Heading */

  .community-button-msguru-masai {
    /* display: inline-block; */
    /* margin: auto; */
    text-align: center;
  }

  .navigation-buttons {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    margin: 16px 10px;
    gap: 10px;
  }
  .button-flex-msguru-masai {
  }

  .masai-guru-right-slide-main-ul {
    display: flex;
    overflow-x: auto;
    gap: 10px;
    scroll-snap-type: x mandatory;
    scroll-snap-align: start;
    /* width: 100%; */
  }
  .masai-guru-right-slide-main-li {
    flex-shrink: 0;
    /* width: 200px; */
  }
  .masai-guru-right-slide-main-ul::-webkit-scrollbar {
    width: 0;
  }
  .navigation-buttons {
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
  ul li {
    list-style-type: none;
  }
  .imageScroll-scrll {
    width: 350px;
    height: 250px;
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
  .bottom-image-middle {
    display: flex;
    align-items: center;
  }

  .msguru-masai-company-image-bottom > img {
    width: 100px;
  }
  .button-left-right-masai-msguru {
    font-size: 2rem;
  }
  .msguru-masai-button {
    border: 1px solid red;
    background-color: rgb(255, 255, 255);
    border-radius: 7px;
    color: rgb(255, 0, 0);
  }
  .msguru-masai-button:hover {
    background: rgb(255, 0, 0);
    color: rgb(255, 255, 255);
    transition: ease all 0.5s;
  }

  @media screen and (max-width: 300px) {
    .headding-tech-community-msguru-masai > h2 {
      font-size: 1.5rem;
    }
    .tech-community-higilite-text > img {
      width: 190px;
    }
  }
</style>
