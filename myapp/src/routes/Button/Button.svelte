<script>
  export let buttonData = "Apply Now";
</script>

<div>
  <button class="msguru-button-component-main">{buttonData}</button>
</div>

<style>

.msguru-button-component-main{
    padding: 14px 18px;
    font: 14px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    background-color: rgb(218, 0, 0);
    color: white;
}
.msguru-button-component-main:hover{
    background-color: rgb(186, 1, 1);
    transition: all ease .5s;
}

</style>
