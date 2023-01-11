
// const resultatBtn=document.getElementById('resultat-btn')
const url = window.location.href

const quizBox=document.getElementById('quiz-box')

const scoreBox=document.getElementById('score-box')
const resultatBox=document.getElementById('resultat-box')


$.ajax({
    type: 'GET',
    url: `${url}donnée`,
    success:function(response){
        // console.log(response);
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

const quizForm=document.getElementById('quiz-form')
const csrf=document.getElementsByName('csrfmiddlewaretoken')


const sendData= () =>{
    const elements=[...document.getElementsByClassName('ans')]

const data= {}
data['csrfmiddlewaretoken']= csrf[0].value
elements.forEach(el=>{
    if (el.checked) {
        data[el.name]= el.value
    }else{
        if (!data[el.name]) {
            data[el.name]=null

        }
    }
})

$.ajax({
    type: 'POST',
    url: `${url}save/`,
    data:data,
    success:function(response){
        // console.log(response);
        const resultats=response.resultats
        console.log(resultats)
        quizForm.classList.add('not-visible')
        scoreBox.innerHTML=`${response.Passer ? "felicitation !" : 'Desole... ('} votre score ${response.score} est insuffisant' }`

        resultats.forEach(res => {
            const resDiv=document.createElement("div")
            for (const[questions,resp] of Object.entries(res)) {


                resDiv.innerHTML += questions
                const cls= ['container', 'p-3', 'text-light', 'h3'] 

                resDiv.classList.add(...cls)

                if (resp=='Pas de reponse') {
                    resDiv.innerHTML +='-pas de reponse' 
                    resDiv.classList.add('bg-danger')
                }else{
                    const reponses=resp["reponse_donner"]
                    const correct=resp["reponse_correct"]
                    if (reponses==correct) {
                        resDiv.classList.add('bg-success')
                        resDiv.innerHTML+= `
                        Reponse donner: ${reponses}
                        `

                    }else{
                        resDiv.classList.add('bg-danger')
                        resDiv.innerHTML+= `
                        | Reponse correct: ${correct}
                        `
                        resDiv.innerHTML+= `
                        | Reponse donner: ${reponses}
                        `
                    }
                }
                
            }
            // const body=document.getElementsByTagName('BODY')[0]
            resultatBox.append(resDiv)

        });
    },
    error:function (error) {
        console.log(error);
    }
})
}

quizForm.addEventListener('submit', e=>{
    e.preventDefault()

sendData()
})
