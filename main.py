from pyscript import display, document # pyright: ignore[reportMissingImports]

def ordering_form(e):
    item1 = document.getElementById("menu1")
    item2 = document.getElementById("menu2")
    item3 = document.getElementById("menu3")
    item4 = document.getElementById("menu4")
    item5 = document.getElementById("menu5")
    total = (float(item1.value) * item1.checked + 
             float(item2.value) * item2.checked + 
             float(item3.value) * item3.checked + 
             float(item4.value) * item4.checked + 
             float(item5.value) * item5.checked)
    display(f"Total: {total}", target="output")

    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value
    message = f"""
    <b>Name:</b> {name}<br>
    <b>Address:</b> {address}<br>
    <b>Contact Number:</b> {contact}
    """
    document.getElementById("contact_output").innerHTML = message