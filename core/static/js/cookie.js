function getCookie(cname) {
    let name = cname + '=';
    let ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) === 0) {
            return c.substring(name.length, c.length);
        }
    }
    return null;
}

function setCookie(name, value, expires_at) {
    let d = new Date(expires_at);
    let expires = 'expires=' + d.toUTCString();
    document.cookie = name + '=' + value + '; ' + expires + '; path=/';
}

function validationCookie(session) {
    if (session.active) {
        let createdAt = new Date(session.startedAt)
        let now = new Date();
        let diff = now.getTime() - createdAt.getTime();
        if ((diff/(1000*60*60*24)) < 1)  {
            return true
        }
    }
    return false
}

function clearCookie(name, value){
    let expires = 'expires=' + new Date().toUTCString();
    document.cookie = name + '=' + value + '; ' + expires + '; path=/';
};
