(function(){
    console.log('executou');
    
    setTimeout(function(){ 
        $('button#login-button').click(function(){
            console.log('clicado!');
            $.post('/ongs/organizations/login', $('#form-login').serialize(), function(response){
                console.log(response);
            })
        })
    }, 100)
})();