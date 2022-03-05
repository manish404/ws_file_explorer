/**
 * Handles click event
 */
function makeReq(path) {
    fetch('/dir', {
        method: 'post',
        cors: 'cors',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'path': path })
    });
}
// 
const links = document.querySelectorAll('.link');
const pathEl = document.querySelector('#path>span');
links.forEach(link => {
    link.addEventListener('click', () => {
        const reqType = link.getAttribute('data-type'); // file or folder
        const path = link.getAttribute('data-name')
        // 
        makeReq(pathEl.innerText.trim());
        document.location.pathname = reqType + '/' + path;
    });
});