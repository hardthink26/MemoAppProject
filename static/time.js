function formatTime(past) {
    const now = new Date();
    const diff = Math.floor((now-past)/1000);
    if (diff < 60) {
        return `${diff}초 전`;
    } else if (diff < 3600) {
        return `${Math.floor(diff/60)}분 전`;
    } else if (diff < 86400) {
        return `${Math.floor(diff/3600)}시간 전`;
    } else {
        return `${Math.floor(diff/86400)}일 전`;
    }
}
const elements = document.querySelectorAll('.memo-created-at, .memo-updated-at');
elements.forEach(element=>{
    const past = new Date(element.dataset.time);
    const text = formatTime(past);
    element.textContent = text;
});

