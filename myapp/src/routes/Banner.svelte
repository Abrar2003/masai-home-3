<script>
    import { onMount, onDestroy } from "svelte";
  
    let isDesktop = false;
    let isTablet = false;
    let isMobile = false;
  
    function checkScreenSize() {
      const screenWidth = window.innerWidth;
      isDesktop = screenWidth >= 1024;
      isTablet = screenWidth >= 768 && screenWidth < 1024;
      isMobile = screenWidth < 768;
    }
  
    onMount(() => {
      if (typeof window !== "undefined") {
        checkScreenSize();
        window.addEventListener("resize", checkScreenSize);
      }
    });
  
    onDestroy(() => {
      if (typeof window !== "undefined") {
        window.removeEventListener("resize", checkScreenSize);
      }
    });
  </script>
  
  {#if isDesktop || isTablet}
    <img src="https://masai-website-images.s3.ap-south-1.amazonaws.com/banner_h_1_3d43d26bd0.webp" alt="Desktop Banner" />
  {:else if isMobile}
    <img src="https://masai-website-images.s3.ap-south-1.amazonaws.com/banner_m_1_b63dd244db.webp" alt="Mobile Banner" />
  {/if}
  
  <style>
    img {
      width: 100%;
    }
  </style>
  