<script>

  import BrandCarousel from "./BrandCarousel/BrandCarousel.svelte";

  import Alumini from "./Alumini.svelte";
  import Banner from "./Banner.svelte";
  import Courses from "./Courses.svelte";

  import CareerPossibilities from "./CareerPossibilities/CareerPossibilities.svelte";
  import CertificateNsdc from "./CertificateByNSDC/CertificateNSDC.svelte";
  import Footer from "./Footer/Footer.svelte";
  import MasaiNews from "./MasaiNews/MasaiNews.svelte";
  import Navbar from "./Navbar.svelte";
  import StudentImpact from "./StudentImpact/StudentImpact.svelte";
  import ScrollerSlide from "./ScrollerSlide.svelte";
  import Sidebar from "./Sidebar.svelte";
</script>

<svelte:head>
  <title>Home</title>
  <meta name="description" content="Svelte demo app" />
</svelte:head>

<section>



  <Navbar />
 
  <Banner />
  <Sidebar />
  <Courses />
  <Alumini />
  <ScrollerSlide />


  I have One Component to Place here
  <BrandCarousel/>
  <StudentImpact />
  <CareerPossibilities />
  <CertificateNsdc />
  <MasaiNews/>
</section>
<footer>
  <Footer />
</footer>

<style>
  section {
    /* border: 1px solid black; */
    width: 100%;
    /* display: flex; */
    /* flex-direction: column; */
    /* justify-content: center; */
    /* align-items: center; */
    /* flex: 0.6; */
  }
</style>
