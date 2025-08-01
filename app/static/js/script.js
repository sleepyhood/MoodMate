// 토스트 애니메이션
function showToast(message, duration = 3000) {
  const toast = document.createElement("div");
  toast.textContent = message;
  toast.classList.add("toast", "show");
  document.body.appendChild(toast); // ✅ DOM에 추가

  setTimeout(() => {
    toast.classList.remove("show");
    toast.addEventListener("transitionend", () => {
      toast.remove(); // ✅ 사라진 후 DOM에서 제거
    });
  }, duration);
}