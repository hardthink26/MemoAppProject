const placeholder = [
    {"오늘 할 일을 적어주세요":["카페에서 공부하기", "운동 30분하기", "친구와 만나기"]},
    {"오늘 일어난 일을 적어주세요":["카페에서 공부했다.", "친구를 만나서 밥을 먹었다.", "집에서 푹 쉬었다."]},
    {"오늘 느낀 점을 적어주세요.":["많이 피곤했다.", "좋은 일이 있었다.", "더 열심히 해야겠다."]},
]
const num1  = Math.floor(Math.random() * placeholder.length);
const text = Object.keys(placeholder[num1])[0];
const num2 = Math.floor(Math.random() * placeholder[num1][text].length);
const example = placeholder[num1][text][num2];

const contentInput = document.getElementById("content");
const titleInput = document.getElementById("title");

if (contentInput) {
    contentInput.placeholder = `${example}`
}
if (titleInput) {
    titleInput.placeholder = `${text}`
}