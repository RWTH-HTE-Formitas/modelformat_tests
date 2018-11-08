Converts all files in the IFC folder into collada and gltf format

--------------------------------------------------------------------

REQUIREMENTS:

Install IFC open shell (http://ifcopenshell.org/ifcconvert.html)
and COLLADA2GLTF (https://github.com/KhronosGroup/COLLADA2GLTF)

Compile COLLADA2GLTF

Create folder "Binaries" and put binary files
	COLLADA2GLTF-bin IfcConvert
into this folder

Create folder "data/IFC"

--------------------------------------------------------------------
Usage:

put IFC files in "data/IFC" that you want to convert

run ./IFCtoGLTF.sh
