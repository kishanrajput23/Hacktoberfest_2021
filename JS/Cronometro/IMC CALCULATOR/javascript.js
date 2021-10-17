function calculate() {
    var bmi;
    var result = document.getElementById("result");

    var weight = parseInt(document.getElementById("weight").value);
    document.getElementById("weight-val").textContent = weight + "kg";

    var height = parseInt(document.getElementById("height").value);
    document.getElementById("height-val").textContent = height + "cm";

    bmi = (weight / Math.pow((height / 100), 2)).toFixed(1);
    result.textContent = bmi;

    if (bmi < 18.5) {
        category = "underweight";
        result.style.color = "#ffc11c";
    } else if (bmi >= 18.5 && bmi <= 24.9) {
        category = "Normal Weight";
        result.style.color = "#007100";
    } else if (bmi >= 25 && bmi <= 29.9) {
        category = "Overweight";
        result.style.color = "#ff0000";
    } else if (bmi >= 30 && imc <= 34.9) {
        category = "Obese 1"
        resultado.style.color = "#990000"
    } else if (bmi > 35 && imc <= 39.9) {
        category = "Obese 2"
        resultado.style.color = "#440000"
    } else {
        category = "Obese 3 or Morbid"
        resultado.style.color = "#220000"

    }
    document.getElementById("category").textContent = category;
}