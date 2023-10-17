<script>
  let animated = true;

  const images = [
    {
      id: 1,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/globallogic_c30eb641f7.svg",
    },
    {
      id: 2,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/swiggy_bc1b88842e.svg",
    },
    {
      id: 3,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/dream11_d6c8d97a52.svg",
    },
    {
      id: 4,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/swiggy_bc1b88842e.svg",
    },
    {
      id: 5,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/airmeet_93e45faced.svg",
    },
    {
      id: 6,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/moneytap_d5a6c9d532.svg",
    },
    {
      id: 7,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/salesken_baefe048ac.svg",
    },
    {
      id: 8,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/smallcase_1740bcc33f.svg",
    },
    {
      id: 9,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/pagarbook_2746958f65.svg",
    },
    {
      id: 10,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/simplilearn_f8af8de923.svg",
    },
    {
      id: 11,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/capgemini_31a863e94f.svg",
    },
    {
      id: 12,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/vyapar_3f3770ebb5.svg",
    },
    {
      id: 13,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/whitehat_5a86f1e308.svg",
    },
    {
      id: 14,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/bharatpe_a3a5a3f552.svg",
    },
    {
      id: 15,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/whitehat_5a86f1e308.svg",
    },
    {
      id: 16,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/paytm_a5c1ce2bc6.svg",
    },
    {
      id: 17,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/airmeet_93e45faced.svg",
    },
    {
      id: 18,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/urbanpiper_2884348a0b.svg",
    },
    {
      id: 19,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/moneytap_d5a6c9d532.svg",
    },
    {
      id: 20,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/homelane_e9cadd0c3c.svg",
    },
    {
      id: 21,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/dream11_d6c8d97a52.svg",
    },
    {
      id: 22,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/eatfit_9dc276a187.svg",
    },
    {
      id: 23,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/globallogic_c30eb641f7.svg",
    },
    {
      id: 24,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/svgviewer_png_output_38_4421638b42.png",
    },
    {
      id: 25,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/ajio_a16cd7a85b.svg",
    },
    {
      id: 26,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/byjus_e7b97a9c80.svg",
    },
    {
      id: 27,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/ibm_795b5429ee.svg",
    },
    {
      id: 28,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/ola_15b5ee2b82.svg",
    },
    {
      id: 29,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/leapfinance_0d785d05eb.svg",
    },
    {
      id: 30,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/sharechat_23a9923a34.svg",
    },
    {
      id: 31,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/bharatagri_d4794042fe.svg",
    },
    {
      id: 32,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/smallcase_1740bcc33f.svg",
    },
    {
      id: 33,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/pagarbook_2746958f65.svg",
    },
    {
      id: 34,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/simplilearn_f8af8de923.svg",
    },
    {
      id: 35,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/capgemini_31a863e94f.svg",
    },
    {
      id: 36,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/vyapar_3f3770ebb5.svg",
    },
    {
      id: 37,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/salesken_baefe048ac.svg",
    },
    {
      id: 38,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/swiggy_bc1b88842e.svg",
    },
    {
      id: 39,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/bharatpe_a3a5a3f552.svg",
    },
    {
      id: 40,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/whitehat_5a86f1e308.svg",
    },
    {
      id: 41,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/paytm_a5c1ce2bc6.svg",
    },
    {
      id: 42,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/airmeet_93e45faced.svg",
    },
    {
      id: 43,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/urbanpiper_2884348a0b.svg",
    },
    {
      id: 44,
      image:
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/moneytap_d5a6c9d532.svg",
    },
  ];
  let isMedia;
</script>

<div class="msguru-masai-brand-main">
  <div style="padding: 2rem 0rem;">
    <p class="masai-msguru-hiring-partner-banner" class:media={isMedia}>
      Meet Our <span
        >4000+ <img
          src="https://masaischool.com/images/new-homepage/yellow-vector.svg"
          alt=""
        />
      </span> Hiring Partners
    </p>

    <div
      class={"scroller " + (animated ? "animated" : "")}
      data-direction="left"
      data-speed="fast"
    >
      <div class="scroller__inner">
        {#each images as img (img.id)}
          <img class="imageScrolling" src={img.image} alt={"Item " + img.id} />
        {/each}
      </div>
    </div>
  </div>
</div>

<style>
  .msguru-masai-brand-main {
    width: 100%;
    margin: auto;
  }

  .masai-msguru-hiring-partner-banner {
    text-align: center;
    font-size: 2.3rem;
    font-weight: 700;
  }

  .masai-msguru-hiring-partner-banner > span {
    position: relative;
    color: red;
  }
  .masai-msguru-hiring-partner-banner > span > img {
    position: absolute;
    width: 115px;
    bottom: 0;
    left: 0;
  }
  .scroller {
    max-width: 100%;
    margin: auto;
  }
  .imageScrolling {
    /* border: 1px solid red; */
    width: 120px;
    height: 120px;
    border-radius: 25px;
    box-shadow: rgba(2, 12, 111, 0.24) 0px 3px 8px;
  }

  .scroller__inner {
    padding-block: 1rem;
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
  }

  .scroller.animated {
    overflow: hidden;
  }

  .scroller.animated .scroller__inner {
    width: max-content;
    flex-wrap: nowrap;
    animation: scroll var(--_animation-duration, 10s)
      var(--_animation-direction, forwards) linear infinite;
  }

  .scroller[data-direction="right"] {
    --_animation-direction: reverse;
  }

  .scroller[data-direction="left"] {
    --_animation-direction: forwards;
  }

  .scroller[data-speed="fast"] {
    --_animation-duration: 50s;
  }

  .scroller[data-speed="slow"] {
    --_animation-duration: 90s;
  }

  @keyframes scroll {
    to {
      transform: translate(calc(-50% - 0.5rem));
    }
  }

  :root {
    --clr-neutral-100: hsl(0, 0%, 100%);
    --clr-primary-100: hsl(205, 15%, 58%);
    --clr-primary-400: hsl(215, 25%, 27%);
    --clr-primary-800: hsl(217, 33%, 17%);
    --clr-primary-900: hsl(218, 33%, 9%);
  }

  html {
    color-scheme: dark;
  }

  body {
    display: grid;
    min-block-size: 100vh;
    place-content: center;
    font-family: system-ui;
    font-size: 1.125rem;
    background-color: var(--clr-primary-800);
  }

  .tag-list {
    margin: 0;
    padding-inline: 0;
    list-style: none;
  }

  .tag-list li {
    padding: 1rem;
    background: var(--clr-primary-400);
    border-radius: 0.5rem;
    box-shadow: 0 0.5rem 1rem -0.25rem var(--clr-primary-900);
  }

  .test {
    background: red !important;
  }
  @media screen and (max-width: 860px) {
    .masai-msguru-hiring-partner-banner {
      font-size: 2rem;
    }

    .masai-msguru-hiring-partner-banner > span > img {
      width: 90px;
    }
  }
  @media screen and (max-width: 480px) {
    .masai-msguru-hiring-partner-banner {
      font-size: 1.5rem;
    }

    .masai-msguru-hiring-partner-banner > span > img {
      width: 70px;
    }
  }
</style>
