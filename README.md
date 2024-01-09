<img src="./images/logom2.png" alt="Logo of the project" align="right">
<br/><br/>

## **[ XMLparser ]**
**Simple parser for modifying all xml files of a certain type inside a folder.
This parser is used to modify the size of hangars in the game [Stormworks](https://store.steampowered.com/app/573090/Stormworks_Build_and_Rescue/).**

---

### **[ WARNING! ]**
This parser can create additional file and directory (```Roaming\xml_parser\xml_parser.cfg```).
Also parser can modificate all ```.xml``` files in a folder.
The program in the releases was compiled with a custom image in the PySimpleGui module, so its weight will be different if you try to compile it yourself. 
(if you want to compile the same program as mine, replace your ```Lib\site-packages\PySimpleGUI\PySimpleGui.py``` file with the one given in the "Changed module" folder)

---

### **[ Options ]**
The first input uses for entering path of tiles folder. (```...\Stormworks\rom\data\tiles```)
(The parser remembers the entered path by creating a file ```xml_parser.cfg``` in the ```Roaming\xml_parser\``` directory
and saving the entered path there. Then the next time you start the path input field will be automatically filled in with the contents of the file.)

The second input uses for entering a number of blocks in each dimension to be added to a hanger. (default value is ```400```)

The third input can change the pattern for searching ```.xml``` files. (default str. value is ``` '*island*.xml' ```, to change all ```.xml``` files in a folder enter ```*.xml``` )

---

### **[ Exceptions ]**
*```"Please enter correct path to the tiles folder!"```* | A non-existent path to the tiles folder was entered. The error is related to 1 input field.

*```"Wrong path or incorrect additional params!"```* | The folder exists but no ```.xml``` files were found in it or they do not match the additional params search pattern. The error is related to 1 or 3 input fields.

*```"Broken files"```* | Error when changing ```.xml``` file, the chance of occurrence is minimal. The error is related to 1 input field.

---
