const url = window.location.href

const quizBox=document.getElementById('quiz-box')


$.ajax({
    type: 'GET',
    url: `${url}donnée`,
    success:function(response){
        console.log(response);
        const data=response.data
        data.forEach(el => {
            for (const [questions, reponses] of Object.entries(el)) {
                quizBox.innerHTML += `
                <div class="mb-2">
                <br>
                <h3><b>${questions}</b></h3>
                </div>
                
                `
            reponses.forEach(reponses => {
                quizBox.innerHTML += `
                

               <div >
                
                <input class="ans" type="radio" id=" ${questions}-${reponses}" name="${questions}" value="${reponses}">
                <label  for="${questions}"> ${reponses}</label>
                </div>
                `
            });
                
            }
        });
    }
})