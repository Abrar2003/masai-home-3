<script>
</script>

<div class="mainGrid">
  <!-- https://masaischool.com/images/new-homepage/nsdc/nsdc-cert.jpg -->

  <div class="msguru-certificate-nsdc">
    <!-- ------------------left Side------------------ -->
    <div class="msguru-certificate-left">
        <h3 class="msguru-heading-laptopview-hide">
            <span class="msguru-certificatie-red"
              >Certification <img
                loading="lazy"
                src="https://masaischool.com/images/new-homepage/yellow-vector.svg"
                alt="Yello Underline"
              />
            </span> The N.S.D.C
          </h3>
      <img
        src="https://masaischool.com/images/new-homepage/nsdc/nsdc-cert.jpg"
        alt="NSDC Demo Certificate"
      />
    </div>
    <!-- ------------------left Side------------------ -->

    <!-- ------------Right Side-------------- -->
    <div class="msguru-certificate-right-side">
      <div>
        <h2>
          <span class="msguru-certificatie-red"
            >Certification <img
              loading="lazy"
              src="https://masaischool.com/images/new-homepage/yellow-vector.svg"
              alt="Yello Underline"
            />
          </span> The N.S.D.C
        </h2>
        <p>
          NSDC Certification is a prestigious recognition for students who have
          completed accredited skill-based training programs. It validates their
          expertise, demonstrating their dedication to practical skills. This
          certification provides a competitive edge in the job market,
          showcasing proficiency and adherence to industry standards. NSDC
          certifications are widely accepted, unlocking rewarding career
          opportunities and personal growth.
        </p>
      </div>
    </div>
    <!-- ------------Right Side-------------- -->
  </div>
</div>

<style>
    .msguru-heading-laptopview-hide{
        display: none;
    }
  .msguru-certificate-nsdc {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    width: 90%;
    margin: auto;
    /* border: 1px solid red; */
    border-radius: 10px;
    background-color: #f2f6ff;
    padding: 1rem;
    gap: 2rem;
    text-align: left;
  }
  .msguru-certificate-left {
    /* border: 3px solid red; */
    /* width: 100%; */
  }
  .msguru-certificate-left > img {
    border: 1.2px solid rgb(0, 195, 255);
    border-radius: 10px;
    width: 100%;
  }
  .msguru-certificate-right-side {
    font-size: 30px;
    font-weight: 700;
    width: 100%;
    margin-top: 3rem;
  }
  .msguru-certificate-right-side > div{
    display: flex;
    flex-direction: column;
    text-align: left;
    gap: 20px   ;
  }
  .msguru-certificate-right-side > div > h2 {
    /* border: 1px solid red; */
    
  }

  .msguru-certificate-right-side > div > p{
    font-size: 1rem;
    font-weight: 400;
    /* stroke: #ea0a0a; */
    color: #21191B;
  }
  .msguru-certificatie-red {
    color: red;
    position: relative;
  }
  .msguru-certificatie-red > img {
    position: absolute;
    left: 0;
    bottom:-7px;
    width: 200px;
  }
  @media screen and (max-width: 996px){
    .msguru-certificate-right-side {
    margin-top: 0rem;
  }
  .msguru-heading-laptopview-hide{
    padding: 10px;
    margin-bottom: 10px;
  }
  .msguru-heading-laptopview-hide>span>img{
    width: 180px;
  }
  }
  @media screen and (max-width: 760px) {
    .msguru-certificate-nsdc{
        grid-template-columns: repeat(1, 1fr);
        gap: 10px;
    }
    .msguru-heading-laptopview-hide{
        display: block;
        text-align: center;
        font-size: 30px;
    }
    .msguru-heading-laptopview-hide>h3>span>img{
        border: 1px solid red;
    }
    .msguru-certificate-right-side > div > h2{
        display: none;
    }
    /* .msguru-certificate-right-side > div > p{

    } */
  
  }
</style>
