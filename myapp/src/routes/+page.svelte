<script>
  import CareerPossibilities from "./CareerPossibilities/CareerPossibilities.svelte";
  import CertificateNsdc from "./CertificateByNSDC/CertificateNSDC.svelte";
  import Footer from "./Footer/Footer.svelte";
  import MasaiNews from "./MasaiNews/MasaiNews.svelte";
import Navbar from "./Navbar.svelte";

</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
    <Navbar/>
	<CareerPossibilities/>
	<CertificateNsdc/>
	<MasaiNews/>

</section>
<footer>
	<Footer/>
</footer>

<style>
    
	section {
		border: 1px solid black;
		width: 100%;
		/* display: flex; */
		/* flex-direction: column; */
		/* justify-content: center; */
		/* align-items: center; */
		/* flex: 0.6; */
		
	}

	
	
</style>
