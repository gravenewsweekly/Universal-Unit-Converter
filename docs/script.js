const conversions = {
    length: { meter: 1, mile: 0.000621371, kilometer: 0.001 },
    weight: { kilogram: 1, pound: 2.20462, gram: 1000 },
    temperature: { celsius: 1, fahrenheit: 1.8, kelvin: 1 }
};

document.getElementById("category").addEventListener("change", updateUnits);

function updateUnits() {
    const category = document.getElementById("category").value;
    const fromUnit = document.getElementById("fromUnit");
    const toUnit = document.getElementById("toUnit");
    fromUnit.innerHTML = toUnit.innerHTML = "";

    Object.keys(conversions[category]).forEach(unit => {
        let option1 = new Option(unit, unit);
        let option2 = new Option(unit, unit);
        fromUnit.add(option1);
        toUnit.add(option2);
    });
}

function convert() {
    const category = document.getElementById("category").value;
    const fromValue = parseFloat(document.getElementById("fromValue").value);
    const fromUnit = document.getElementById("fromUnit").value;
    const toUnit = document.getElementById("toUnit").value;

    if (category === "temperature" && fromUnit === "celsius" && toUnit === "fahrenheit") {
        document.getElementById("result").innerText = (fromValue * 1.8) + 32;
    } else {
        const factor = conversions[category][toUnit] / conversions[category][fromUnit];
        document.getElementById("result").innerText = (fromValue * factor).toFixed(4);
    }
}

// Initialize dropdown
updateUnits();
