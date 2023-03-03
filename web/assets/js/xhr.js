
function createXHR() {
    let xhr;
        try {
        xhr = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
        try {
            xhr = new ActiveXObject("Microsoft.XMLHTTP");
        } catch (e2) {
            try {
            xhr = new XMLHttpRequest();
            } catch (e3) {
            xhr = false;
            }
        }
        }
        return xhr;
    }
