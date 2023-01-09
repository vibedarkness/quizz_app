const modalBtns= [...document.getElementsByClassName('modal-button')]
const modalBody= document.getElementById('modal-body-confirm')
const startBtn=document.getElementById('start-button')
const url=window.location.href



modalBtns.forEach(modalBtn=>modalBtn.addEventListener('click',()=>{
    const id= modalBtn.getAttribute('data-id')
    const name= modalBtn.getAttribute('data-quiz')
    const numQuestions= modalBtn.getAttribute('data-questions')
    const niveau= modalBtn.getAttribute('data-niveau')
    const score_passe= modalBtn.getAttribute('data-pass')
    const temps= modalBtn.getAttribute('data-temps')

    modalBody.innerHTML=`
    <div class="h5 mb-3" >Etes vous sur de vouloir passer le test: <b>${name}</b></div>
    <div class="text-muted">
    <ul style="color:black;">
        <li>Niveau:${niveau}</li>
        <li>Nombre de question:${numQuestions}</li>
        <li>Score demander pour passer:${score_passe} %</li>
        <li>Temps:${temps} mn</li>
    </ul>
    </div>

    `
    startBtn.addEventListener('click',()=>{
        window.location.href=url + id
    })
}))