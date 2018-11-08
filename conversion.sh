for format in "gltf" "collada" "obj"
  do
    if [ ! -d "data/$format" ]; then
      mkdir -p "data/$format";
    fi
  done

for a in data/IFC/*.ifc ; do
    d=$(basename $a .ifc)
    echo "converting $d"
    ./Binaries/IfcConvert data/IFC/$d.ifc data/obj/$d.obj
    ./Binaries/IfcConvert data/IFC/$d.ifc  data/collada/$d.dae
    ./Binaries/COLLADA2GLTF-bin -i data/collada/$d.dae -o data/gltf/$d.gltf
done
