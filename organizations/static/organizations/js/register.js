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

    return errors;
}

function validateOrganizationForm(){
    let errors = {};    

    return errors;
}

function validateAddressForm(){
    let errors = {};    

    return errors;
}

function registerAdress(){
    var cookies = getCookie('ongs_session');
    var session = (cookies) ? JSON.parse(atob(cookies)): null;

    $.get('/ongs/organizations/register/address', function(response){
        // console.log('clicked!');
        $('.content-body').html(response['content_html']);
        
        $('#organization_id').val((session) ? session.organization.id: 6);

        $('button#register-address').click(function(){
            let errors = validateAddressForm();
            if(Object.keys(errors).length > 0){

            } else {
                $.post('/ongs/organizations/register/address', $('#form-address-register').serialize(), function(response){
                    
                })
            }
        })
    })
}

function registerOrganization(){
    var cookies = getCookie('ongs_session');
    var session = (cookies) ? JSON.parse(atob(cookies)): null;

    $.get('/ongs/organizations/register/organization', function(response){
        $('.content-body').html(response['content_html']);

        $('#session_uuid').val(session.uuid);
        
        $('button#register-organization').click(function(){
            let errors = validateOrganizationForm();
            if(Object.keys(errors).length > 0){

            } else {
                $.post('/ongs/organizations/register/organization', $('#form-organization-register').serialize(), function(response){
                    session['organization'] = response['organization']['value'];
                    setCookie('ongs_session', btoa(JSON.stringify(session)), session.expires_at);
                    registerAdress();
                })
            }

        })
    })
}

function registerUser(){
    $.get('/ongs/organizations/register/user', function(response){
        $('.content-body').html(response['content_html']);

        $('button#register-user').click(function(){
            let errors = validateUserForm();
            if(Object.keys(errors).length > 0){
                $('.username-error').html('<p>'+errors['username']+'</p>');
                $('.email-error').html('<p>'+errors['email']+'</p>');
                $('.password-error').html('<p>'+errors['password']+'</p>');
            } else {
                $.post('/ongs/organizations/register/user', $('#form-user-register').serialize(), function(response){
                    if(!response['error']){
                        setCookie('ongs_session', btoa(JSON.stringify(response['session'])), response['session'].expires_at);
                        
                        registerOrganization();
                    }
                })
            }
        });
    })
}

(function(){
    // registerUser();
    // registerOrganization();
    registerAdress();
})();