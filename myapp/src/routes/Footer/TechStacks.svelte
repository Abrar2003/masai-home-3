<script>
  let isMedia = 460;
  let techStacks = [
    { skill: "Full Stack Web Development - Full Time", id: 1 },
    { skill: "Data Analytics - Full Time", id: 2 },
    { skill: "Mobile Development - Full Time", id: 3 },
    { skill: "Software Testing & Automation - Full Time", id: 4 },
    { skill: "Backend Development - Full Time", id: 5 },
  ];
</script>

<div class="masai-tech-stack-main" class:guru={isMedia}>
  {#each techStacks as skill (skill.id)}
    <span class="masai-techStack">{skill.skill}</span>
  {/each}
</div>

<style>
  .masai-tech-stack-main {
    padding: 1rem;
    width: 70%;
   
  }
  .masai-techStack {
    display: inline-block;
    margin: 16px 0px 0px 32px;
    background-color: rgb(255, 255, 255);
    color: black;
    font-size: 14px;
    font-weight: 600;
    padding: 10px 16px;
    border-radius: 35px;
  }
  @media screen and (max-width: 560px) {
    .guru {
      width: auto;
    }
    .masai-techStack {
      width: fit-content;
    }
  }
</style>
