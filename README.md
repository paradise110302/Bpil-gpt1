<h1><Image Caption Generator></h1>
    
<h3>After researching multiple models I came across BLIP by salesforce and tried implementing the model on hugging space. I received successful results but the gneerated caption was simply a description of the image.</h3>
    https://huggingface.co/docs/transformers/model_doc/blip
https://huggingface.co/spaces/rimssss/bliptrial
<img width="859" alt="image" src="https://github.com/paradise110302/Bpil-gpt1/assets/67607497/a7e01925-120f-4427-ae2e-19590adf2fcd">

<h3>The issue was that the caption was only the description of the image and it wasn't catchy or captivating. So, to the solve the above problem I further passed the description to a GPT model along with an option for the user to submit a prompt and accordingly generate the desired caption.</h3>
    <img width="535" alt="Image2" src="https://github.com/paradise110302/Bpil-gpt1/assets/67607497/07b01c80-3d38-440b-ba08-bfb3ab43f307">
    <img width="946" alt="image" src="https://github.com/paradise110302/Bpil-gpt1/assets/67607497/51aaf7b6-36ec-4270-8283-4926beed8946">
<h3>And thus the model was able to generate "catchy" (as prompted by the user) captions which can easily be used as an actual caption for social media posts.</h3>
    
    <h2>Requirements</h2>
    <h4> -Transformer </h4>
    <h4> -Torch </h4>
    <h4> - Flask </h4>

    
