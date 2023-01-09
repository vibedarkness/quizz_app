const modalBtns= [...document.getElementsByClassName('modal-button')]
const modalBody= document.getElementById('modal-body-confirm')
modalBtns.forEach(modalBtn=>modalBtn.addEventListener('click',()=>{
    const id= modalBtn.getAttribute('data-id')
    const name= modalBtn.getAttribute('data-name')
    const numQuestions= modalBtn.getAttribute('data-nombre_de_question')
    const niveau= modalBtn.getAttribute('data-niveau')
    const score_passe= modalBtn.getAttribute('score_passe')
    const temps= modalBtn.getAttribute('data-temps')

    modalBody.innerHTML=`
    <div class="h5 mb-3">Etes vous sur de vouloir passer le test "<b>${name}</b></div>
    <div class="text-muted">
    <ul>
        <li>Niveau:${niveau}</li>
        <li>Nombre de question:${nombre_de_question}</li>
        <li>Score demander pour passer:${score_passe}</li>
        <li>Temps:${temps}</li>
    </ul>
    </div>

    `
    
}))