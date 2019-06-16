function validateUserForm(){
    let errors = {};

    if($('#username').val() === ''){
        errors['username'] = '* nome de usuário vazio';
    }

    if($('#email').val() === ''){
        errors['email'] = '* email vazio';
    } else if($('#email').val() !== $('#email_confirmation').val()){
        errors['email'] = '* email e confirmação de email não conferem \n';
    }

    if($('#password').val() === ''){
        errors['password'] = '* senha vazia';
    } else if($('#password').val() !== $('#password_confirmation').val()){
        errors['password'] = '* senha e confirmação de senha não conferem'
    }

    return errors
}

(function(){

    $.get('/ongs/organizations/register/user', function(response){
        $('.container-content').html(response['content_html']);

        $('button#register-user').click(function(){
            let errors = validateUserForm();
            if(Object.keys(errors).length > 0){
                $('.username-error').html('<p>'+errors['username']+'</p>');
                $('.email-error').html('<p>'+errors['email']+'</p>');
                $('.password-error').html('<p>'+errors['password']+'</p>');
            } else {
                $.post('/ongs/organizations/register/user', $('#form-user-register').serialize(), function(response){
                    console.log(response);
                })
            }
        });
    })
})();