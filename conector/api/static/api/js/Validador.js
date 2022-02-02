const $formularioActualizar=document.getElementById('formularioActualizar');
const $scampaña=document.getElementById('scampaña');

(function(){

    $formularioActualizar.addEventListener('submit', function (e) {
        let status = String($scampaña.value);
        if ( status != True || status != False){
            alert("Valor invalido por favor indicar solo con Valores 'True' o 'False' ");
            e.preventDefault();
        }
    });
})();

