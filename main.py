from pyscript import document

gradeten = {'Athena Alfaro', 'Bela Allas', 'Lindsay Esguerra'}
gradenine = {'Katniss Everdeen', 'Jude Duarte', 'Evangeline Fox'}
gradeeight = {'Daisy Maria', 'Lara Jean Covey', 'Clementine West'}
gradeseven = {'Cecilia Lisbon', 'Susanna Kaysen', 'Esther Greenwood'}

superset = gradeten | gradenine | gradeeight | gradeseven


def getname(event):
    firstname = document.getElementById('fname').value.title().strip()
    lastname = document.getElementById('lname').value.title().strip()

    full_name = firstname + " " + lastname

    superset.add(full_name)

    output = document.getElementById("output")
    output.innerHTML = ""

    for name in sorted(superset):
        output.innerHTML += f"<p>{name}</p>"

    output.innerHTML += f"<p>Total students: {len(superset)}</p>"