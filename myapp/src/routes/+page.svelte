<script>
  import Alumini from "./Alumini.svelte";
import Banner from "./Banner.svelte";
import Navbar from "./Navbar.svelte";

</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
    <Navbar/>
	<Banner/>
	<Alumini/>
	
</section>

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
