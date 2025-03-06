import streamlit as st

# Writing function to handle unit conversion
def convert_units(value, from_unit, to_unit, unit_category):
    conversions = {
        "Length": {
            "meter": 1,
            "kilometer": 0.001,
            "mile": 0.000621371,
            "yard": 1.09361,
            "foot": 3.28084
        },
        "Weight": {
            "gram": 1,
            "kilogram": 0.001,
            "pound": 0.00220462,
            "ounce": 0.035274,
        },
    }

    if from_unit == to_unit:
        return value

    if unit_category == "Temperature":
        if from_unit == "celsius" and to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "celsius" and to_unit == "kelvin":
            return value + 273.15
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            return (value - 32) * 5/9
        elif from_unit == "fahrenheit" and to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "kelvin" and to_unit == "celsius":
            return value - 273.15
        elif from_unit == "kelvin" and to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return value

    # Generic conversion for Length & Weight
    return value * conversions[unit_category][to_unit] / conversions[unit_category][from_unit]

# StreamLit UI
st.title("Simple Unit Converter")
st.write("📐 Length, ⚖️ Weight and 🌡️ Temperature")

unit_types = {
    "Length": ["meter", "kilometer", "mile", "yard", "foot"],
    "Weight": ["gram", "kilogram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"]
}

unit_category = st.selectbox("Select unit type:", list(unit_types.keys()))
value = st.number_input("Enter value:")
from_unit = st.selectbox("From unit:", unit_types[unit_category])
to_unit = st.selectbox("To unit:", unit_types[unit_category])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, unit_category)
    st.success(f"✅ Converted Value: {result:.2f} {to_unit}")

st.markdown("---")
st.write("A Journey of Learning & Creativity 🚀 | Built by Ume-Farwa")