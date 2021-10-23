const encoder = document.getElementById("encoder");
const decoder = document.getElementById("decoder");

encoder.addEventListener("keyup", (e) => {
  const plainText = e.currentTarget.value;
  decoder.value = encode(plainText);
});

decoder.addEventListener("keyup", (e) => {
  try {
    const chiperText = e.currentTarget.value;
    encoder.value = decode(chiperText);
  } catch (e) {
    encoder.value = "Encoded text is invalid base64";
  }
});

const encode = (value) => {
  return btoa(value);
};

const decode = (value) => {
  return atob(value);
};

// Copy Function
const copy = (target) => {
  const copyText = document.getElementById(target);
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  navigator.clipboard.writeText(copyText.value);
  alert("Text copied");
};

// Paste Function
const paste = async (target) => {
  const text = await navigator.clipboard.readText();
  if (target === "encoder") {
    encoder.value = text;
    decoder.value = encode(text);
  } else {
    decoder.value = text;
    encoder.value = decode(text);
  }
};
